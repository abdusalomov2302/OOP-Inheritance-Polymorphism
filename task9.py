class Notification:
    def __init__(self, recipient, message):
        self.recipient = recipient
        self.message = message

    def send(self):
        raise NotImplementedError("Hali bunday metod mavjud emas!")

class EmailNotification(Notification):
    def send(self):
        print(f"Emailingizga xabar yuborildi.{self.message}: Foydalanuvchi xabarni qabul qildi {self.recipient}")

class SMSNotification(Notification):
    def send(self):
        print(f"Sms yuborildi.{self.message}: Foydalanuvchi smsni qabul qildi {self.recipient}.")

emailNotification = EmailNotification("abdusalomov2302", "Bugun darsga bora olmayman")
smsNotification = SMSNotification("+999976122302", "darsdan chiqib uyga kel,ish bor")


emailNotification.send()
smsNotification.send()
