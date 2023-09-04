import asyncio
from telethon.sync import TelegramClient


async def get_pdf_links():
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

    # Open the file containing the IDs
    with open('ids1.txt', 'r') as file:
        # Open a new file to save the direct links
        with open('direct_links.txt', 'w') as links_file:
            # Iterate through each line in the file
            for line in file:
                message_id = int(line.strip())

                try:
                    # Get the message by its ID
                    message = await client.get_messages(channel, ids=message_id)

                    # Check if the message contains a PDF file
                    if message.media and hasattr(message.media, 'document') and message.media.document.mime_type == 'application/pdf':
                        # Save the direct link
                        direct_link = f"https://api.telegram.org/file/bot{api_id}:{api_hash}/{message.media.document.file_id}"
                        print(f"Direct link for PDF ID {message_id}: {direct_link}")
                        links_file.write(f"Direct link for PDF ID {message_id}: {direct_link}\n")

                except Exception as e:
                    print(f"Error retrieving message ID {message_id}: {e}")

    # Stop the client
    await client.disconnect()

# Run the async function
asyncio.run(get_pdf_links())
