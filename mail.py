__author__ = 'rodolfopardo28' 
     
#!/usr/bin/python 
     
import smtplib 
from email.MIMEText import MIMEText 
     
emisor = "emisor@correo.com.py" 
receptor = "receptor@correo.com.py" 
   
  # Configuracion del mail 
mensaje = MIMEText("Este correo ha sido enviado desde Python") 
mensaje['From']=emisor 
mensaje['To']=receptor 
mensaje['Subject']="Python prueba 2" 
   
  # Nos conectamos al servidor SMTP de Gmail 
serverSMTP = smtplib.SMTP('mail.correo.com.py',587) 
serverSMTP.ehlo() 
serverSMTP.starttls() 
serverSMTP.ehlo() 
serverSMTP.login(emisor,"password") 
   
  # Enviamos el mensaje 
serverSMTP.sendmail(emisor,receptor,mensaje.as_string()) 
print("Correo enviado!")
  # Cerramos la conexion 
serverSMTP.close()