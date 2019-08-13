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
    session_name='544dfsdfdhg-4ui-s_htypy_channel'
    #hardcode channel id
    channel_id=0
    try:
        # tg client start
        # same session would lock the database, nothing can do if this session is in process
        client = TelegramClient(session_name, api_id, api_hash)
        client.start()
    except Exception as e:
        print(str(e))
    else:

        try:
            users=[]
            mychannel=client.get_entity(PeerChannel(channel_id))
            start=True
            total=0
            offset=0
            while start == True or total > 0:
                channel_members=client(functions.channels.GetParticipantsRequest(
                    channel=mychannel,
                    filter=types.ChannelParticipantsSearch(''),
                    offset=offset,
                    limit=200,
                    hash=0
                ))
                offset += 200
                start=False
                total=len(channel_members.participants)
                users=[]
                if len(channel_members.participants) > 0:
                    for member in channel_members.participants:
                        if member.__class__.__name__ != 'ChannelParticipantSelf':
                            #print(member)
                            #print(member.user_id)
                            users.append(member.user_id)
                
                    all_users=client(functions.users.GetUsersRequest(
                        id=users
                    )) 
                    for user in all_users:
                        print(user.stringify())
        except Exception as e:
            client.disconnect()
            print(str(e))
        else:
         
            client.disconnect()
            
tg()
