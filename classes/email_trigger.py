# Defines the email type to be shared among all other modules. This way ALFRED can always read an email no matter the origin.
# EMAIL TRIGGER CLASS
#   - This is the core of the system.
#   - Calls both Email and Analyze Email scripts.
#   - Has access to all email operations

import scripts.Email.outlook as myInbox
import scripts.Email.analyzeEmails as emailAnalysis

import time


class Email_Trigger:
    "Common base class for all email base analysis"
    inbox = None

    def __init__(
        self, SenderName, SenderEmailAddress, SentOn, To, CC, BCC, Subject, Body
    ):
        """Creates a NEW Email Object for the query
        Keywords:
            self, SenderName, SenderEmailAddress, SentOn, To, CC, BCC, Subject, Body"""

        self.SenderName = SenderName
        self.SenderEmailAddress = SenderEmailAddress
        self.SentOn = SentOn
        self.To = To
        self.CC = CC
        self.BCC = BCC
        self.Subject = Subject
        self.Body = Body

        myInbox.init()

    def searchEmails(self, ventana):
        print("Checking for new emails...")
        messages = myInbox.getMessagesFromInbox(
            self.SenderName,
            self.SenderEmailAddress,
            self.SentOn,
            self.Subject,
            ventana,
        )
        print("Emails extracted:    ")
        print(str(myInbox.Email.emailCount))
        return messages

    def advancedSubjectSearch(self, Subject):
        print("\tChecking for new emails...ADV-SUBJECT")
        messages = emailAnalysis.advancedSubjectSearch(Subject, myInbox.raw_subjectList)
        print("\tEmails extracted:    ")
        print(len(messages))
        return messages

    def advancedBodySearch(self, Regex):
        print("\tChecking for new emails...ADV-BODY")
        messages = emailAnalysis.advancedBodySearch(Regex, myInbox.raw_bodyList)
        print("\tEmails extracted:    ")
        print(len(messages))
        return messages

    def getEmailByID(self, id):
        message = myInbox.getEmailByID(id)
        return message

    def printEmailSearch(self, messages):
        print("-----------------------------------------")
        for temp_email in messages:
            print(temp_email.SenderName)
            print(temp_email.Subject)
            # print(temp_email.Body)
            print("-----------------------------------------")

    def tagEmail(self, message, rulebook):
        return emailAnalysis.classifyEmail(message.Body, message.Subject, rulebook)

    def showTagMatch(self, message, regex):
        return emailAnalysis.showMatches(message, regex)

    def splitText(self, text, limiter):
        return emailAnalysis.splitText(text, limiter)

    def sendEmail(self, To, Subject, Body, attachment_path=None):
        return myInbox.sendEmail(To, Subject, Body, attachment_path)

    def printEmailBrief(self, message):
        return myInbox.printMessageBrief(message)


# --------------------------------------------------------------------
