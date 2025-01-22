from pydantic import BaseModel

from authentication.app.domain.entities.token_domain import TokenDomain


class VerifyResponseDTO(BaseModel):
     access_token : str
     refresh_token : str


     @classmethod
     def from_domain(cls,token_domain : TokenDomain):
          cls(
               access_token=token_domain.access_token,
               refresh_token=token_domain.refresh_token,
          )