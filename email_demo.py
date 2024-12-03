from email.message import EmailMessage
import ssl
import smtplib

email_sender='bkeerthana395@gmail.com'
e_password='bttp xtpu nnhn jcrf'

email_recevier='reddylakshana208@gmail.com'

body=" surprise big guda is waiting"
em=EmailMessage()
em['From']=email_sender
em['subject']="lakshana"
em['To']=email_recevier

em.set_content(body)

context=ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,e_password)
    smtp.sendmail(email_sender,email_recevier,em.as_string())
