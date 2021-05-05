# -*- coding: utf-8 -*-
import sys
from collections import Counter

from scripts.regularExpressions.textAnalysis import *

# -------------------Parse emails-------------------------------------------------------


def classifyEmail(body, subject, rulebook):
    texts = [body, subject]
    output = []
    total_tokens = []
    for text in texts:
        temp_tokens = findTokens(rulebook, text)
        output.append([text, temp_tokens])
        if len(temp_tokens) > 0:
            total_tokens.append(temp_tokens)
    output = total_tokens  # dict(total_tokens)
    return output


def showMatches(text, regex):
    return findRegex(text, regex)


def advancedSubjectSearch(Subject, SubjectsList):
    """
    Returns emails from IMBOX that match filtering criteria from keywords.

    Keywords:

        Subject: Email subject (String can be a REGEX)
        SubjectList: Subjects from all emails

    Returns:

        related_messages : List with all email_IDs that match the search pattern

    """
    related_subjects = []
    for temp_subject in SubjectsList:
        if len(re.findall(Subject, temp_subject[1], flags=re.IGNORECASE)) > 0:
            related_subjects.append(temp_subject[0])
    print(str(len(related_subjects)) + " Messages Retrieved")

    return related_subjects


def advancedBodySearch(Regex, BodyList):
    """
    Returns emails from INBOX that match filtering criteria from keywords.

    Keywords:

        Regex:  (String can be a REGEX)
        BodyList: Body from all emails

    Returns:

        related_messages : List with all email_IDs that match the search pattern

    """
    related_messages = []
    for temp_body in BodyList:
        if len(re.findall(Regex, temp_body[1], flags=re.IGNORECASE)) > 0:
            related_messages.append(temp_body[0])
    print(str(len(related_messages)) + " Messages Retrieved")

    return related_messages