import smtplib

#message = smtplib.SMTP(host_pi='', port='', local_hostname='')

#message.sendmail(sender, receiver, msge)

# example of mail send using smtplip module in python
   
sender_mail = 'haron.murumba22@gmail.com'    
receivers_mail = ['haronmurrumba23@gmail.com']    
message = """From: From Person %s  
To: To Person %s  
Subject: Sending SMTP e-mail   
This is a test e-mail message.  
"""%(sender_mail,receivers_mail)    
try:    
   smtpObj = smtplib.SMTP('localhost')    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")  



   # send html mail using smtp
sender_mail = 'sender@fromdomain.com'    
receivers_mail = ['reciever@todomain.com']    
message = """From: From Person %s  
To: To Person %s  
  
MIME-Version:1.0  
Content-type:text/html  
  
  
Subject: Sending SMTP e-mail   
  
<h3>Python SMTP</h3>  
<strong>This is a test e-mail message.</strong>  
"""%(sender_mail,receivers_mail)    
try:    
   smtpObj = smtplib.SMTP('localhost')    
   smtpObj.sendmail(sender_mail, receivers_mail, message)    
   print("Successfully sent email")    
except Exception:    
   print("Error: unable to send email")    
 
