from authentication.app.application.services.sms_service import SMSService
from authentication.app.infrastructure.exceptions import SMSServicesException


class SMSServiceImpl(SMSService):
    async def send_sms(self, msisdn: str, otp: str):
        try:
           print(f'otp {otp} sent to {msisdn} ...')
        except:
            raise SMSServicesException