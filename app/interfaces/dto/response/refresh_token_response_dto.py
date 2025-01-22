from pydantic import BaseModel

class RefreshTokenResponseDTO(BaseModel):
     access_token: str

