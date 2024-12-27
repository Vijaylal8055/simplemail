#Sending a simple email using Python
#smptlib -->simple mail transfer protocol
#Email OTP Authentication
import random
import math
import smtplib

#We will generate a 6 digit otp by taking base digits
digits ="0123456789"
OTP = "" #empty string

#now we will use math module along with module to
#generate a customized 6 digit otp
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
    #print(OTP)
otp = OTP+"is your OTP"
msg= otp
#include our email automation
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("vijaylalbussa@gmail.com","xnaf gvut pkpt tibl")
user="vijaylalbussa@gmail.com"
emailid=input("Enter the mail which you want to send OTP:")
s.sendmail(user,emailid,msg)
while True:
    a=input("Enter your OTP: ")
    if a==OTP:
        print("OTP correct")
    else:
        print("Failure wrong OTP")
