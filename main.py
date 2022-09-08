import shutil
import my_skype_tools as skt
import tools as tool
import gmail_tools as gmail
from datetime import date

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.modify']

def send_pdf_to_skype(skype_id):
    path = "F:\kaly_mora\kaly_mora"
    today = date.today()
    file_name = "kaly_mora " + today.strftime("%d/%m/%y") + ".pdf"
    skt.send_file_skype(skype_id,path,file_name)

    # move file to ok
    shutil.move(path, "F:\kaly_mora\ok\Kaly mora " + "07_09_22")

if __name__=="__main__":
    data = tool.get_data()
    anais_id = data["jira_skype_ids"]["Anais"][1]
    marga = data["jira_skype_ids"]["Margarette"][1]
    print("getting pdf")
    gmail.download_kaly_mora()

    print("sending to skype")
    skt.send_msg_skype(marga, "Coucou")
    send_pdf_to_skype(marga)

    skt.send_msg_skype(anais_id, "Le Pdf a bien été envoyé a Margarette")