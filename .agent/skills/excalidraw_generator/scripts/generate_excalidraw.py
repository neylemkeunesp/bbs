#!/usr/bin/env python3
import json
import random
import time
import argparse
import sys

class ExcalidrawBuilder:
    def __init__(self):
        self.elements = []
        self.view_bg_color = "#ffffff"

    def _generate_id(self):
        # Gera um ID de 10 caracteres alfanuméricos como o Excalidraw prefere
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        return "".join(random.choice(chars) for _ in range(10))

    def _get_timestamp(self):
        return int(time.time() * 1000)

    def _base_element(self, element_type, x, y, width, height, **kwargs):
        el_id = kwargs.get("id") or self._generate_id()
        timestamp = self._get_timestamp()
        
        element = {
            "id": el_id,
            "type": element_type,
            "x": float(x),
            "y": float(y),
            "width": float(width),
            "height": float(height),
            "angle": 0.0,
            "strokeColor": kwargs.get("stroke_color", "#1e1e1e"),
            "backgroundColor": kwargs.get("bg_color", "transparent"),
            "fillStyle": kwargs.get("fill_style", "hachure"),
            "strokeWidth": kwargs.get("stroke_width", 1),
            "strokeStyle": kwargs.get("stroke_style", "solid"),
            "roughness": kwargs.get("roughness", 1),
            "opacity": kwargs.get("opacity", 100),
            "groupIds": [],
            "frameId": None,
            "roundness": {"type": 3} if kwargs.get("roundness", True) else None,
            "seed": random.randint(1, 9999999),
            "version": 1,
            "versionNonce": random.randint(1, 9999999),
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp,
            "link": None,
            "locked": False
        }
        return element

    def add_rectangle(self, x, y, width, height, text=None, **kwargs):
        rect = self._base_element("rectangle", x, y, width, height, **kwargs)
        self.elements.append(rect)
        
        if text:
            # Centraliza o texto sobre o retângulo
            font_size = kwargs.get("font_size", 20)
            font_family = kwargs.get("font_family", 1)
            self.add_text_centered_in(rect["id"], x, y, width, height, text, font_size, font_family, kwargs.get("stroke_color", "#1e1e1e"))
            
        return rect["id"]

    def add_ellipse(self, x, y, width, height, text=None, **kwargs):
        ellipse = self._base_element("ellipse", x, y, width, height, **kwargs)
        self.elements.append(ellipse)
        
        if text:
            # Centraliza o texto sobre a elipse
            font_size = kwargs.get("font_size", 20)
            font_family = kwargs.get("font_family", 1)
            self.add_text_centered_in(ellipse["id"], x, y, width, height, text, font_size, font_family, kwargs.get("stroke_color", "#1e1e1e"))
            
        return ellipse["id"]

    def add_text(self, x, y, text, font_size=20, font_family=1, text_align="center", stroke_color="#1e1e1e"):
        # Calcula dimensões aproximadas do texto para que a caixa delimitadora do Excalidraw não fique distorcida
        lines = text.split("\n")
        max_len = max(len(l) for l in lines) if lines else 0
        
        # Estimativas de largura/altura por caractere/linha
        char_width = font_size * 0.6
        line_height = font_size * 1.25
        
        width = max_len * char_width
        height = len(lines) * line_height
        
        # Ajusta coordenada x se centralizado
        if text_align == "center":
            x_pos = x - (width / 2)
        elif text_align == "right":
            x_pos = x - width
        else:
            x_pos = x

        text_element = self._base_element("text", x_pos, y, width, height, stroke_color=stroke_color, roundness=False)
        
        # Campos exclusivos de texto no Excalidraw
        text_element.update({
            "text": text,
            "fontSize": font_size,
            "fontFamily": font_family,
            "textAlign": text_align,
            "verticalAlign": "middle",
            "baseline": font_size - 2
        })
        
        self.elements.append(text_element)
        return text_element["id"]

    def add_text_centered_in(self, container_id, cx, cy, cw, ch, text, font_size=20, font_family=1, stroke_color="#1e1e1e"):
        lines = text.split("\n")
        max_len = max(len(l) for l in lines) if lines else 0
        char_width = font_size * 0.55
        line_height = font_size * 1.25
        
        text_width = max_len * char_width
        text_height = len(lines) * line_height
        
        tx = cx + (cw - text_width) / 2
        ty = cy + (ch - text_height) / 2
        
        text_element = self._base_element("text", tx, ty, text_width, text_height, stroke_color=stroke_color, roundness=False)
        text_element.update({
            "text": text,
            "fontSize": font_size,
            "fontFamily": font_family,
            "textAlign": "center",
            "verticalAlign": "middle",
            "baseline": font_size - 2,
            "containerId": container_id
        })
        
        self.elements.append(text_element)
        return text_element["id"]

    def add_arrow(self, x1, y1, x2, y2, label=None, **kwargs):
        # Uma seta é definida por um ponto inicial x, y e pontos relativos
        dx = x2 - x1
        dy = y2 - y1
        
        arrow = self._base_element("arrow", x1, y1, abs(dx), abs(dy), roundness=True, **kwargs)
        
        arrow.update({
            "points": [
                [0.0, 0.0],
                [float(dx), float(dy)]
            ],
            "lastCommittedPoint": None,
            "startBinding": None,
            "endBinding": None,
            "arrowhead": kwargs.get("arrowhead", "arrow")
        })
        
        self.elements.append(arrow)
        
        if label:
            # Adiciona um texto no ponto médio da seta
            mx = x1 + dx/2
            my = y1 + dy/2 - 15  # Levemente acima da linha
            self.add_text(mx, my, label, font_size=kwargs.get("font_size", 14), font_family=kwargs.get("font_family", 1), stroke_color=kwargs.get("stroke_color", "#1e1e1e"))
            
        return arrow["id"]

    def add_smart_connection(self, id_a, id_b, label=None, **kwargs):
        """Conecta dois elementos de forma inteligente usando os pontos médios de bordas mais próximas."""
        el_a = next((el for el in self.elements if el["id"] == id_a), None)
        el_b = next((el for el in self.elements if el["id"] == id_b), None)
        
        if not el_a or not el_b:
            return None
            
        # Coordenadas do elemento A
        xa1, ya1 = el_a["x"], el_a["y"]
        xa2, ya2 = xa1 + el_a["width"], ya1 + el_a["height"]
        cx_a, cy_a = xa1 + el_a["width"]/2, ya1 + el_a["height"]/2
        
        # Coordenadas do elemento B
        xb1, yb1 = el_b["x"], el_b["y"]
        xb2, yb2 = xb1 + el_b["width"], yb1 + el_b["height"]
        cx_b, cy_b = xb1 + el_b["width"]/2, yb1 + el_b["height"]/2
        
        # Determina os pontos de borda candidatos
        # [x, y, direcao]
        pts_a = {
            "right": [xa2, cy_a],
            "left": [xa1, cy_a],
            "bottom": [cx_a, ya2],
            "top": [cx_a, ya1]
        }
        
        pts_b = {
            "right": [xb2, cy_b],
            "left": [xb1, cy_b],
            "bottom": [cx_b, yb2],
            "top": [cx_b, yb1]
        }
        
        # Seleciona o melhor par de pontos de conexão baseado na proximidade e direção relativa
        best_dist = float("inf")
        best_a = pts_a["right"]
        best_b = pts_b["left"]
        
        # Lógica heurística de fluxo simples
        if xb1 > xa2:  # B está à direita de A
            best_a = pts_a["right"]
            best_b = pts_b["left"]
        elif xa1 > xb2:  # A está à direita de B
            best_a = pts_a["left"]
            best_b = pts_b["right"]
        elif yb1 > ya2:  # B está abaixo de A
            best_a = pts_a["bottom"]
            best_b = pts_b["top"]
        elif ya1 > yb2:  # B está acima de A
            best_a = pts_a["top"]
            best_b = pts_b["bottom"]
        else:
            # Fallback para distância mínima entre todas as combinações
            for dir_a, pt_a in pts_a.items():
                for dir_b, pt_b in pts_b.items():
                    dist = ((pt_a[0] - pt_b[0])**2 + (pt_a[1] - pt_b[1])**2)**0.5
                    if dist < best_dist:
                        best_dist = dist
                        best_a = pt_a
                        best_b = pt_b
                        
        return self.add_arrow(best_a[0], best_a[1], best_b[0], best_b[1], label, **kwargs)

    def to_dict(self):
        return {
            "type": "excalidraw",
            "version": 2,
            "source": "https://excalidraw.com",
            "elements": self.elements,
            "appState": {
                "viewBackgroundColor": self.view_bg_color,
                "gridSize": None
            },
            "files": {}
        }

    def save(self, filepath):
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)
        print(f"Diagrama salvo com sucesso em: {filepath}")

