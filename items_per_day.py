#!/usr/bin/python

import feedparser
from time import gmtime, strftime

d = feedparser.parse('feeds/remote-jobs.rss')
items = {}

for entry in d.entries:
    p = entry.published_parsed
    key = "%s-%s-%s" % (p[0], str(p[1]).zfill(2), str(p[2]).zfill(2))
    if not key in items:
        items[key] = 0
    items[key] += 1

for key, value in items.items():
    print("%s;%i" % (key, value))
