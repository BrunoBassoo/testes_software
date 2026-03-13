"""Mutação manual simples (Fórmula 1) com cálculo de taxa.

Este script aplica mutações básicas (troca de sinais) no `formula1.py`, roda os
mesmos testes e calcula a taxa de mutação (mutantes mortos / total).

Use:
  python mutar_manual.py

Isso pode ser útil para entender o que a ferramenta mutmut faz automaticamente.
"""

import re
import subprocess
import sys
from pathlib import Path


MUTACOES = [
    ("igual_para_diferente", "== -> !=", r"==", "!="),
    ("diferente_para_igual", "!= -> ==", r"!=", "=="),
    ("menor_igual_para_menor", "<= -> <", r"<=", "<"),
    ("maior_igual_para_maior", ">= -> >", r">=", ">"),
    ("mais_para_menos", "+ -> -", r"\+", "-"),
    ("menos_para_mais", "- -> +", r"-", "+"),
    ("vezes_para_divisao", "* -> /", r"\*", "/"),
    ("divisao_para_vezes", "/ -> *", r"/", "*"),
]


def aplicar_mutacao(codigo: str, padrao: str, substituicao: str) -> str:
    """Aplica uma única mutação (substitui a 1ª ocorrência).

    Isso ajuda a não criar mutantes excessivamente agressivos (múltiplas alterações
    no mesmo arquivo).
    """

    return re.sub(padrao, substituicao, codigo, count=1)


def rodar_testes(cwd: Path) -> bool:
    """Roda os testes e retorna True se falharem (mutante morto)."""

    result = subprocess.run(
        [sys.executable, "-m", "pytest", "test_formula1.py", "-q"],
        cwd=str(cwd),
        capture_output=True,
        text=True,
        timeout=30,
    )
    return result.returncode != 0


def rodar_mutantes_manualmente():
    """Aplica as mutações em formula1.py e calcula a taxa de mutação."""

    pasta = Path(__file__).resolve().parent
    arquivo_alvo = pasta / "formula1.py"

    if not arquivo_alvo.exists():
        print("Erro: formula1.py não encontrado em", pasta)
        sys.exit(1)

    codigo_original = arquivo_alvo.read_text(encoding="utf-8")
    resultados = []

    try:
        for nome, descricao, padrao, substituicao in MUTACOES:
            codigo_mutado = aplicar_mutacao(codigo_original, padrao, substituicao)
            arquivo_alvo.write_text(codigo_mutado, encoding="utf-8")

            morto = rodar_testes(pasta)
            resultados.append((nome, descricao, morto))
            print(f"{nome}: {'MORTO' if morto else 'SOBREVIVEU'} ({descricao})")

    finally:
        arquivo_alvo.write_text(codigo_original, encoding="utf-8")

    mortos = sum(1 for _, _, m in resultados if m)
    total = len(resultados)
    taxa = (mortos / total * 100) if total else 0.0

    print("\n=== RESULTADO DA MUTACAO MANUAL ===")
    print(f"Mutantes mortos: {mortos}/{total}")
    print(f"Taxa de mutação (manual): {taxa:.1f}%")


if __name__ == "__main__":
    rodar_mutantes_manualmente()
