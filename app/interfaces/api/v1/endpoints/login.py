from fastapi import APIRouter, Depends

from authentication.app.infrastructure.di.controllers.auth_controller import get_auth_controller
from authentication.app.interfaces.controller.auth_controller import AuthController
from authentication.app.interfaces.dto.request.login_request_dto import LoginRequestDto
from authentication.app.interfaces.dto.request.verify_request_dto import VerifyRequestDTO
from authentication.app.interfaces.dto.response.login_response_dto import LoginResponseDTO
from authentication.app.interfaces.dto.response.verify_response_dto import VerifyResponseDTO

router = APIRouter()



@router.post("/login",response_model=LoginResponseDTO)
async def login(login_request : LoginRequestDto,auth_controller : AuthController = Depends(get_auth_controller)):
   return await auth_controller.login_use_case.execute(login_request.msisdn)

@router.post("/verify",response_model=VerifyResponseDTO)
async def verify(verify_request : VerifyRequestDTO,auth_controller : AuthController = Depends(get_auth_controller)):
   return await auth_controller.verify_use_case.execute(session_id= verify_request.session_id,otp_code= verify_request.otp)