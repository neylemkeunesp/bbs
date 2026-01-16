#!/usr/bin/env python3
import sys
import re
import os

def check_file_references(file_path, content_lines, issues):
    """Checks for missing files referenced in the tex file."""
    base_dir = os.path.dirname(os.path.abspath(file_path))
    
    # Regex for common file inclusions
    # \input{filename}, \include{filename}, \includegraphics[options]{filename}
    patterns = [
        (r'\\input\{([^}]+)\}', 'input'),
        (r'\\include\{([^}]+)\}', 'include'),
        (r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', 'includegraphics')
    ]

    for line_idx, line in enumerate(content_lines):
        # Skip comments
        if line.strip().startswith('%'):
            continue
            
        for pattern, method in patterns:
            matches = re.finditer(pattern, line)
            for match in matches:
                ref_file = match.group(1)
                
                # Handle relative paths, extensions (latex often omits .tex or image extensions)
                # This is a basic check.
                
                # 1. Try exact match
                candidates = [ref_file]
                
                # 2. Add extensions if missing
                if method in ['input', 'include'] and not ref_file.endswith('.tex'):
                    candidates.append(ref_file + '.tex')
                
                # 3. For images, we can't easily guess extension if omitted, but we can check if file exists with common image extensions
                if method == 'includegraphics':
                    image_exts = ['.png', '.jpg', '.jpeg', '.pdf', '.eps']
                    if not any(ref_file.endswith(ext) for ext in image_exts):
                         for ext in image_exts:
                             candidates.append(ref_file + ext)
                
                found = False
                for cand in candidates:
                    full_path = os.path.join(base_dir, cand)
                    if os.path.exists(full_path):
                        found = True
                        break
                
                if not found:
                    issues.append(f"Line {line_idx + 1}: Referenced file not found: '{ref_file}' (via \\{method})")

def analyze_log_file(tex_file_path, issues):
    """Parses the corresponding .log file for errors."""
    log_file_path = os.path.splitext(tex_file_path)[0] + '.log'
    
    if not os.path.exists(log_file_path):
        # It's not an error if log doesn't exist (maybe never compiled), but worth noting?
        # For now, silently skip.
        return

    try:
        with open(log_file_path, 'r', encoding='utf-8', errors='replace') as f:
            log_lines = f.readlines()
            
        for i, line in enumerate(log_lines):
            line = line.strip()
            # Look for lines starting with '!', which usually indicate errors
            if line.startswith('! '):
                # Get context from next few lines if possible
                error_msg = line
                issues.append(f"Log Error: {error_msg}")
    except Exception as e:
        issues.append(f"Could not parse log file: {str(e)}")

def analyze_tex(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    issues = []
    
    # State variables
    in_frame = False
    frame_start_line = 0
    frame_content_lines = 0
    frame_blocks = 0
    
    # Global structure tracking
    env_stack = []
    
    # Thresholds
    MAX_LINES_PER_FRAME = 10
    MAX_BLOCKS_PER_FRAME = 3

    print(f"Analyzing {file_path}...\n")

    # 1. Analyze LaTeX Structure and Overfull Frames
    for i, line in enumerate(lines):
        line_num = i + 1
        stripped = line.strip()
        
        # Skip comments
        if stripped.startswith('%'):
            continue
            
        # Check for environment start
        start_match = re.search(r'\\begin\{([^}]+)\}', stripped)
        if start_match:
            env_name = start_match.group(1)
            env_stack.append((env_name, line_num))
            
            if env_name == 'frame':
                if in_frame:
                    issues.append(f"Line {line_num}: Nested 'frame' detected (previous started at {frame_start_line}).")
                in_frame = True
                frame_start_line = line_num
                frame_content_lines = 0
                frame_blocks = 0
            
            if in_frame and env_name in ['block', 'alertblock', 'exampleblock']:
                frame_blocks += 1

        # Check for environment end
        end_match = re.search(r'\\end\{([^}]+)\}', stripped)
        if end_match:
            env_name = end_match.group(1)
            
            if not env_stack:
                issues.append(f"Line {line_num}: Unexpected \\end{{{env_name}}}. Stack is empty.")
            else:
                last_env, start_line = env_stack.pop()
                if last_env != env_name:
                    issues.append(f"Line {line_num}: Mismatched \\end{{{env_name}}}. Expected \\end{{{last_env}}} (started at {start_line}).")
            
            if env_name == 'frame':
                in_frame = False
                # Check frame statistics
                if frame_content_lines > MAX_LINES_PER_FRAME:
                    issues.append(f"Frame (Lines {frame_start_line}-{line_num}): Too dense ({frame_content_lines} text lines > {MAX_LINES_PER_FRAME}).")
                if frame_blocks > MAX_BLOCKS_PER_FRAME:
                    issues.append(f"Frame (Lines {frame_start_line}-{line_num}): Too many blocks ({frame_blocks} > {MAX_BLOCKS_PER_FRAME}).")

        # Count content lines inside frame
        if in_frame and stripped and not stripped.startswith('\\begin') and not stripped.startswith('\\end') and not stripped.startswith('%'):
             # Heuristic: exclude simple formatting or empty title lines if needed, but keeping it simple for now
             frame_content_lines += 1

    # Final check for unclosed environments
    if env_stack:
        for env, start in env_stack:
            issues.append(f"Unclosed environment: '{env}' started at line {start}.")

    # 2. Check File References
    check_file_references(file_path, lines, issues)

    # 3. Analyze Log File
    analyze_log_file(file_path, issues)

    # Report results
    if issues:
        print("Issues Found:")
        for issue in issues:
            print(f" - {issue}")
        sys.exit(1) # Issues found
    else:
        print("No apparent issues found.")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 analyze_frames.py <path_to_tex_file>")
        sys.exit(1)
    
    analyze_tex(sys.argv[1])
