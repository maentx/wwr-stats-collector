#!/usr/bin/python

import feedparser
from time import gmtime, strftime

items = {}
terms = { 'Python', 'Java', 'Node', 'PHP', 'C++', 'JavaScript' }
for term in terms:
    items[term] = 0

def read_all_rss_feeds():
    import os
    dirn = "./feeds/"
    for file in os.listdir(dirn):
        if file.endswith(".rss"):
            iterate_over_rss_feed(os.path.join(dirn, file))

def iterate_over_rss_feed(filename):
    global items, terms
    d = feedparser.parse(filename)
    for entry in d.entries:
        # check if
        for term in terms:
            if term.lower() in entry.description.lower():
                items[term] += 1

read_all_rss_feeds()

for key, value in items.items():
    print("%s: %i" % (key, value))
