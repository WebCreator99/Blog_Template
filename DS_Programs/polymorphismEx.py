class Notification:
    def send(self):
        print("Notification sent")

class EmailNotification(Notification):
    def send(self):
        print("Emain sent")

class SMSNotification(Notification):
    def send(self):
        print("SMS sent")

Messages = [EmailNotification(), SMSNotification(), Notification()]
for SMS in Messages:
    SMS.send()