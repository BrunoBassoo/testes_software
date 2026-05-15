"""Sistema de estoque — desenvolvido guiado por testes (TDD).

Os ciclos RED → GREEN → REFACTOR estão documentados em `tests/test_estoque.py`
na ordem em que os testes foram especificados. Aqui consolidamos a API final
após refatorações (validações centralizadas, remoção de duplicação).
"""

from __future__ import annotations

from typing import Dict, List, Optional


class Estoque:
    """Armazena quantidades por nome de produto."""

    def __init__(self) -> None:
        # REFACTOR: estrutura única escolhida após os primeiros ciclos GREEN
        self._itens: Dict[str, int] = {}

    def _validar_quantidade_positiva(self, quantidade: int, operacao: str) -> None:
        # REFACTOR: extrair validação comum de adicionar/remover (DRY)
        if quantidade <= 0:
            raise ValueError(f"{operacao}: quantidade deve ser maior que zero")

    def adicionar_produto(self, nome: str, quantidade: int) -> None:
        # GREEN: acumular quantidade; REFACTOR: validação positiva extraída
        self._validar_quantidade_positiva(quantidade, "Adicionar")
        self._itens[nome] = self._itens.get(nome, 0) + quantidade

    def remover_produto(self, nome: str, quantidade: int) -> None:
        # GREEN: checar disponível antes de mutar; REFACTOR: remover chave ao zerar
        self._validar_quantidade_positiva(quantidade, "Remover")
        disponivel = self._itens.get(nome, 0)
        if quantidade > disponivel:
            raise ValueError("Não é possível remover mais unidades do que o disponível")
        novo = disponivel - quantidade
        if novo == 0:
            del self._itens[nome]
        else:
            self._itens[nome] = novo

    def consultar_quantidade(self, nome: str) -> int:
        # GREEN: inexistente => 0 via dict.get
        return self._itens.get(nome, 0)

    def listar_produtos(self) -> List[str]:
        # GREEN: apenas q > 0; REFACTOR: sorted para ordem estável
        return sorted(n for n, q in self._itens.items() if q > 0)

    def produto_mais_estocado(self) -> Optional[str]:
        # GREEN: None se vazio; maior quantidade; REFACTOR: desempate min(nomes)
        if not self._itens:
            return None
        max_q = max(self._itens.values())
        candidatos = [n for n, q in self._itens.items() if q == max_q]
        return min(candidatos)
