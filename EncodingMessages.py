import smtplib


def check():
    print("Would you like to encode the message? (Y?N)")
    encode = input()
    if encode == "Y" or encode == "y":
        return True
    else:
        return False


class EncodingMessage:
    msg = ""
    send_to = ""
    send_from = "codinggodnaysh@gmail.com"  # email account used to send emails
    password = "!Bewd99!"  # password to the email account used to send emails

    def __init__(self):  # constructor
        self.msg = ""
        self.send_to = ""

    def change_message(self, message):
        self.msg = message

    def change_recipient(self, to):
        self.send_to = to

    def encode_message(self):  # encodes message in the object
        encoded = ""
        for char in self.msg:
            uc = ord(char)
            encoded += str(uc)
        self.msg = encoded

    def send_message(self):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.send_from, self.password)
        server.sendmail(self.send_from, self.send_to, self.msg)
        server.quit()
