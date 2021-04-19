import scripts.Email.outlook as myInbox
import scripts.FileHandling.csvOperations as emailCSV
import scripts.regularExpressions.analyzeEmails as emailAnalysis

import time

myInbox.init()

minutos = 20  # Delay entre revisiones

sender = ""

print("Checking for new emails...")
messages = myInbox.getMessagesFromOutlook()
print("Emails extracted:    ")
print("-----------------------------------------")
# for temp_email in myInbox.parsed_emails:
#     print(temp_email.Body)
#     print(emailAnalysis.analyzeString(temp_email.Body))
#     print("-----------------------------------------")

temp_email = myInbox.parsed_emails[100]
print(temp_email.Body)
print(emailAnalysis.analyzeString(temp_email.Body))
print("-----------------------------------------")

print(str(myInbox.Email.emailCount))

# --------------------------------------------------------------------
