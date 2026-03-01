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
        return f"Subject: {title}\n\nDear {self.recipient} \n{content}"
    
    def send_message(self, formatted_message):
        return f"Email sent to {self.recipient}"


def main():
    test = EmailService("Adam")
    
    # print(test.format_message("Flipping Awesome News!", "i tootin' like putin"))
    # print(f"DEBUG: Format message = {test.format_message("Flipping Awesome News!", "i tootin' like putin")}")
    # print(test.send_message("wowie zowie"))
    # print(f"DEBUG: Send message = {test.send_message("wowie zowie")}")
    print(test.notify("Flipping Awesome News!", "i tootin' like putin"))


if __name__ == "__main__":
    main()
