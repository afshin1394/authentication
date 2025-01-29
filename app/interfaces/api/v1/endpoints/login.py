from fastapi import APIRouter, Depends

from authentication.app.infrastructure.di.controllers.auth_controller import get_auth_controller
from authentication.app.interfaces.controller.auth_controller import AuthController
from authentication.app.interfaces.dto.request.login_request_dto import LoginRequestDto
from authentication.app.interfaces.dto.request.verify_request_dto import VerifyRequestDTO
from authentication.app.interfaces.dto.response.login_response_dto import LoginResponseDTO
from authentication.app.interfaces.dto.response.verify_response_dto import VerifyResponseDTO

router = APIRouter(prefix= "/auth")



@router.post("/login",response_model=LoginResponseDTO)
async def login(login_request : LoginRequestDto,auth_controller : AuthController = Depends(get_auth_controller)) -> LoginResponseDTO:
   return await auth_controller.login(login_dto= login_request)

@router.post("/verify",response_model=VerifyResponseDTO)
async def verify(verify_request : VerifyRequestDTO,auth_controller : AuthController = Depends(get_auth_controller)) ->VerifyResponseDTO:
   return await auth_controller.verify(verify_request)