import shutil
import my_skype_tools as skt
import tools as tool
import gmail_tools as gmail

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly','https://www.googleapis.com/auth/gmail.modify']

def send_pdf_to_skype(skype_id):
    path = "F:\kaly_mora\Kaly mora " + "07_09_22"
    file_name = "kaly_mora " + "today" + ".pdf"
    skt.send_file_skype(skype_id,path,file_name)

    # move file to ok
    shutil.move(path, "F:\kaly_mora\ok\Kaly mora " + "07_09_22")

if __name__=="__main__":
    # data = get_data()
    # print(data)
    # print_labels()

    # get_last_pdf()
    # send_pdf_to_skype()

    data = tool.get_data()
    anais_id = data["jira_skype_ids"]["Anais"][1]

    # send_pdf_to_skype(anais_id)
    gmail.print_labels()