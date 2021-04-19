from .classes.email import Email

# other libraries to be used in this script
import os, time
from datetime import datetime, timedelta
import win32com.client
import sys, importlib

importlib.reload(sys)


def init():
    global outlook
    global mapi
    global inbox
    global messages
    global parsed_emails
    global total_emails
    global new_email

    outlook = win32com.client.Dispatch("outlook.application")
    mapi = outlook.GetNamespace("MAPI")

    for account in mapi.Accounts:
        print(account.DeliveryStore.DisplayName)

    inbox = mapi.GetDefaultFolder(6)

    total_emails = 0
    new_email = False

    parsed_emails = []


def saveMessage(msg):
    """Converts MESSAGE to email_type for inter module communications"""
    email = Email(
        msg.SenderName,
        msg.SenderEmailAddress,
        msg.SentOn.strftime("%m/%d/%Y %H:%M %p"),
        msg.To,
        msg.CC,
        msg.BCC,
        msg.Subject,
        msg.Body,
    )

    return email


def saveMessages():
    """Converts ALL MESSAGES to email_type for inter module communications"""
    global messages
    global parsed_emails
    for message in list(messages):
        try:
            parsed_emails.append(saveMessage(message))
        except Exception as e:
            print(e)


def getMessagesFromOutlook(SenderEmailAddress="", Subject="", timeWindow=0):
    """
    Returns emails from IMBOX that match filtering criteria from keywords.

    Keywords:

        SenderEmailAddress : Email address from sender (default "")
        Subject: Email subject (default "")
        timeWindow: Filters emails from "now" back in time up to timeWindow (in minutes) (default 0 / no filter)

    Returns:

        messages

    """
    global messages

    messages = inbox.Items
    if timeWindow > 0:
        received_dt = datetime.now() - timedelta(minutes=refreshRate)
        received_dt = received_dt.strftime("%m/%d/%Y %H:%M %p")
        messages = messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
    if SenderEmailAddress != "":
        messages = messages.Restrict(
            "[SenderEmailAddress] = '" + SenderEmailAddress + "'"
        )
    if Subject:
        messages = messages.Restrict("[Subject] = '" + Subject + "'")
    print(str(len(list(messages))) + " Messages Retrieved")
    saveMessages()
    return messages


def getAttachments():
    """
    GETs attachments from ALL emails filtered
    """

    # Let's assume we want to save the email attachment to the below directory
    outputDir = os.path.join(os.path.dirname(__file__), "Attachments")
    if not os.path.exists(outputDir):
        try:
            os.makedirs(outputDir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    try:
        for message in list(messages):
            try:
                s = message.sender
                for attachment in message.Attachments:
                    attachment.SaveASFile(os.path.join(outputDir, attachment.FileName))
                    print(f"attachment {attachment.FileName} from {s} saved")
            except Exception as e:
                print("error when saving the attachment:" + str(e))
    except Exception as e:
        print("error when processing emails messages:" + str(e))


def printMessage(msg):

    print("From Name: " + msg.SenderName)
    print("From email: " + msg.SenderEmailAddress)
    print("Date: " + msg.SentOn.strftime("%m/%d/%Y %H:%M %p"))
    print("To: " + msg.To)
    print("CC: " + msg.CC)
    print("BCC: " + msg.BCC)
    print("Subject: " + msg.Subject)
    print("Body: " + msg.Body)

    count_attachments = msg.Attachments.Count
    if count_attachments > 0:
        print("Attachments: ")
        for item in range(count_attachments):
            print("\t" + msg.Attachments.Item(item + 1).Filename)


def printMessages():

    global messages
    for message in list(messages):
        # contenido = message.body
        print("---------------------------------------")
        printMessage(message)
        print("---------------------------------------")
    return


def printSavedMessages():
    global parsed_emails
    for email in parsed_emails:
        print(email.Body)
