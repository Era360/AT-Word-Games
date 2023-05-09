import random
from num2words import num2words
import africastalking
import time
import os
from dotenv import load_dotenv

load_dotenv()

math_attemps = 0
ran = 0


def random_number(start, end):
    ran = random.randint(1, 100)

    Number_in_Words = str(num2words(ran))
    # print(ran)
    return {"Words": Number_in_Words.replace("-", " "), "Number": ran}


wordsnumber = random_number(1, 100)

words = wordsnumber["Words"]
number = wordsnumber["Number"]


class SMS:
    def __init__(self):
        # Set your app credentials

        # Initialize the SDK
        africastalking.initialize(
            os.getenv("AT_USERNAME"), os.getenv("AT_API_KEY"))

        # Get the SMS service
        self.sms = africastalking.SMS

    def send(self):
        # Set the numbers you want to send to in international format
        recipients = [os.getenv("TEST_NUMBER")]

        # Set your message
        message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"

        # Set your shortCode or senderId
        sender = os.getenv("SENDER_ID")

        # Uncomment here
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(number, recipients, sender)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))


if __name__ == '__main__':
    SMS().send()
print(number)

'''
def num():
    randomnumber = random_number(1, 100)
    print(randomnumber)
    dogoinput = input("Enter number dogo: ")

    if dogoinput == randomnumber:
        print("Umepatia dogo")
        
    elif dogoinput != randomnumber:
        print("Unafel wp dogo")

num()


'''

# from chatgpt.gpt35 import chatgpt35


class SMS:
    def __init__(self):
        africastalking.initialize(
            os.getenv("AT_USERNAME"), os.getenv("AT_API_KEY"))

        self.sms = africastalking.SMS

    def fetch_sms_sync(self):
        last_msg = "let-this-be-like-this-ever"
        response = self.sms.send(wordsnumber["Number"], [
                                 str(os.getenv("TEST_NUMBER"))], os.getenv("SENDER_ID"))

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
                    # We got u covered

                    for message in messages:
                        frominbox = str(message["text"]).replace(
                            "THEGAME ", "")
                        tophone = message["from"]

                        last_received_id = int(message['id'])
                    print(frominbox)
                    if wordsnumber["Words"] == frominbox:
                        response = self.sms.send(
                            "Congrats", [str(os.getenv("TEST_NUMBER"))], os.getenv("SENDER_ID"))
                        break

                    elif wordsnumber["Words"] != frominbox:

                        response = self.sms.send(
                            "Failed", [str(os.getenv("TEST_NUMBER"))], os.getenv("SENDER_ID"))
                        break

                    time.sleep(5)

            except Exception as e:
                print('Encountered an error while fetching: %s' % str(e))


if __name__ == '__main__':
    SMS().fetch_sms_sync()

'''
def Hesabu():
    ops = ['-', '+', '/', '*']
    globalop = ''
    randomop = random.randint(1, 3)
    op = ops[randomop]
    rval = random.randint(1, 10)
    lval = random.randint(1, 10)
    if op == '-':
        result = rval - lval
    elif op == '+':
        result = rval + lval
    elif op == '/':
        result = rval / lval
    elif op == '*':
        result = rval * lval
  
    
    print("What is ")
    print(str(rval) +" "+ op +" "+ "[]" + " = " +str(result))
    userinput = input("Enter missing number: ")
    if lval == int(userinput):
        print("Umepatia")
    elif lval != int(userinput):
        print("Umekosa")
    
Hesabu()  

'''
# works with both python 2 and 3
