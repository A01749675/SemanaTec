from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import aspose.words as aw
import smtplib
import mammoth

def send_mail(text):
    sender ='caikfure47@gmail.com'
    receiver = "iker.fuentesreyes@gmail.com"
    password ='wrwgfkaulfdkgveq'
    mensaje = MIMEMultipart("plain")
    mensaje["From"]=sender
    mensaje["To"]=receiver
    mensaje["Subject"]="¡Compra realizada!"
    adjunto = MIMEBase(text,"plain")
    mensaje.attach(adjunto)
    smtp =smtplib.SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login(sender,password)
    smtp.sendmail(sender,receiver,mensaje.as_string().encode("utf-8"))
    smtp.quit()