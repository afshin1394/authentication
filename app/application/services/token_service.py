from abc import ABC, abstractmethod

from abcem.app.domain.entities.users_domain import UserDomain
from authentication.app.domain.entities.token_domain import TokenDomain


class TokenService(ABC):
    @abstractmethod
    async def generate_tokens(self, session_id: str,otp_code : str) -> TokenDomain:
        pass

    @abstractmethod
    async def refresh_access_token(self, refresh_token: str) -> str:
        pass

    @abstractmethod
    async def generate_session_id(self, user: UserDomain) -> str:
        pass