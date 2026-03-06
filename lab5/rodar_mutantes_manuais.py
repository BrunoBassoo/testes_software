"""
Script para rodar os testes contra cada MUTANTE MANUAL e calcular a taxa de acerto.
Uso: na pasta lab5, execute: python rodar_mutantes_manuais.py

Cada mutante é aplicado no formula1.py, os testes rodam:
- Se os testes FALHAREM → mutante MORTO (bom)
- Se os testes PASSAREM → mutante SOBREVIVEU (suíte não detectou)

Taxa de mutação manual = (mutantes mortos / total de mutantes) * 100%
"""
import subprocess
import sys
from pathlib import Path

PASTA_LAB5 = Path(__file__).resolve().parent
ARQUIVO_ALVO = PASTA_LAB5 / "formula1.py"
PASTA_MUTANTES = PASTA_LAB5 / "mutantes_manuais"
MUTANTES = ["formula1_m1.py", "formula1_m2.py", "formula1_m3.py", "formula1_m4.py", "formula1_m5.py"]


def main():
    print("Rodando mutantes manuais (cada um substitui formula1.py, roda testes, restaura)...")
    if not ARQUIVO_ALVO.exists():
        print("Erro: formula1.py não encontrado em", PASTA_LAB5)
        sys.exit(1)

    original = ARQUIVO_ALVO.read_text(encoding="utf-8")
    resultados = []

    try:
        for nome in MUTANTES:
            path_mutante = PASTA_MUTANTES / nome
            if not path_mutante.exists():
                print(f"Aviso: {nome} não encontrado, pulando.")
                continue

            # Aplica o mutante (sobrescreve formula1.py)
            ARQUIVO_ALVO.write_text(path_mutante.read_text(encoding="utf-8"), encoding="utf-8")

            # Roda os testes
            r = subprocess.run(
                [sys.executable, "-m", "pytest", "test_formula1.py", "-v", "--tb=no", "-q"],
                cwd=str(PASTA_LAB5),
                capture_output=True,
                text=True,
                timeout=30,
            )

            morto = r.returncode != 0
            resultados.append((nome, morto))
            status = "MORTO" if morto else "SOBREVIVEU"
            print(f"  {nome}: {status}")

    finally:
        # Restaura o formula1.py original
        ARQUIVO_ALVO.write_text(original, encoding="utf-8")

    # Resumo
    mortos = sum(1 for _, m in resultados if m)
    total = len(resultados)
    taxa = (mortos / total * 100) if total else 0

    print()
    print("=" * 50)
    print("MUTAÇÃO MANUAL - RESULTADOS")
    print("=" * 50)
    for nome, morto in resultados:
        print(f"  {nome}: {'MORTO' if morto else 'SOBREVIVEU'}")
    print()
    print(f"Mutantes mortos: {mortos}/{total}")
    print(f"Taxa de mutação (manual): {taxa:.1f}%")
    print()
    print("Agora rode 'mutmut run' e depois 'mutmut results' para comparar com a taxa do mutmut.")


if __name__ == "__main__":
    main()
