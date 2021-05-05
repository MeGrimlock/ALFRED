# This test shows how to:
#
#
# 1) create an email trigger
# 2) process each email and get extract info.
# 3) Using the extracted info, perform a "sub-search"
# 4) For elements that match the previous criteria, print some attributes and tag using REGEX MODULE
#
#
# Optimization is still pending... but right now whats important is that the concept works
#

from classes.email_trigger import Email_Trigger
from scripts.regularExpressions.classes.regex_token import Regex_RuleBook

ventana = 0

SenderEmailAddress = "ClientesDatos@TEST.COM"
Subject = "CambioEstadoClientesDatos"
Body = ""

SenderName = ""
SentOn = ""
To = ""
CC = ""
BCC = ""

sample_text = "El caso del cliente ::: id3820:reduccion: Me Grimlock Rulz ::: ha cambiado a estado COMERCIAL-4. Este aviso ha sido enviado a integrantes del grupo COMERCIAL."


def getTicketElements(text):
    elements = new_trigger.splitText(text, ":")
    elements = [x.strip(" ") for x in elements]
    id = elements[3].replace("id", "")
    tipo = elements[4]
    cliente = elements[5]
    estado = str(elements[8]).replace(" ha cambiado a estado ", "")
    estado = str(estado).replace(
        "\r\nEste aviso ha sido enviado a integrantes del grupo ", ""
    )
    estado = estado.split(".")
    grupo = estado[1]
    estado = estado[0]
    return [id, tipo, cliente, estado, grupo]


# 1) Create RuleBook
basicRuleBook = Regex_RuleBook("General Rules")

# 2) create the rule for analyzing INBOX emails.
new_trigger = Email_Trigger(
    SenderName, SenderEmailAddress, SentOn, To, CC, BCC, Subject, Body
)

# 3) Get emails that match creteria within a fiven time window
messages = new_trigger.searchEmails(ventana)

# 4) Process Messages, in this example... we search for all items in inbox containing ticket related data.

for message in messages:
    elements = getTicketElements(message.Body)
    print("-----------------------Ticket Data:----------------------")
    print(elements)
    filter_regex = elements[0] + "|" + elements[2]

    # Find messages related to the trigger.email
    sub_messages = new_trigger.advancedBodySearch(filter_regex)

    # Process them (TAG and PRINT)
    for sub_m in sub_messages:
        msg = new_trigger.getEmailByID(sub_m)
        new_trigger.printEmailBrief(msg)
        tags = new_trigger.tagEmail(msg, basicRuleBook.getDict())
        # Print tags
        print(tags)
        print("----------")
