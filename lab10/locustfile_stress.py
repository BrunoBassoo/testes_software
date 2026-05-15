"""
Estresse / spike: ritmo agressivo e marcação de lentidão ou 503.
Uso headless (exemplo):
  locust -f locustfile_stress.py --host=http://127.0.0.1:8000 --users 500 --spawn-rate 50 --run-time 30s --headless --csv=resultado_estresse
"""

from locust import HttpUser, constant_pacing, task


class EstresseSpikeUser(HttpUser):
    wait_time = constant_pacing(0.05)

    @task
    def endpoint_catalogo(self):
        with self.client.get("/api/produtos", catch_response=True) as r:
            if r.elapsed.total_seconds() > 0.5:
                r.failure("Resposta lenta (>500ms)")
            elif r.status_code == 503:
                r.failure("Serviço indisponível")
