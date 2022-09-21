# Python 3.8.0
import smtplib
import time
import imaplib
import email
import traceback
import tools as t


# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------

data = t.get_data()
ORG_EMAIL = data["user"]
FROM_EMAIL = ORG_EMAIL
FROM_PWD = data["pwd"]
SMTP_SERVER = "imap.mail.yahoo.com"
SMTP_PORT = 993

subject= "kaly mora"
outputdir = "F:/kaly_mora"

def connect(server=SMTP_SERVER, user=FROM_EMAIL, password=FROM_PWD):
    m = imaplib.IMAP4_SSL(server)
    m.login(user, password)
    m.select()
    return m

def read_email_from_gmail(self,payload={}):
    try:

        mail = connect()
        mail.select('inbox')

        data = mail.search(None, 'SUBJECT "kaly mora"')

        msgs = data[0].split()
        for emailid in msgs:
            downloaAttachmentsInEmail(m, emailid, outputdir)

        mail_ids = data[1]
        id_list = mail_ids[0].split()
        latest_email_id = int(id_list[-1])


        data = mail.fetch(str(latest_email_id), '(RFC822)' )

        for response_part in data:
            arr = response_part[0]
            if isinstance(arr, tuple):
                msg = email.message_from_string(str(arr[1],'utf-8'))
                email_subject = msg['subject']
                email_from = msg['from']
                print('From : ' + email_from + '\n')
                print('Subject : ' + email_subject + '\n')
                print(msg )

    except Exception as e:
        traceback.print_exc()
        print(str(e))

def downloaAttachmentsInEmail(m, emailid, outputdir):
    # resp, data = m.fetch(emailid, "(BODY.PEEK[])")
    resp, data = m.fetch(emailid, '(RFC822)')
    email_body = data[0][1]
    mail = email.message_from_bytes(email_body)
    if mail.get_content_maintype() != 'multipart':
        return
    for part in mail.walk():
        if part.get_content_maintype() != 'multipart' and part.get('Content-Disposition') is not None:
            open(outputdir + '/' + part.get_filename().replace("/","-"), 'wb').write(part.get_payload(decode=True))

#download attachments from all emails with a specified subject line
def downloadAttachments(subject=subject):
    m = connect()
    m.select("Inbox")
    typ, msgs = m.search(None, '(UNSEEN SUBJECT "' + subject + '")')

    msgs = msgs[0].split()
    if not msgs:
        print("NO msg FOUND!!")
        return False
    downloaAttachmentsInEmail(m, msgs[-1], outputdir)
    return True

if __name__ == "__main__":
    downloadAttachments()