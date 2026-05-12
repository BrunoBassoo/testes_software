class HistoricoRepositorio:
    def __init__(self) -> None:
        self._registros: list[str] = []

    def salvar(self, entrada: str) -> None:
        self._registros.append(entrada)

    def listar(self) -> list[str]:
        return self._registros

    def limpar(self) -> None:
        self._registros.clear()

    def total(self) -> int:
        return len(self._registros)
