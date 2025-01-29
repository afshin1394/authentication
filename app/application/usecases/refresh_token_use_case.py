from typing import Any

from authentication.app.application.services.token_service import TokenService
from authentication.app.application.usecases.base_use_case import BaseUseCase


class RefreshTokenUseCase(BaseUseCase):


    def __init__(self, token_service: TokenService):
        self.token_service = token_service

    async def execute(self, refresh_token: str) -> Any:
        return await self.token_service.refresh_access_token(refresh_token)
