from fastapi import Depends

from authentication.app.application.repository.auth_repository import AuthRepository
from authentication.app.application.services.sms_service import SMSService
from authentication.app.application.services.token_service import TokenService
from authentication.app.application.usecases.login_use_case import LoginUseCase
from authentication.app.infrastructure.di.repositries.auth_repository import get_auth_repository
from authentication.app.infrastructure.di.services.sms_service import get_sms_service
from authentication.app.infrastructure.di.services.token_service import get_token_service


async def get_login_use_case(auth_repository: AuthRepository = Depends(get_auth_repository),sms_service: SMSService = Depends(get_sms_service), token_service: TokenService = Depends(get_token_service)):
    return LoginUseCase(auth_repository=auth_repository, sms_service= sms_service,token_service=token_service)