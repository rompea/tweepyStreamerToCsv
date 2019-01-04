import json
import re
import csv
import os

a , b = 'áéíóúü', 'aeiouu'
trans = str.maketrans(a, b)

def remove_url(str):
    return re.sub(r"http\S+", "", str)


def removeSign(str):
    return re.sub(r"\?|(\¿)|(…)|(RT)|(\"\")|(\")|(\.)|(«)|(»)|(“)|(”) +", "", str)


def removeEnye(str):
    return re.sub(r"(n)/i", "n", str)

def strip_undesired_chars(tweet):
    stripped_tweet = tweet.replace('\n', ' ').replace('\r', '')
    char_list = [stripped_tweet[j] for j in range(
        len(stripped_tweet)) if ord(stripped_tweet[j]) in range(65536)]
    stripped_tweet = ''
    for j in char_list:
        stripped_tweet = stripped_tweet+j

    removed_url = stripped_tweet.translate(trans)
    return removeEnye(removeSign((remove_url(removed_url))))

def write(file_name,tweet, cont):
    with open(file_name + ".csv", "a", newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        if cont == 0:
            writer.writerow(['text'])
        else:
            writer.writerow([strip_undesired_chars(tweet)])
    pass