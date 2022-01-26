import smtplib
import getpass

#email port
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()  
smtp_object.starttls()

#logowanie do maila
email = getpass.getpass('username/mail: ')
haslo = getpass.getpass('password: ')
smtp_object.login(email,haslo)

from_adress = email
to_adress = 'm.galazynn@gmail.com'
subject = 'BITCOIN' 
message = 'Cena bitcoina spadła o 10%'

msg = subject + '\n' + message

smtp_object.sendmail(from_adress,to_adress,msg)
smtp_object.quit()
