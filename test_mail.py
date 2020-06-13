from EncodingMessages import EncodingMessage

test_message = EncodingMessage()
test_message.change_message("This is a test message from Python.")
test_message.change_recipient("jayush.arora@gmail.com")
test_message.encode_message()
test_message.send_message()