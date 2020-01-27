#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 13:07:51 2018

@author: emma
"""

from bs4 import BeautifulSoup
from collections import Counter
import nltk
from nltk.corpus import stopwords
from urllib.request import urlopen

with urlopen("http://shakespeare.mit.edu/othello/full.html") as url:
    soup = BeautifulSoup(url, "lxml")
    text = soup.get_text().lower()
word = nltk.word_tokenize(text)
all_word = nltk.corpus.words.words("en")
word1 = [w for w in word if w not in set(stopwords.words('english')) and w.isalnum()]# words without stopwords
word2 = Counter([w for w in word1 if w not in all_word])# words are not in words corpus
old_word = [word2.most_common(25)[i][0] for i in range(25)]
print(old_word)