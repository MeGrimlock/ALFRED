# https://www.thepythoncode.com/article/reading-emails-in-python
# https://gist.github.com/robulouski/7441883
# https://medium.com/@yernagulahemanth/download-emails-from-gmail-using-python-31e9bc62e501
import settings
import scripts.Email.IMAP as myInbox
import scripts.FileHandling.csvOperations as emailCSV
import scripts.regularExpressions.analyzeEmails as emailAnalysis

import time

myInbox.init(
    settings.imap_url, settings.imap_port, settings.imap_email, settings.imap_psw
)

minutos = 20  # Delay entre revisiones

sender = ""

print("Checking for new emails...")
messages = myInbox.getMessagesFromInbox()
print("Emails extracted:    ")
print("-----------------------------------------")
# for temp_email in myInbox.parsed_emails:
#     print(temp_email.Body)
#     print(emailAnalysis.analyzeString(temp_email.Body))
#     print("-----------------------------------------")

temp_email = myInbox.parsed_emails[0]
print(temp_email.Subject)
print(temp_email.To)
# print(temp_email.SenderEmailAddress)
# print(temp_email.Body)
print(emailAnalysis.analyzeString(temp_email.Body))
print("-----------------------------------------")

print(str(myInbox.Email.emailCount))

# --------------------------------------------------------------------
