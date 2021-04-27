from classes.email_trigger import Email_Trigger
from scripts.regularExpressions.classes.regex_token import Regex_RuleBook

ventana = 0

SenderEmailAddress = ""
Subject = ""
Body = ""

SenderName = ""
SentOn = ""
To = ""
CC = ""
BCC = ""

sample_text = "El caso del cliente ::: id3820:reduccion:GG de la vida ::: ha cambiado a estado COMERCIAL-4. Este aviso ha sido enviado a integrantes del grupo COMERCIAL."


def getTicketElements(text):
    elements = new_trigger.splitText(text, ":")
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


# Create RuleBook
basicRuleBook = Regex_RuleBook("General Rules")

new_trigger = Email_Trigger(
    SenderName, SenderEmailAddress, SentOn, To, CC, BCC, Subject, Body
)

messages = new_trigger.searchEmails(ventana)

for message in messages:
    print(getTicketElements(message.Body))
# new_trigger.printEmailSearch(messages)


# ---------- Now lets customize the rulebook---------------------
# print("\n")
# basicRuleBook.clearRuleBook()
# basicRuleBook.addRule("DDFF STATUS", "estado .+\. ")
# basicRuleBook.addRule("DDFF TRABAJO", "\d:.*:")
# basicRuleBook.displayRules()
# messages = new_trigger.searchEmails(ventana)
# new_trigger.printEmailSearch(messages, basicRuleBook.getDict())

# print(
#    new_trigger.showTagMatch(
#        sample_text,
#        basicRuleBook.rules["ID DDFF"],
#    )
# )
