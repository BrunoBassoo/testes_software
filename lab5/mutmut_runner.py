"""Exemplo simples de uso da biblioteca mutmut.

Este script demonstra como importar o mutmut e executar uma corrida de mutação.

Nota: para funcionar, instale:
    pip install mutmut

Uso:
    python mutmut_runner.py
"""

import sys


def main() -> int:
    try:
        import mutmut
    except ImportError:
        print("Erro: mutmut não está instalado. Instale com: pip install mutmut")
        return 1

    # mutmut expõe a função `mutmut.cli.main` para rodar a ferramenta via código.
    # Aqui usamos a interface de linha de comando interna para rodar uma sessão simples.
    try:
        from mutmut import cli
    except ImportError:
        print("Erro: não foi possível importar `mutmut.cli`. Verifique a instalação de mutmut.")
        return 1

    # Rodar mutmut como se fosse: `python -m mutmut run`
    return cli.main(["run"])


if __name__ == "__main__":
    raise SystemExit(main())
