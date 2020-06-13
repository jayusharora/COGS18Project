from EncodingMessages import EncodingMessage, check

email = EncodingMessage()

print("Hello! Please enter the message you would like to email: ")
message = input()
email.change_message(message)

print("Please enter the recipients email address: ")
send_to = input()
email.change_recipient(send_to)

encode = check()

if encode:
    email.encode_message()
    email.send_message()
    print("Message has been encoded and sent to " + send_to + "!")
else:
    email.send_message()
    print("Message has been sent to " + send_to + " without encoding!")