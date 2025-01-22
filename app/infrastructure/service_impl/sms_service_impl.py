from authentication.app.application.services.sms_service import SMSService


class SMSServiceImpl(SMSService):
    async def send_sms(self, msisdn: str, otp: str):
        print(f'otp {otp} sent to {msisdn} ...')
        pass