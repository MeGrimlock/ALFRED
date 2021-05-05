from classes.email_trigger import Email_Trigger
from scripts.regularExpressions.classes.regex_token import Regex_RuleBook

ventana = 0
SenderName = "WALKER JOHNNIE"
SenderEmailAddress = ""
SentOn = ""
Subject = ""

# Still not implemented
To = ""
CC = ""
BCC = ""
Body = ""


# Create RuleBook
basicRuleBook = Regex_RuleBook("General Rules")

# Create EMAIL trigger that starts RPA agent
new_trigger = Email_Trigger(
    SenderName, SenderEmailAddress, SentOn, To, CC, BCC, Subject, Body
)

# Process Email Search with new_trigger parameters.
messages = new_trigger.searchEmails(ventana)

# Show search results
# new_trigger.printEmailSearch(messages)

# Custom process for each Message (in this example, we TAG emails using the General Rules for text analysis both subject and Body)
print("Custom EMAIL Automation: ")
for msg in messages:
    new_trigger.printEmailBrief(msg)
    tags = new_trigger.tagEmail(msg, basicRuleBook.getDict())
    print(tags)
    print("----------")
