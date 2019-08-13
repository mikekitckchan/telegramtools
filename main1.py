from telethon import TelegramClient, events, sync, functions, types
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, InputPeerEmpty
import datetime
import sys
import json 
import time

 
def tg():

    api_id = 0 # use app id of telegram account
    api_hash = '' # use app hash of your telegram account
    
    # please change your prefix of session name , and don,t send to anyone
    session_name='dfddf3435-s_htypy_channel'

    try:
        # tg client start
        # same session would lock the database, nothing can do if this session is in process
        client = TelegramClient(session_name, api_id, api_hash)
        client.start()
    except Exception as e:
        print(str(e))
    else:

        try:
            chats = []
            users = []
            all_participants = []
            result = client(functions.messages.GetDialogsRequest(
                 offset_date=datetime.datetime(2022, 12, 25),
                 offset_id=0,
                 offset_peer=InputPeerEmpty(),
                 limit=100,
                 hash = 0
            ))
            chats.extend(result.chats)
            for chat in chats:
                try:
                    if chat.megagroup == True:
                        print(chat.id)
                        print(chat.title) 
                        print('----------') 
                except:
                    continue

        except Exception as e:
            client.disconnect()
            print(str(e))
        else:
         
            client.disconnect()
            
tg()
