from classes.email_trigger import Email_Trigger
from scripts.regularExpressions.classes.regex_token import Regex_RuleBook

ventana = 0
SenderName = ""
SenderEmailAddress = ""
SentOn = ""
To = ""
CC = ""
BCC = ""
Subject = ""
Body = ""


# Create RuleBook
basicRuleBook = Regex_RuleBook("General Rules")

new_trigger = Email_Trigger(
    SenderName, SenderEmailAddress, SentOn, To, CC, BCC, Subject, Body
)

messages = new_trigger.searchEmails(ventana)
new_trigger.printEmailSearch(messages, basicRuleBook.getDict())