# Exemplos de geração de diagramas
def build_flowchart_example(filepath):
    builder = ExcalidrawBuilder()
    
    # Adicionar formas
    id_start = builder.add_ellipse(100, 100, 140, 60, "Início", bg_color="#d4edda", stroke_color="#28a745", stroke_width=2)
    id_proc1 = builder.add_rectangle(320, 90, 180, 80, "Coleta de Dados\ne Metadados", bg_color="#cce5ff", stroke_color="#004085")
    id_decision = builder.add_ellipse(580, 80, 160, 100, "Dados\nConsistentes?", bg_color="#fff3cd", stroke_color="#856404")
    id_proc_yes = builder.add_rectangle(820, 90, 180, 80, "Treinar Modelo\nde Redes", bg_color="#cce5ff", stroke_color="#004085")
    id_proc_no = builder.add_rectangle(570, 260, 180, 80, "Refinar Filtros\ne Pipeline", bg_color="#f8d7da", stroke_color="#721c24")
    
    # Conectar de forma inteligente
    builder.add_smart_connection(id_start, id_proc1)
    builder.add_smart_connection(id_proc1, id_decision)
    builder.add_smart_connection(id_decision, id_proc_yes, label="Sim")
    builder.add_smart_connection(id_decision, id_proc_no, label="Não")
    builder.add_smart_connection(id_proc_no, id_proc1)  # Retorno do pipeline
    
    builder.save(filepath)

