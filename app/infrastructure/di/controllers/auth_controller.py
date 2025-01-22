from authentication.app.application.usecases.refresh_token_use_case import RefreshTokenUseCase
from authentication.app.application.usecases.login_use_case import LoginUseCase
from fastapi import Depends

from authentication.app.application.usecases.verify_use_case import VerifyUseCase
from authentication.app.infrastructure.di.usecases.login_use_case import get_login_use_case
from authentication.app.infrastructure.di.usecases.refresh_token_use_case import get_refresh_token_use_case
from authentication.app.infrastructure.di.usecases.verify_use_case import get_verify_use_case
from authentication.app.interfaces.controller.auth_controller import AuthController


async def get_auth_controller(login_use_case: LoginUseCase = Depends(get_login_use_case),
                              verify_otp_use_case: VerifyUseCase = Depends(get_verify_use_case),
                              refresh_token_use_case: RefreshTokenUseCase = Depends(get_refresh_token_use_case)
                              ): return AuthController(login_use_case=login_use_case,verify_use_case=verify_otp_use_case,refresh_token_use_case=refresh_token_use_case)
