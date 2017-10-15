# Chatik. Client part
Server API:

# Request format:
 command\0params\0

# Commands:
login\0YOUR_LOGIN\0 - Login (without authentification)

sendm\0YOUR_MESSAGE\0 - Send a mess

get_5\0 - Get 5 last messages (without params)

getal\0 - Get all messages (without params)

If error occured, server will return "ERR!"
