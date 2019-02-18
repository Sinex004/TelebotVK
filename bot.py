import requests
import misc
from time import sleep
#import json
token = misc.token
#https://api.telegram.org/bot714693425:AAEBg1WxHKJZXwS8roORspGIq56U_s4Y6E4/sendmessage?chat_id=335812792&text=Hello
URL = 'https://api.telegram.org/bot' + token + '/'


global last_update_id
last_update_id = 0


def get_updates():
    # Take last updates(chats) and return it
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()

def get_message():
    #function take data from chats, and return last messaage of user
    data = get_updates()
    #take last update
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    '''
    сompare previous message and this last message
    if last message is different , then return parameters of message
    else -->  return None
    '''
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id

        '''
        get variables chat_id and text from json object from telegram
        '''
        chat_id = last_object['message']['chat']['id'] 
        message_text = last_object['message']['text']

        # creating a dictionary called message, which include important variables of last message in telegram
        message = {'chat_id':chat_id,
                   'text': message_text}
        return message
    return None

def send_message(chat_id, text='I did not understand you'):
    # fuction for sending message. if we dont give variable text, by default it will be <I did not understand you>

    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)

                 
def main():
    #d = get_updates()

    #with open('updates.json','w') as file:
    #    json.dump(d, file, indent=2, ensure_ascii=False)
    while True:
        answer = get_message()
        # check that message exists
        if answer != None:
            # take important variables of message
            chat_id = answer['chat_id']
            text = answer['text']

            # check what the user wrote
            if text == 'да':
                send_message(chat_id,'чем вам помочь?')
            else:
                send_message(chat_id)
        # if there is not any new message, then just contiune
        else:
            continue
        sleep(1)

if __name__ == '__main__':
    main()
