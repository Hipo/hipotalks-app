from django.conf import settings
from slack import WebClient

def get_client(self, company):
    client = WebClient(token=settings.SLACK_BOT_TOKEN, timeout=30)
    return client


def send_message(self, users=None):
    client = self.get_client()
    usernames = ', '.join([user.username for user in users])
    message = f'@channel next week will be {usernames}'
    client.chat_postMessage(channel=settings.HIPOTALKS_SLACK_CHANNEL_ID, text=message)
