from __future__ import annotations

import time
from collections import defaultdict, deque

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


def _client_ip(request: Request) -> str:
    forwarded = request.headers.get("x-forwarded-for")
    if forwarded:
        return forwarded.split(",")[0].strip()
    if request.client:
        return request.client.host
    return "unknown"


class RateLimitPerMinuteMiddleware(BaseHTTPMiddleware):
    """Limite simples por IP: 100 requisições por minuto (janela deslizante ~60s)."""

    def __init__(self, app, max_per_minute: int = 100, window_seconds: float = 60.0):
        super().__init__(app)
        self.max_per_minute = max_per_minute
        self.window = window_seconds
        self._hits: dict[str, deque[float]] = defaultdict(deque)

    async def dispatch(self, request: Request, call_next):
        ip = _client_ip(request)
        now = time.monotonic()
        dq = self._hits[ip]
        while dq and now - dq[0] > self.window:
            dq.popleft()
        if len(dq) >= self.max_per_minute:
            return JSONResponse(
                status_code=429,
                content={
                    "detail": "RATE_LIMIT_EXCEEDED",
                    "limite_por_minuto": self.max_per_minute,
                },
            )
        dq.append(now)
        return await call_next(request)


app = FastAPI(title="E-commerce Demo Black Friday", version="1.0.0")
app.add_middleware(RateLimitPerMinuteMiddleware, max_per_minute=100, window_seconds=60.0)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/api/produtos")
async def listar_produtos():
    return [{"id": i, "nome": f"Produto {i}", "preco": float(10 * i)} for i in range(1, 11)]


@app.get("/api/produto/{produto_id}")
async def obter_produto(produto_id: int):
    return {
        "id": produto_id,
        "nome": f"Item {produto_id}",
        "preco": 99.90,
        "estoque": 500,
    }


@app.post("/api/carrinho")
async def adicionar_carrinho(payload: dict):
    return {"carrinho_id": 1, "itens": payload.get("itens", []), "total": 0.0}
