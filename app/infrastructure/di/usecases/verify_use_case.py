from authentication.app.application.repository.auth_repository import AuthRepository
from authentication.app.application.services.token_service import TokenService
from authentication.app.application.usecases.verify_use_case import VerifyUseCase
from fastapi import Depends

from authentication.app.infrastructure.di.repositries.auth_repository import get_auth_repository
from authentication.app.infrastructure.di.services.token_service import get_token_service


async def get_verify_use_case(auth_repository: AuthRepository = Depends(get_auth_repository), token_service: TokenService = Depends(get_token_service)):
    return VerifyUseCase(auth_repository=auth_repository, token_service=token_service)
