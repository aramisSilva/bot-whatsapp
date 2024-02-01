import pywhatkit
from datetime import datetime

now = datetime.now()

actual_hour = now.strftime("%H")
celular = input('Enter Mobile No of Receiver : ')
mensagem = input('Enter Message you wanna send : ')
hora = int(input('Enter hour : '))
minutos = int(input('Enter minute : '))

pywhatkit.sendwhatmsg(celular,mensagem,hora,minutos)