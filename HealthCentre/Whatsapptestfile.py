from WPP_Whatsapp import Create
from django.conf import settings
import time
from concurrent import futures
# from playwright._impl import _api_types 
# if __name__ == '__main__':
    # from .views import catchgenqr
# import psutil

# genqr = ""

    # openWhatsapp()


def catchqr(qrCode: str , asciiQR: str , attempt: int, urlCode: str):
            """
            qrCode:"data:image/png;base64,",
            asciiQR:"",
            attempt:1,
            urlCode:"2@242",
            """
            
            getqr = asciiQR
            print(getqr)
            
            # global genqr
            genqr =qrCode
            # test = testqr()
            # print(test)
            # print(asciiQR)
            # print(attempt)
            # print(urlCode)

creator = ""
client = ""
# wpIsConnected = False
class openWhatsapp():
        # start client with your session name
     
    def wp(DocName):
        from .views import catchgenqr
        your_session_name = DocName #"test"
        global creator
        creator = Create(session=your_session_name, catchQR= catchgenqr , logQR= True) #catchgenqr
        settings.GLOBAL_VAR = creator
        settings.WP_IS_CONNECTED = False
        global client
        try:
            client = creator.start()
            if client.waitForLogin():
                time.sleep(10) 
        except futures._base.TimeoutError():
            time.sleep(7)
            client.close()
    # Now scan Whatsapp Qrcode in browser
    # check state of login
        if creator.state != 'CONNECTED':
        
            raise Exception(creator.state)
        if creator.state == 'CONNECTED' and (creator.session == DocName):
            
            # request.session['wpStatus'] = True
            settings.WP_IS_CONNECTED = True
        # return client
        time.sleep(5)
        # try:
        client.close()
        # except _api_types.Error:
        #     time.sleep(5)
        #     client.close()

def whatsappApi(patientName, doctorName, whatsappNumber, time_, date, clinicName):
    # reclient= openWhatsapp.client
    from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"APPOINTMENT REMINDER: Dear {patientName}, This is Dr.{doctorName}, from {clinicName}. You have an appointment in three hours. Your Appointment is fixed at {time_} on {date}."
    # global client
    # result = client.sendText(phone_number, message)
    Sesscreator = Create(session=doctorName, catchQR= catchgenqr, logQR= True)
    sess = Sesscreator.session
    global client
    try:
        sessStart = Sesscreator.start()
        if sessStart.waitForLogin():
            time.sleep(10)
    except futures._base.TimeoutError():
        result = sessStart.sendText(phone_number, message)
        sessStart.close()    
    dumSess = sessStart.session
    result = sessStart.sendText(phone_number, message)
    time.sleep(5)
    # try:
    sessStart.close()
    # except _api_types.Error or futures._base.TimeoutError():
    #     time.sleep(5)
    #     pass
        # sessStart.close()
        
def whatsappApiDoc(doctorName, whatsappNumber, time_, date):
    from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"APPOINTMENT REMINDER: Dear {doctorName}, You have an appointment in three hours, fixed at {time_} on {date}. Thanks!!"
    # global client
    # # Simple message
    # result = client.sendText(phone_number, message)
    Sesscreator = Create(session=doctorName, catchQR= catchgenqr, logQR= True)
    sess = Sesscreator.session
    global client
    try:
        sessStart = Sesscreator.start()
        if sessStart.waitForLogin():
            time.sleep(10)
    except futures._base.TimeoutError():
        result = sessStart.sendText(phone_number, message)
        sessStart.close()
    dumSess = sessStart.session
    result = sessStart.sendText(phone_number, message)
    time.sleep(5)
    # try:
    sessStart.close()
    # except _api_types.Error:
    #     time.sleep(5)
    #     pass
        # sessStart.close()
    
def whatsappApiEdit(patientName, doctorName, whatsappNumber, time_, date, clinicName):
    # reclient= openWhatsapp.client
    from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}" #phone_number = "+917904427507"  # or "+201016708170"
    message = f"Dear {patientName}, This is Dr.{doctorName}, from {clinicName}. Your Appointment has been changed to {time_} on {date}."
    global creator
    Sesscreator = Create(session=doctorName, catchQR= catchgenqr, logQR= True)
    sess = Sesscreator.session
    global client
    # try:
    sessStart = Sesscreator.start()
    print("starting whatsapp session...")
    if sessStart.waitForLogin():
        print("waiting for whatsapp session login...")
        time.sleep(10)
        print("browser must be open...")
    # except futures._base.TimeoutError():
        # result = sessStart.sendText(phone_number, message)
        # sessStart.close()
    result = sessStart.sendText(phone_number, message)
    print("text message sent...")
    time.sleep(5)
    # try:
    sessStart.close()
    # except _api_types.Error:
    #     time.sleep(5)
    #     # sessStart.close()
    #     pass
    
def whatsappMedia(whatsappNumber, pdfPathForWP, docName, patientName, prescDate):
    from .views import catchgenqr
    phone_number = f"+91{whatsappNumber}"
    path = pdfPathForWP
    name = patientName
    caption = prescDate
    global client
    Sesscreator = Create(session=docName, catchQR= catchgenqr, logQR= True)
    sess = Sesscreator.session
    global client
    try:
        sessStart = Sesscreator.start()
        if sessStart.waitForLogin():
            time.sleep(25)
    except futures._base.TimeoutError():
        result = sessStart.sendFile(phone_number, path, name, caption )
        sessStart.close()    
    dumSess = sessStart.session
    result = sessStart.sendFile(phone_number, path, name, caption )
    time.sleep(5)
    # try:
    sessStart.close()
    # except _api_types.Error:
    #     time.sleep(5)
    #     # sessStart.close()
    #     pass
    # message = openWhatsapp.client.sendMessageOptions()


    # # for pc in psutil.process_iter():
    # #     try:
    # #         print(pc.cmdline())
    # #     except psutil.AccessDenied:
    # #         continue
        
    # # start client with your session name
    # your_session_name = "test"
    # # check_open_directory = False
    # creator = Create(session=your_session_name, check_open_directory = False )
    # # client = creator.start()
    # client = creator.start()
    # # Now scan Whatsapp Qrcode in browser

    # # check state of login
    # if creator.state != 'CONNECTED':
    #     raise Exception(creator.state)

    # phone_number = whatsappNumber # or "+201016708170"
    # message = '''Hello From WPP WhatsApp Test Code !
    # A reminder from Dr Nandha kumar Dental clinic. Your Appointment has been fixed on 12 July 23 at 6pm and Don't forget your prescription!! '''

    # # Simple message
    # result = client.sendText(phone_number, message)
    # chrome_process = psutil.Process(1300)
    # info = chrome_process.info()
    # print(info)