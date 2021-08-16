import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html = Template(Path('index.html').read_text())
email=EmailMessage()
email['from']='Animesh Srivastava'
email['to']='shaguntiwari0611@gmail.com'
email['subject']='You are the greatest person in the world'
email.set_content(html.substitute({'name':'Boobooooo'}),'html')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('shaguntiwari017@gmail.com', 'Shagun@2709')
    smtp.send_message(email)
    print('Sent!')
#DOES NOT WORK BCOZ GOOGLE CLOSES THE ID