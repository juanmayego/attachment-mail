import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
# Iniciamos los parametros del script
remitente = 'remitente@correo.com.py'
#destinatarios = ['destinatario_uno@correo.com', 'destinatario_dos@correo.com', 'destinatario_tres@correo.com']
destinatarios = ['destino@correo.com.py']
asunto = '[RPI] Correo de prueba 2'
cuerpo = 'Este es el contenido del mensaje'
ruta_adjunto = '/path/to/file/file.png'
nombre_adjunto = 'file.png'

# Creamos el objeto mensaje
mensaje = MIMEMultipart()
 
# Establecemos los atributos del mensaje
mensaje['From'] = remitente
mensaje['To'] = ", ".join(destinatarios)
mensaje['Subject'] = asunto
 
# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
mensaje.attach(MIMEText(cuerpo, 'plain'))
 
# Abrimos el archivo que vamos a adjuntar
archivo_adjunto = open(ruta_adjunto, 'rb')
 
# Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
adjunto_MIME.set_payload((archivo_adjunto).read())
# Codificamos el objeto en BASE64
encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
# Y finalmente lo agregamos al mensaje
mensaje.attach(adjunto_MIME)
 
# Creamos la conexion con el servidor
sesion_smtp = smtplib.SMTP('mail.correo.com.py', 587)
 
# Ciframos la conexion
sesion_smtp.starttls()

# Iniciamos sesion en el servidor
sesion_smtp.login('remitente@correo.com.py','password')

# Convertimos el objeto mensaje a texto
texto = mensaje.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatarios, texto)

# Cerramos la conexion
sesion_smtp.quit()
