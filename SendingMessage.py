import time
import pywhatkit
import ReadExcel
import NumberProcessing, MessagesByCountry
import ErrorCatch

close_time = 10

MessageToSending = ""

def SendMessage(listOfNumbers):
    for PhoneNumber in listOfNumbers:
        NumberProcessing.NumberProcessing(PhoneNumber)
        time.sleep(3)
        MessageToSending = MessagesByCountry.MessageToSend
        if  MessageToSending != "":
            pywhatkit.sendwhatmsg_instantly(PhoneNumber, MessageToSending,close_time,True,10)
            print("Enviando Mensaje a: " + PhoneNumber)
        else:
           NumberProcessing.Errors.append("No se pudo enviar el mensaje a: " + PhoneNumber) 
        time.sleep(5)
    ErrorCatch.ErrorCatched(NumberProcessing.Errors)
    
SendMessage(ReadExcel.NumbersData)