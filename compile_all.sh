#!/bin/bash

# Script para compilar todas as apresentações
# Uso: ./compile_all.sh

set -e  # Parar em caso de erro

echo "============================================"
echo "Compilando Apresentações de Bioinformática"
echo "============================================"
echo ""

# Entrar no diretório de capítulos
cd "$(dirname "$0")/capitulos"

# Contador
total=0
sucesso=0
falha=0

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Compilar cada arquivo .tex
for file in capitulo*.tex; do
    if [ -f "$file" ]; then
        total=$((total + 1))
        echo -e "${YELLOW}Compilando: $file${NC}"

        # Primeira compilação
        if pdflatex -interaction=nonstopmode -halt-on-error "$file" > /dev/null 2>&1; then
            # Segunda compilação para referências
            pdflatex -interaction=nonstopmode -halt-on-error "$file" > /dev/null 2>&1

            sucesso=$((sucesso + 1))
            echo -e "${GREEN}✓ Sucesso: ${file%.tex}.pdf${NC}"
        else
            falha=$((falha + 1))
            echo -e "${RED}✗ Falha: $file${NC}"
        fi
        echo ""
    fi
done

# Limpar arquivos auxiliares
echo "Limpando arquivos auxiliares..."
rm -f *.aux *.log *.nav *.out *.snm *.toc *.vrb 2>/dev/null || true

echo ""
echo "============================================"
echo "Resumo da Compilação"
echo "============================================"
echo -e "Total de arquivos: $total"
echo -e "${GREEN}Sucessos: $sucesso${NC}"
echo -e "${RED}Falhas: $falha${NC}"
echo ""

# Listar PDFs gerados
if [ $sucesso -gt 0 ]; then
    echo "PDFs gerados:"
    ls -lh *.pdf 2>/dev/null | awk '{print "  " $9 " (" $5 ")"}'
fi

echo ""
echo "Concluído!"

# Retornar código de saída apropriado
if [ $falha -gt 0 ]; then
    exit 1
else
    exit 0
fi
