## Learning how to do RegEx in python. 
# https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/
##

import re
import numpy as np


def parseStory(story):
    GPTresponse = story #Enter repsonse from ChatGPT

    pattern = re.compile("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", re.MULTILINE | re.DOTALL )
    match = pattern.split(GPTresponse)

    return match