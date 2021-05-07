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
    global parsed_subjects
    global parsed_emails
    global total_emails
    global new_email
    global raw_subjectList
    global raw_bodyList

    outlook = win32com.client.Dispatch("outlook.application")
    mapi = outlook.GetNamespace("MAPI")

    for account in mapi.Accounts:
        print(account.DeliveryStore.DisplayName)

    inbox = mapi.GetDefaultFolder(6)

    total_emails = 0
    new_email = False

    parsed_emails = []
    parsed_subjects = []
    raw_subjectList = []
    raw_bodyList = []
    getInboxSubjects()
    getInboxBodys()


# -------------- EMAIL OPERATIONS-------------------


def createEmail(to, subject, body, attachment=None):
    """
    createEmail(to, subject, body, attachment="")

    If function returns "False" then there was an error.
    """
    global mail

    mail = outlook.CreateItem(0)

    retorno = False
    mail.To = to  #'zucale@telefonica.com'
    mail.Subject = subject  #'Message subject'

    mail.Body = body  # body #'Message body'
    # mail.HTMLBody = body  #'<h2>HTML Message body</h2>'  #this field is optional

    # To attach a file to the email (optional):
    att_file = attachment
    if att_file != None:
        try:
            mail.Attachments.Add(att_file)
            retorno = True
        except:
            print("error sending email, please retry")
    return retorno


def sendEmail(to, subject, body, attachment=None):
    global mail
    createEmail(to, subject, body, attachment)
    return mail.Send()


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


def getMessagesFromInbox(
    SenderName="", SenderEmailAddress="", SentOn="", Subject="", timeWindow=0
):
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
        received_dt = datetime.now() - timedelta(minutes=timeWindow)
        received_dt = received_dt.strftime("%m/%d/%Y %H:%M %p")
        messages = messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
    if SenderEmailAddress != "":
        messages = messages.Restrict(
            "[SenderEmailAddress] = '" + SenderEmailAddress + "'"
        )
    if SenderName != "":
        messages = messages.Restrict("[SenderName] = '" + SenderName + "'")
    if SentOn != "":
        messages = messages.Restrict("[SentOn] = '" + SentOn + "'")
    if Subject:
        messages = messages.Restrict("[Subject] = '" + Subject + "'")
    print(str(len(list(messages))) + " Messages Retrieved")
    saveMessages()
    return messages


def getInboxSubjects():
    """
    Loads all email subjects (without duplicates) into raw_SubjectList of the inbox.
    This can be used together with advanced REGEX searchs wich are easier to work with than OUTLOOKs built in ADVANCED SEARCH
    """
    global messages
    global raw_subjectList
    messages = inbox.Items
    for email in messages:
        raw_subjectList.append((email.EntryId, email.Subject))
    # Remove duplciates
    # raw_subjectList = list(dict.fromkeys(raw_subjectList))
    return raw_subjectList


def getInboxBodys():
    """
    Loads all email bodys (without duplicates) into raw_BodyList of the inbox.
    This can be used together with advanced REGEX searchs wich are easier to work with than OUTLOOKs built in ADVANCED SEARCH
    """
    global messages
    global raw_bodyList
    messages = inbox.Items
    for email in messages:
        raw_bodyList.append((email.EntryID, email.Body))
    # Remove duplciates
    # raw_bodyList = list(dict.fromkeys(raw_bodyList))
    return raw_bodyList


# -------------- SAVE DATA-------------------


def saveMessage(msg):
    """Converts MESSAGE to email_type for inter module communications

    Parameters

    msg: outlook email

    Returns:

    email: custom email format (soon to match Pythons email class)
    """

    email = Email(
        msg.EntryId,
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
    global parsed_subjects
    global parsed_emails
    for message in list(messages):
        try:
            parsed_emails.append(saveMessage(message))
            parsed_emails.append(message.Subject)
        except Exception as e:
            print(e)


# -------------- GET DATA-------------------
def getSubjectList():
    return parsed_subjects


def getParsedEmails():
    return parsed_emails


def getEmailByID(EntryId):
    global mapi
    msg = mapi.GetItemFromID(EntryId)
    return msg


# -------------- PRINT DATA-------------------
def printMessageBrief(msg):
    print("UniqueID: " + msg.EntryId)
    print("From Name: " + msg.SenderName)
    print("Date: " + msg.SentOn.strftime("%m/%d/%Y %H:%M %p"))
    print("Subject: " + msg.Subject)


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
