#!/usr/bin/python

import feedparser
from time import gmtime, strftime

d = feedparser.parse('remote-jobs.rss')

for entry in d.entries:
    dPub = entry.published
    dPubPretty = strftime(dPub, gmtime())
    print(dPubPretty)
