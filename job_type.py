#!/usr/bin/python

import feedparser
from time import gmtime, strftime

items = {}
count = 0
types = { 
           'Full-Time',
           'Contract',
           }
for jtype in types:
    items[jtype] = 0

def read_all_rss_feeds():
    import os
    dirn = "./feeds/"
    for file in os.listdir(dirn):
        if file.endswith(".rss"):
            iterate_over_rss_feed(os.path.join(dirn, file))

def iterate_over_rss_feed(filename):
    global items, types, count
    d = feedparser.parse(filename)
    for entry in d.entries:
        count += 1
        if not hasattr(entry, 'type') or not entry.type in types:
            continue
        items[entry.type] += 1

read_all_rss_feeds()

for key, value in items.items():
    percent = round ( 100 * (value / count), 2 )
    print("%s: %i (%s%%)" % (key, value, percent))
