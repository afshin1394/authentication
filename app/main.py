from urllib.request import Request

from fastapi import FastAPI

from authentication.app.interfaces.api.v1.endpoints.login import router
from authentication.app.interfaces.middlewares.exception_handling_middleware import ExceptionHandlingMiddleware

app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc")
app.add_middleware(ExceptionHandlingMiddleware)

app.include_router(router)

