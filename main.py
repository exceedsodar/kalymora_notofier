import shutil
import my_skype_tools as skt
import tools as tool
import imap as gmail
from datetime import date
from retry import retry

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.modify']

@retry(delay=5, tries=6)
def send_pdf_to_skype(skype_id):
    try:
        today = date.today()
        path = "F:\kaly_mora\Kaly mora "+ today.strftime("%d-%m-%y")
        file_name = "Kaly mora " + today.strftime("%d-%m-%y") + ".pdf"
        skt.send_file_skype(skype_id,path,file_name)

        # move file to ok
        shutil.move(path, "F:\kaly_mora\ok\Kaly mora " + "07_09_22")
    except Exception as e:
        print("error while sinding pdf. retrying")
        raise

if __name__=="__main__":
    if tool.is_weekend():
        print("c'est le week end")
        exit()

    data = tool.get_data()
    anais_id = data["jira_skype_ids"]["Anais"][1]
    marga = data["jira_skype_ids"]["Margarette"][1]
    print("getting pdf")
    gmail.downloadAttachments()

    print("sending to skype")
    try:
        skt.send_msg_skype(marga, "Coucouu")
        send_pdf_to_skype(marga)
        skt.send_msg_skype(anais_id, "Le Pdf a bien été envoyé a Margarette")
    except Exception as e:
        skt.send_msg_skype(anais_id, f"ERREUR lors de l'envoie  Pdf: {repr(e)}")