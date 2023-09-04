# GRANT ALL PRIVILEGES ON DATABASE hamzoooz TO hamzoooz;
# ALTER ROLE hamzoooz SET client_encoding TO 'utf8';
# ALTER ROLE hamzoooz SET default_transaction_isolation TO 'read committed';
# ALTER ROLE hamzoooz SET timezone TO 'UTC';


# # import os 
# # # /home/hamzoooz/.local/share/Zeal/

# # dir = "/home/hamzoooz/.local/share/Zeal/"
# # def change_permissions(dir):
# #     # Set read, write, and execute permissions for all users
# #     os.chmod(directory, 0o777)

# #     # Recursively change permissions for all child files and directories
# #     for root, dirs, files in os.walk(directory):
# #         for dir in dirs:
# #             os.chmod(os.path.join(root, dir), 0o777)
# #         for file in files:
# #             os.chmod(os.path.join(root, file), 0o777)

# # To get all posts in your channel in Telegram using Python,
# # you can use the Telethon library. Here's an example code that
# # will fetch all posts from a channel:

# # Replace the values below with your own API ID, API hash, and phone number
# # api_id = 123456
# # api_hash = 'your_api_hash'
# # phone_number = '+1234567890'

# # # Initialize the Telegram client
# # client = TelegramClient('session_name', api_id, api_hash)

# # # Start the client
# # client.start(phone_number)

# # # Get the channel entity
# # channel = client.get_entity('your_channel_name')

# # # Get all posts in the channel
# # posts = client.get_messages(channel, limit=None)

# # # Print the posts
# # for post in posts:
# #     print(post.text)

# import staticfiles_urlpatterns

# # Replace the values below with your own API ID, API hash, and phone number
# from telethon.sync import TelegramClient
# api_id = 23741394
# api_hash = 'ac7aff1d5698c4f832501d4852b31f0a'
# phone_number = '+249 99 934 7606'

# # Initialize the Telegram client
# client = TelegramClient('session_name', api_id, api_hash)
# # Start the client
# client.start(phone_number)
# # Get the channel entity
# channel = client.get_entity('channel_name')
# # Iterate through all the messages in the channel
# async for message in client.iter_messages(channel):
#     # Check if the message contains a file
#     if message.media:
#         # Print the ID of the message
#         print(message.id)

# # Stop the client
# client.disconnect()

# # #########################################################################
# # To forward a post from one channel to another channel in Telegram using Python and the
# # Telethon library, you can use the forward_messages method. Here's an example code that will 
# # forward the latest post from one channel to another channel:

# # Initialize the Telegram client
# # client = TelegramClient('session_name', api_id, api_hash)

# # # Start the client
# # client.start(phone_number)

# # # Get the source channel entity

# # # Get the source channel entity
# # source_channel = client.get_entity('l_alnader2')

# # # Print the name of the source channel
# # print(source_channel.title)

# # # Stop the client
# # client.disconnect()


# # ######################################################################3
# # To get all the IDs for files from a channel in Telegram using Python and the Telethon 
# # library, you can use the iter_messages method. Here's an example code that will
# # iterate through all the messages in a channel and print the ID of any 
# # message that contains a file:


# # Replace the values below with your own API ID, API hash, and phone number
# # from telethon import TelegramClient
# # # Initialize the Telegram client
# async def main():
#     async with TelegramClient('session_name', api_id, api_hash) as client:
#         # Get the channel entity
#         channel = await client.get_entity('l_alnader2')

#         # Iterate through all the messages in the channel
#         async for message in client.iter_messages(channel):
#             # Check if the message contains a file
#             if message.media:
#                 # Print the ID of the message
#                 print(message.id)

# # Start the main function
# with client:
#     client.loop.run_until_complete(main())



# # Make sure to replace the values for api_id, api_hash, phone_number, and channel_name 
# # with your own values. The iter_messages method takes one argument: the entity
# # to iterate through (in this case, the channel entity). The async 
# # for loop will iterate through all the messages in the 
# # channel, and the if statement will check if each
# # message contains a file. If a message does
# # contain a file, its ID will be printed. Finally
# # , don't forget to stop the client using the disconnect method.