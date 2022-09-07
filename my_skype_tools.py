from http.client import HTTPSConnection
from base64 import b64encode
import skpy
import time
from datetime import date, timedelta
import tools as tool

# # ch_group = sk.chats.chat("19:ffd117e2bcb74a259c0c06049545908e@thread.skype") # DIR SYN RESTREINT

data = tool.get_data()
# Credentials
skype_user = data.get("user")
skype_pwd = data.get("pwd")

# Dates management
today = date.today()
yesterday = today - timedelta(days=1)
period = today.strftime("%m%y")
yesterday_th_tag = yesterday.strftime("%d%m")

def send_msg_skype(skype_id,msg):

    sk = skpy.Skype(skype_user, skype_pwd)  # connect to Skype

    # sk.user  # you
    # sk.contacts  # your contacts
    # sk.chats  # your conversations
    contact = sk.contacts[skype_id].chat  # 1-to-1 conversation

    print("sending msg")
    contact.sendMsg(msg)  # plain-text message


def send_file_skype(skype_id,path,file_name):

    sk = skpy.Skype(skype_user, skype_pwd)  # connect to Skype
    contact = sk.contacts[skype_id].chat  # 1-to-1 conversation
    print("sending file")
    contact.sendFile(open(path, "rb"), file_name)