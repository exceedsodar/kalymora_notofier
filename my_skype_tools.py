from http.client import HTTPSConnection
from base64 import b64encode
import skpy
import time
from datetime import date, timedelta
import tools as tool
from retry import retry

# # ch_group = sk.chats.chat("19:ffd117e2bcb74a259c0c06049545908e@thread.skype") # DIR SYN RESTREINT

data = tool.get_data()
# Credentials
skype_user = data.get("sk_user")
skype_pwd = data.get("sk_pwd")

sk = skpy.Skype(skype_user, skype_pwd)
# Dates management
today = date.today()
yesterday = today - timedelta(days=1)
period = today.strftime("%m%y")
yesterday_th_tag = yesterday.strftime("%d/%m/%y")

@retry(delay=5, tries=5)
def send_msg_skype(skype_id,msg,rich=False):
    try:
        sk = skpy.Skype(skype_user, skype_pwd)  # connect to Skype

        # sk.user  # you
        # sk.contacts  # your contacts
        # sk.chats  # your conversations
        contact = sk.contacts[skype_id].chat  # 1-to-1 conversation

        print("sending msg")
        contact.sendMsg(msg,rich)  # plain-text message
    except Exception as e:
        print("Error!. retring")
        raise

def send_msg_grp_skype(skype_id,msg,rich=False):

    sk = skpy.Skype(skype_user, skype_pwd)  # connect to Skype

    # sk.user  # you
    # sk.contacts  # your contacts
    # sk.chats  # your conversations
    contact = sk.chats[skype_id]  # 1-to-1 conversation

    print("sending msg")
    contact.sendMsg(msg,rich)  # plain-text message

def send_file_skype(skype_id,path,file_name):

    sk = skpy.Skype(skype_user, skype_pwd)  # connect to Skype
    contact = sk.contacts[skype_id].chat  # 1-to-1 conversation
    print("sending file")
    print(path)
    print(file_name)
    contact.sendFile(open(path, "rb"), file_name)


def print_recent():
    for id in sk.chats.recent():
        print(id)

def send_rappel(skype_id):
    if tool.is_weekend():
      return  False

    sk = skpy.Skype(skype_user, skype_pwd)  # connect to Skype

    # sk.user  # you
    # sk.contacts  # your contacts
    # sk.chats  # your conversations
    contact = sk.chats[skype_id]  # 1-to-1 conversation

    msg = 'Hello <at id="*">all</at>. Rappel kely so dia nisy nanadino commande :D'
    print(msg)
    contact.sendMsg(msg,rich=True)  # plain-text message


if __name__ == "__main__":
    data = tool.get_data()
    kaly_mora_id = data["jira_skype_ids"]["KayMora"][1]

    send_rappel(kaly_mora_id)