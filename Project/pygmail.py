import smtplib

def sendEmail( mailto, doctor, date, time, name, report ):
    gmailaddress = "EMAIL_ID"
    gmailpassword = "PASSWORD"
    
    sub = "Confirmed: Doctor Appointment Booked"
    if (len(report) == 0): report = "Checkup"
    msag = "Hey " + name + ",\n\nYour Appointment has been Successfully Booked with Dr." + doctor + "\n\nDate : " + date + "\nTime : " + time + "\nProblem : " + report + "\n\nThank you for using Doctor Chatbot."
    msg = 'Subject: {}\n\n{}'.format(sub, msag)
    
    sub2 = "Appointment Booked with Doctor "+ doctor + " on "+ date
    msag2 = "Patient Email: "+ mailto + "\n\nReport: " + report
    msg2 = 'Subject: {}\n\n{}'.format(sub2, msag2)
    
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , msg)
    print("--------------------\nUser Email Sent!\n--------------------")
    mailServer.sendmail(gmailaddress, gmailaddress , msg2)
    print("\n--------------------\nAdmin Email Sent!\n--------------------")
    mailServer.quit()
    return

# Turn ON/OFF
# https://myaccount.google.com/lesssecureapps
# Check Spam Folder if message not delivered
