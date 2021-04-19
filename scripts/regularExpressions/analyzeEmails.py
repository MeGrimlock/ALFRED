# -*- coding: utf-8 -*-
import sys
from collections import Counter

from .config import config
from .textAnalysis import *

# -------------------Parse emails-------------------------------------------------------


def analyzeString(text):
    # output = []
    # total_tags = []
    temp_tokens = findTokens(text)
    # output.append([subject, temp_tokens])
    # if len(temp_tokens) > 0:
    # total_tags.append(temp_tokens)
    # output = dict(output)
    return temp_tokens
