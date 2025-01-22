from pydantic import BaseModel

from authentication.app.domain.entities.otp_domain import LoginDomain


class LoginResponseDTO(BaseModel):
    session_id : str
    otp:str

    @classmethod
    def from_domain(cls, otp_domain: LoginDomain) :
        cls(
            session_id=otp_domain.session_id,otp=otp_domain.otp
        )