from pydantic import BaseModel, Field, field_validator

# class Settings(BaseModel):
#     # Application Settings
#     APP_NAME: str = Field(...)
#     APP_ENV: str = Field(...)
#
#     # Database Settings
#     POSTGRES_USER: str = Field(...)
#     POSTGRES_PASSWORD: str = Field(...)
#     POSTGRES_DB: str = Field(...)
#     POSTGRES_HOST: str = Field(...)
#     POSTGRES_PORT: int = Field(...)
#
#     # Redis Settings
#     REDIS_HOST: str = Field(...)
#     REDIS_PORT: int = Field(...)
#     REDIS_DB: int = Field(...)
#     REDIS_PASSWORD: str = Field(None)  # Optional
#     REDIS_URL: str = Field(None)
#
#     # Kafka Settings
#     KAFKA_BOOTSTRAP_SERVERS: str = Field(...)
#
#     # JWT Settings
#     SECRET_KEY: str = Field(...)
#     ALGORITHM: str = Field(...)
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(...)
#
#     # Other Settings
#     DEBUG: bool = Field(False)
#     # Configuration for Pydantic v2
#     model_config = {
#         "env_file": ".env",
#         "env_prefix": "",  # No prefix for environment variables
#         "case_sensitive": False,  # Environment variables are case-insensitive
#     }
#
#     @field_validator("REDIS_URL", mode="after")
#     def assemble_redis_url(cls, value, values):
#         """
#         Constructs REDIS_URL from individual components if not provided.
#         """
#         if not value:
#             host = values.get("REDIS_HOST", "localhost")
#             port = values.get("REDIS_PORT", 6379)
#             db = values.get("REDIS_DB", 0)
#             password = values.get("REDIS_PASSWORD")
#
#             if password:
#                 return f"redis://:{password}@{host}:{port}/{db}"
#             return f"redis://{host}:{port}/{db}"
#         return value
#
#
#
#
# # Instantiate the settings
# settings = Settings()
