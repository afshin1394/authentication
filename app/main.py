from fastapi import FastAPI

from authentication.app.interfaces.api.v1.endpoints.login import router

app = FastAPI(docs_url= "/api/docs", redoc_url= "/api/redoc")

app.include_router(router)