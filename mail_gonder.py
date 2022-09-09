import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def mail(email,mesajbody):
    try:
        mail = smtplib.SMTP("smtp.gmail.com", 587)
        mail.ehlo()
        mail.starttls()

        # gmail kullanıcı adımı ve şifremi giriyorum.
        mail.login("merterbirproje@gmail.com", "blabla")

        mesaj = MIMEMultipart()

        mesaj["From"] = " merterbirproje@gmail.com"  # Gönderen kişi
        mesaj["To"] = email  # Alıcı

        mesaj["Subject"] = "Uygunitem.com - Takip ettiğiniz bir ürünün fiyatı düştü!"  # Konu

        body = mesajbody

        body_text = MIMEText(body, "plain")
        mesaj.attach(body_text)

        mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())


    except:
        print("Mail gönderimi yapılırken bir hata yaşandı.")