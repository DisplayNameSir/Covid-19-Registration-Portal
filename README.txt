Name: Peter Thanh Nguyen
Course: EE 104
Institution: San Jose State University – College of Engineering
Date: 2/15/2023

Project Title: Lab 2 - Covid19 Registration Portal (Reminders/Alerts)

Project Description:
This program is made for nurses and users that work to provide vaccines for patients. When a patient is finished getting their
first vaccination shot, the user can input the patients personal information to register in the database wheter they recieved their shot
and to also recieve notifcations to their email and phone about their second vaccination date. The initial program is provided by Professor Christopher Pham.
All rights to the program belong to the professor and editing the program is part of our assignment for the course.

Video Execution Link:
https://www.youtube.com/watch?v=Ho5_tQbIzlo

IMPORTANT NOTES:
Users that wish to modify the program should test the program before modifying the program. The program is built to be implemented to a registered excel file.
The excel file is used as a database and has identified sections that is organized based on the registration form. Its highly advised that the user should only 
modify the additional fields and messages to clients as the yagmail and twilio features may be difficult to fix after it not working.

Installed Modules:
import yagmail
from tkinter import *
from openpyxl import *
from datetime import date, datetime, timedelta
import pandas as pd
import os
import smtplib, ssl
from twilio.rest import Client

How to install modules:
To install the modules needed for the program or verify that its installed, users will open their anaconda powershell and type the following commands
1. Open Anaconda Powershell Prompt
2. Type "pip install twilio"
3. Allow the powershell to install the module
4. Once its finished type "pip install yagmail"
5. Allow that module to finish downloading and the program should be ready to go!
6. If the program runs into any issues try updating spyder or restarting the IDE.

Instructions:
1.Ensure the correct modulus are installed in the powershell
2.Run the program
3.Click on “register” to make an account 
4.Exit Registration
5.Click on “login” and input your account details
6.Click okay to exit “successful login” popup
7.Input client details
	a.When inputting phone number ensure that the format is 10 digits with no spaces or dashes 
		i.Example:4086444882
	b.Follow the format specified on the right of the registration form
	c.List only common types of vaccine brands
	d.Enter the date in the correct format
		i.Example:2023-02-15
8. When the form is filled the form will clear and you will be asked to input the future date to confirm the second vaccination date
9. Verify if the email and text was successfully sent
10.User is free to stay logged in to register another client

References:
-https://www.twilio.com/docs/sms/quickstart/python
-https://pypi.org/project/yagmail/
-https://realpython.com/python-gui-tkinter/