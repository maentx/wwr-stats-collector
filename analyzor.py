#!/usr/bin/python

import feedparser
from time import gmtime, strftime

d = feedparser.parse('remote-jobs.rss')

for entry in d.entries:
    print(entry.title)
    # dPub = entry.title
    # dPubPretty = strftime(dPub, gmtime())
    # print(dPubPretty)
