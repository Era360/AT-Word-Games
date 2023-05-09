import africastalking
import time
import os
from dotenv import load_dotenv

load_dotenv()


class SMS:
    def __init__(self):

        africastalking.initialize(
            os.getenv("AT_USERNAME"), os.getenv("AT_API_KEY"))
        self.sms = africastalking.SMS

    def fetch_sms_sync(self):
        last_msg = "let-this-be-like-this-ever"
        while (True):
            print("Here we go... start")

            try:
                last_received_id = 0

                while True:
                    MessageData = self.sms.fetch_messages(last_received_id)

                    messages = MessageData['SMSMessageData']['Messages']
                    if len(messages) == 0:
                        print('No sms messages in your inbox.')
                        break
                    '''You don't need to worry we will take the last message from inbox'''
                    # We got u covered
                    for message in messages:
                        tochatgpt = str(message["text"]).replace(
                            "THEGAME ", "")
                        tophone = message["from"]

                        last_received_id = int(message['id'])
                    print(tochatgpt)
                    if last_msg == tochatgpt:
                        print("Do not send, and sleeping")

                    elif last_msg != tochatgpt:
                        # response = self.sms.send("Test", [str("255693338637")] , "15054")
                        last_msg = tochatgpt
                        print("Send now, and sleeping")
                        time.sleep(2)

            except Exception as e:
                print('Encountered an error while fetching: %s' % str(e))


if __name__ == '__main__':
    SMS().fetch_sms_sync()
