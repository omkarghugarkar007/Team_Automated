#
# def save_pass_to_file(dic):
#     f = open('r.txt', 'w')
#     f.write(str(dic))
#     f.close()
#
#
# def load_pass_from_file():
#     f = open('r.txt', 'r')
#     data = f.read()
#     f.close()
#     return data
#
# save_pass_to_file("text")
# password=load_pass_from_file()
# if lil=="text":
#     print(453)

# import smtplib
# from email.message import EmailMessage
# import datetime
# server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
# msg=EmailMessage()
# contacts=['bhuvanaggarwal9@gmail.com']
# msg['Subject']="Password Change Detected!!"
# msg['From']="team.automatediitb@gmail.com"
# msg['To']=contacts
# #msg.set_content('The password was changed')
# msg.add_alternative(f"""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray; font-style:"bold"; font-family:"Comic Sans MS", cursive, sans-serif;"> {datetime.datetime.now()} is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')
#
# server.login("team.automatediitb@gmail.com", "SASHAsasha")
# server.send_message(msg)
# server.quit()
#

import random


test_list = ["lol", "dsf", "sdsdg ", "dsfsdf", "sdfdsf", "sdfddsfsdfsdfdsf", "dsfsdffdsdf"]


while True:# printing random number
    random_num = random.choice(test_list)
    print(random_num)
