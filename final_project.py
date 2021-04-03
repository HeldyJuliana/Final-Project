#!/usr/bin/env python
# coding: utf-8

# In[1]:


#sending to one specific email

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "pythonfortesting1@gmail.com"  # Enter your address
receiver_email = "heldyjuli@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


# In[5]:


#sending to list of emails

mails = open('receiver_list.txt','r+')
#mailList = mails.read()
#mailList = [i.strip() for i in mails.readlines()] 
directory = "cd/Users/SESA440895/basic-pyhton"

#Source: https://stackoverflow.com/questions/22120330/send-email-to-recipient-from-txt-in-python-3-3

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "pythonfortesting1@gmail.com"  # Enter your address
receiver_email = [i.strip() for i in mails.readlines()] 
print(receiver_email) # Enter receiver address
password = input("Type your password and press enter: ")
message = """Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    
#Source: https://realpython.com/python-send-email/


# In[ ]:





# In[ ]:




