import asyncio
from telethon.sync import TelegramClient


async def get_pdf_ids():
    # Replace the values below with your own API ID, API hash, and phone number
    api_id = 20688053
    api_hash = 'e95d0f75b6c68ede3415e8390d1248f0'
    phone_number = '+256744859083'

    # Initialize the Telegram client
    client = TelegramClient('session_name', api_id, api_hash)

    # Start the client
    await client.start(phone_number)

    # Get the channel entity
    channel = await client.get_entity('l_alnader2')
    # channel = await client.get_entity('book_hope_com')

    # Open a file to write the IDs
    with open('PDF_IDs.txt', 'w') as file:
        # Iterate through all the messages in the channel
        async for message in client.iter_messages(channel):
            # Check if the message contains a PDF file
            if message.media and message.media.document.mime_type == 'application/pdf':
                # Write the ID to the file
                file.write(str(message.id) + '\n')

    # Stop the client
    await client.disconnect()

# Run the async function
asyncio.run(get_pdf_ids())