def build_mindmap_example(filepath):
    builder = ExcalidrawBuilder()
    
    # Nó Central
    id_core = builder.add_ellipse(400, 200, 200, 80, "Biologia de\nSistemas", bg_color="#e2d9f3", stroke_color="#5f27cd", stroke_width=3, font_size=22)
    
    # Ramos
    id_r1 = builder.add_rectangle(150, 100, 160, 60, "Redes Estáticas", bg_color="#e5f5e0", stroke_color="#31a354")
    id_r2 = builder.add_rectangle(650, 100, 160, 60, "Modelagem Dinâmica", bg_color="#fee0d2", stroke_color="#de2d26")
    id_r3 = builder.add_rectangle(150, 320, 160, 60, "ômicas e Dados", bg_color="#e0f3db", stroke_color="#43a2ca")
    id_r4 = builder.add_rectangle(650, 320, 160, 60, "Inteligência Artificial", bg_color="#e0ecf4", stroke_color="#8856a7")
    
    # Conexões
    builder.add_smart_connection(id_core, id_r1, arrowhead=None, stroke_width=2, stroke_color="#5f27cd")
    builder.add_smart_connection(id_core, id_r2, arrowhead=None, stroke_width=2, stroke_color="#5f27cd")
    builder.add_smart_connection(id_core, id_r3, arrowhead=None, stroke_width=2, stroke_color="#5f27cd")
    builder.add_smart_connection(id_core, id_r4, arrowhead=None, stroke_width=2, stroke_color="#5f27cd")
    
    builder.save(filepath)

def main():
    parser = argparse.ArgumentParser(description="Excalidraw Diagram Generator")
    parser.add_argument("output", help="Caminho do arquivo de saída .excalidraw")
    parser.add_argument("--type", choices=["flowchart", "mindmap"], default="flowchart", help="Tipo de diagrama pré-definido para gerar")
    
    args = parser.parse_args()
    
    if args.type == "flowchart":
        build_flowchart_example(args.output)
    elif args.type == "mindmap":
        build_mindmap_example(args.output)

if __name__ == "__main__":
    main()
