import re
from .config import config


def text2token(text, regex="[\w-]{1,20}@\w{2,20}\.\w{2,3}", token="--email--"):
    """ I like to keep it simple, so i rather have one versatile function than one for each token"""
    # function to find emails and replace with tokens ie: --email--
    result = re.sub(regex, token, text, flags=re.IGNORECASE)
    return result


def findRegex(text, regex="[\w-]{1,20}@\w{2,20}\.\w{2,3}"):
    result = re.findall(regex, text, flags=re.IGNORECASE)

    return result


def findTokens(text):
    """
    Parameters:
        text: text to analyze against all stored tags
    Returns:
        tags: a list with all tags that match regex search with text
    """
    config.tokensNregex
    tags = []
    for token in config.tokensNregex.keys():
        # replace keys with token
        # temp_text = text2token(temp_text, str(tokensNregex[token]), token)
        if len(findRegex(text, str(config.tokensNregex[token]))) > 0:
            tags.append(token)
    # email_processed = [text[2],text[0],tags]
    return tags