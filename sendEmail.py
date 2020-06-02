#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from smtplib import SMTP
def main():
    from_address = "emisor@correo.com.py"
    to_address = "receptor@correo.com.py"
    message = "Hello, world!"
    
    mime_message = MIMEText(message, "plain")
    mime_message["From"] = from_address
    mime_message["To"] = to_address
    mime_message["Subject"] = "Correo de prueba"
    
    smtp = SMTP("mail.correo.com.py:587")
    smtp.login(from_address, "password")
    
    smtp.sendmail(from_address, to_address, mime_message.as_string())
    smtp.quit()
if __name__ == "__main__":
    main()



'''

'''