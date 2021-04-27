# Defines the email type to be shared among all other modules. This way ALFRED can always read an email no matter the origin.
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
            self.SenderEmailAddress, self.Subject, ventana
        )
        print("Emails extracted:    ")
        print(str(myInbox.Email.emailCount))
        return messages

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


# --------------------------------------------------------------------
