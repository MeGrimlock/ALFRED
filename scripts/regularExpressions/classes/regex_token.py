class Regex_RuleBook:
    """
    Defines the Regex-Token Pair this can be then used with regex module for analysis.

    Token: The TAG that indicates what I'm identifying to the user
    REGEX: String that contains the regular expression to search for.
    """

    total_rules = 0
    rules = {}

    def __init__(self, name="Rule Book", loadDefault=True):
        """
        Token : Text ID describing the TAG
        REGEX : String that shuold be used to search
        """
        self.ruleBookName = name

        if loadDefault == True:
            self.resetRulebook()

    def displayCount(self):
        print("Total rules %d" % Regex_RuleBook.total_rules)

    def displayName(self):
        print("RuleBook Name: %s" % self.ruleBookName)

    def displayRule(self, token):
        print("{Token: %s , Regex: %s }" % (token, Regex_RuleBook.rules[token]))

    def displayRules(self):
        self.displayName()
        self.displayCount()
        for token, regex in Regex_RuleBook.rules.items():
            self.displayRule(token)

    def displayTokens(self):
        for token in Regex_RuleBook.rules.keys():
            self.displayRegex(token)

    def displayRegex(self, token):
        print(Regex_RuleBook.rules[token])

    def addRule(self, token, regex):
        Regex_RuleBook.total_rules += 1
        Regex_RuleBook.rules[token] = regex

    def getTokens(self):
        tokens = []
        for token in Regex_RuleBook.rules.keys():
            tokens.append(token)
        return tokens

    def getRegex(self, token):
        return Regex_RuleBook.rules[tokens]

    def getDict(self):
        return Regex_RuleBook.rules

    def deleteRule(self, token):
        del Regex_RuleBook.rules[token]

    def clearRuleBook(self):
        Regex_RuleBook.rules = {}
        Regex_RuleBook.total_rules = 0

    def resetRulebook(self):
        # Add rules to Rulebook
        self.addRule("EMAIL", "[\w-]{1,20}@\w{2,20}\.\w{2,3}")
        self.addRule(
            "URL",
            "(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?.",
        )
        self.addRule("PSEUDO-URL", "(http|ftp|https)[^\s]+")
        self.addRule("MPLS", "(\d{1,2})(\smbps|mbps)|enlace")
        self.addRule("SDWAN", "sd-wan|sdwan")
        self.addRule("DNS", "DNS")
        self.addRule("APN", "apn")
        self.addRule("VPN", "vpn")
        self.addRule("DATACENTER", "Datacenter|Data Center|housing")
        self.addRule("PLANES", "planes pymes|planes|PLC(\d{2,3})")
        self.addRule("INTERNET", "Internet corporativo|internet|Ancho de Banda|ip")
        self.addRule("SMS", "sms|numero corto")
        self.addRule("ID DDFF", "id\d{4}")
        self.addRule("SALESFORCE", "Salesforce|sf")