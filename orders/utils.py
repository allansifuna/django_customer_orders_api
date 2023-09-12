import threading


class SMSThread(threading.Thread):

    def __init__(self, sms, message, customer_phone):
        self.sms = sms
        self.message = message
        self.customer_phone = customer_phone
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.sms.send(self.message, self.customer_phone)
            print("Message was sent")
        except Exception as e:
            raise e


class Util:
    @staticmethod
    def send_sms(sms, message, customer_phone):
        SMSThread(sms, message, customer_phone).start()
