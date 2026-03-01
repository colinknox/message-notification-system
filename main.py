class NotificationService:
    def __init__(self, recipient):
        self.recipient = recipient

    def format_message(self, title, content):
        raise NotImplementedError("Must implement message formatting")

    def send_message(self, formatted_message):
        raise NotImplementedError("Must implement message sending")

    def notify(self, title, content):
        formatted_message = self.format_message(title, content)
        return self.send_message(formatted_message)

class EmailService(NotificationService):
    def __init__(self, recipient):
        super().__init__(recipient)

    def format_message(self, title, content):
        return f"Subject: {title}\n\nDear {self.recipient},\n{content}"
    
    def send_message(self, formatted_message):
        return f"Email sent to {self.recipient}"

class SMSService(NotificationService):
    def __init__(self, recipient):
        super().__init__(recipient)

    def format_message(self, title, content):
        return f"{title}: {content}"
    
    def send_message(self, formatted_message):
        return f"SMS sent to {self.recipient}"
        
class PushService(NotificationService):
    def __init__(self, recipient):
        super().__init__(recipient)

    def format_message(self, title, content):
        return f"{title} | {content}"
    
    def send_message(self, formatted_message):
        return f"Push notification sent to {self.recipient}"

def send_notifications(services, title, content):
    for current_service in services:
        print(current_service.notify(title, content))



def main():
    services = [
        EmailService("john@email.com"),
        SMSService("555-1234"),
        PushService("User123")
    ]

    send_notifications(services, "Meeting Alert", "Team meeting in 30 minutes")

if __name__ == "__main__":
    main()