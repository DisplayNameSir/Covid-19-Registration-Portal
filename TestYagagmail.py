#Make sure you pip install yagmail
import yagmail

from_address = 'edcockcutlet@gmail.com' #this is your own gmail account
app_password = 'avsmpxqrpuujunpz' # a token for gmail, this is the app password from Gmail Security
to_address = 'nguyenpeter8574@gmail.com'   #send test to another email or the same email is OK

subject = 'Yet another test'  #modify the subject line anyway you like
content = ['About what they say']  #you can have different email and attachment

with yagmail.SMTP(from_address, app_password) as yag:
    yag.send(to_address, subject, content)
    print('Sent email successfully')  #you can have different success message