# To get all posts in your channel in Telegram using Python, you can use the Telethon library. 
# Here's an example code that will fetch all posts from a channel:
from telethon import TelegramClient

# Replace the values below with your own API ID, API hash, and phone number
api_id = 23741394
api_hash = 'ac7aff1d5698c4f832501d4852b31f0a'
phone_number = '+249 99 934 7606'


# Initialize the Telegram client
client = TelegramClient('session_name', api_id, api_hash)

# Start the client
client.start(phone_number)

# Get the channel entity
channel = client.get_entity('L_alnader14')
# channel = client.get_entity('book_hope_com')

# Get all posts in the channel
posts = client.get_messages(channel, limit=None)

# Print the posts
for post in posts:
    print(post.text)
