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
