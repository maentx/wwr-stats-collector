#!/usr/bin/python

import feedparser, os, hashlib
from time import gmtime, strftime

# items = {}
itemset = set()
dup_count = 0

def read_all_rss_feeds():
    import os
    dirn = "./feeds/"
    for file in os.listdir(dirn):
        if file.endswith(".rss"):
            iterate_over_rss_feed(os.path.join(dirn, file))

def iterate_over_rss_feed(filename):
    global dup_count
    d = feedparser.parse(filename)
    for entry in d.entries:
        key = "%s_%s" % (entry.published, entry.title)
        key_hash = hashlib.md5(key.encode('utf-8')).hexdigest()
        if key_hash in itemset:
            print('Found duplicate')
            dup_count += 1
            continue
        itemset.add(key_hash) # not checking for dupes as using a set



read_all_rss_feeds()
print("Duplicates found: %i" % dup_count)
print(len(itemset))
