"""
Carga (Black Friday): mix leitura / escrita com think time curto.
Uso (com API no ar):
  uvicorn app.main:app --host 127.0.0.1 --port 8000
  locust -f locustfile.py --host=http://127.0.0.1:8000
Ou headless:
  locust -f locustfile.py --host=http://127.0.0.1:8000 --users 200 --spawn-rate 20 --run-time 60s --headless
"""

from locust import HttpUser, between, task


class CompradorBlackFriday(HttpUser):
    wait_time = between(0.05, 0.25)

    @task(4)
    def ver_produto(self):
        self.client.get("/api/produto/1")

    @task(2)
    def listar_produtos(self):
        self.client.get("/api/produtos")

    @task(1)
    def adicionar_carrinho(self):
        self.client.post("/api/carrinho", json={"itens": [{"id": 1, "q": 1}]})
