
from authentication.app.application.usecases.refresh_token_use_case import RefreshTokenUseCase
from authentication.app.application.usecases.login_use_case import LoginUseCase
from authentication.app.application.usecases.verify_use_case import VerifyUseCase
from authentication.app.interfaces.dto.request.login_request_dto import LoginRequestDto
from authentication.app.interfaces.dto.request.refresh_token_request_dto import RefreshTokenRequestDto
from authentication.app.interfaces.dto.request.verify_request_dto import VerifyRequestDTO
from authentication.app.interfaces.dto.response.login_response_dto import LoginResponseDTO
from authentication.app.interfaces.dto.response.refresh_token_response_dto import RefreshTokenResponseDTO
from authentication.app.interfaces.dto.response.verify_response_dto import VerifyResponseDTO


class AuthController:
    def __init__(self, verify_use_case: VerifyUseCase,
                 login_use_case: LoginUseCase,
                 refresh_token_use_case: RefreshTokenUseCase):
        self.verify_use_case = verify_use_case
        self.login_use_case = login_use_case
        self.refresh_token_use_case = refresh_token_use_case


    async def request_otp(self, request_otp_request : LoginRequestDto)->LoginResponseDTO:
       return LoginResponseDTO.from_domain(await self.login_use_case.execute(msisdn=request_otp_request.msisdn))

    async def verify_otp(self, verify_request_dto : VerifyRequestDTO)->VerifyResponseDTO:
       return VerifyResponseDTO.from_domain(token_domain= await self.verify_use_case.execute(session_id=verify_request_dto.session_id,otp_code=verify_request_dto.otp))

    async def refresh_token(self, refresh_token_request : RefreshTokenRequestDto)->RefreshTokenResponseDTO:
       return RefreshTokenResponseDTO(access_token= await self.refresh_token_use_case.execute(refresh_token= refresh_token_request.refresh_token))