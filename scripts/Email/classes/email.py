# Defines the email type to be sahred among all other modules. This way ALFRED can always read an email no matter the origin.


class Email:
    "Common base class for all emails"
    emailCount = 0

    def __init__(
        self, id, SenderName, SenderEmailAddress, SentOn, To, CC, BCC, Subject, Body
    ):
        """Creates a NEW Email Object
        Keywords:
            self, SenderName, SenderEmailAddress, SentOn, To, CC, BCC, Subject, Body"""
        self.id = id
        self.SenderName = SenderName
        self.SenderEmailAddress = SenderEmailAddress
        self.SentOn = SentOn
        self.To = To
        self.CC = CC
        self.BCC = BCC
        self.Subject = Subject
        self.Body = Body
        Email.emailCount += 1

    def displayCount(self):
        print("Total emails %d" % Emails.emailCount)

    def displayEmail(self):
        print("From Name: " + self.SenderName)
        print("From email: " + self.SenderEmailAddress)
        print("Date: " + self.SentOn)
        print("To: " + self.To)
        print("CC: " + self.CC)
        print("BCC: " + self.BCC)
        print("Subject: " + self.Subject)
        print("Body: " + self.Body)

    def html_table(myList):
        """Aux method for generating HTML tables"""
        print("<table>")
        for element in myList:
            print("<tr><td>%s</td></tr>" % element)
        print("</table>")

    def html_body(text):
        pass
