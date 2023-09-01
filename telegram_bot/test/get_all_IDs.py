# # To fix the NameError: name 'asyncio' is not defined error, you need to import the asyncio module at the beginning of your code. Here's the updated code with the necessary import statement:
# import asyncio
# from telethon.sync import TelegramClient

# async def get_all_ids():
#     # Replace the values below with your own API ID, API hash, and phone number
#     api_id = 23741394
#     api_hash = 'ac7aff1d5698c4f832501d4852b31f0a'
#     phone_number = '+249 99 934 7606'

#     # Initialize the Telegram client
#     client = TelegramClient('session_name', api_id, api_hash)

#     # Start the client
#     await client.start(phone_number)

#     # Get the channel entity
#     channel = await client.get_entity('book_hope_com')

#     # Iterate through all the messages in the channel
#     async for message in client.iter_messages(channel):
#         # Check if the message contains a file
#         if message.media:
#             # Print the ID of the message
#             print(message.id)

#     # Stop the client
#     await client.disconnect()

# # Run the async function
# asyncio.run(get_all_ids())

import asyncio
from telethon.sync import TelegramClient


async def get_all_ids():
    # Replace the values below with your own API ID, API hash, and phone number
    api_id = 23741394
    api_hash = 'ac7aff1d5698c4f832501d4852b31f0a'
    phone_number = '+249 99 934 7606'

    # Initialize the Telegram client
    client = TelegramClient('session_name', api_id, api_hash)

    # Start the client
    await client.start(phone_number)

    # Get the channel entity
    channel = await client.get_entity('l_alnader2')
    # channel = await client.get_entity('book_hope_com')

    # Open a file to write the IDs
    with open('ids.txt', 'w') as file:
        # Iterate through all the messages in the channel
        async for message in client.iter_messages(channel):
            # Check if the message contains a file
            if message.media:
                # Write the ID to the file
                file.write(str(message.id) + '\n')

    # Stop the client
    await client.disconnect()

# Run the async function
asyncio.run(get_all_ids())


