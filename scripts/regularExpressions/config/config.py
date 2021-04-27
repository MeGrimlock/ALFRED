# ---------------------------------<Parameters>---------------------------------

file_to_analyze = "ingComMaro2021.CSV"
file_to_save = "ingcom-parsed.csv"

# ---------------------------------</Parameters>---------------------------------

# ------------------------------------TOKENS------------------------------------

email_token = "EMAIL"
url_token = "URL"
pseudourl_token = "PSEUDO-URL"
mpls_token = "MPLS"
sdwan_token = "SDWAN"
dns_token = "DNS"
apn_token = "APN"
vpn_token = "VPN"
datacenter_token = "DATACENTER"
planes_token = "PLANES"
internet_token = "INTERNET"
sms_token = "SMS"
ddff_token = "ID DDFF"
salesforce_token = "SALESFORCE"

tokens = [
    email_token,
    url_token,
    pseudourl_token,
    mpls_token,
    sdwan_token,
    dns_token,
    apn_token,
    vpn_token,
    datacenter_token,
    planes_token,
    internet_token,
    sms_token,
    ddff_token,
    salesforce_token,
]

# ------------------------------------Expressions------------------------------------

email_regex = "[\w-]{1,20}@\w{2,20}\.\w{2,3}"
url_regex = "(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?."
pseudourl_regex = "(http|ftp|https)[^\s]+"
mpls_regex = "(\d{1,2})(\smbps|mbps)|enlace"
sdwan_regex = "sd-wan|sdwan"
dns_regex = "DNS"
apn_regex = "apn"
vpn_regex = "vpn"
datacenter_regex = "Datacenter|Data Center|housing"
planes_regex = "planes pymes|planes|PLC(\d{2,3})"
internet_regex = "Internet corporativo|internet|Ancho de Banda|ip"
sms_regex = "sms|numero corto"
ddff_regex = "id\d{4}"
salesforce_regex = "Salesforce|sf"

regexs = [
    email_regex,
    url_regex,
    pseudourl_regex,
    mpls_regex,
    sdwan_regex,
    dns_regex,
    apn_regex,
    vpn_regex,
    datacenter_regex,
    planes_regex,
    internet_regex,
    sms_regex,
    ddff_regex,
    salesforce_regex,
]

# ------------------------------------Dictionary------------------------------------

tokensNregex = dict(zip(tokens, regexs))

# ------------------ Particular rules for ClientesDatos processing-----------------------

# Sample: El caso del cliente ::: id3722:desinstalacion:D1082 GOFINAL PIETROBONI :::
#   ID:                            XXXX
#
#
get_id_regex = (
    "El caso del cliente ::: id\d{4}:desinstalacion:D1082 GOFINAL PIETROBONI :::"
)
