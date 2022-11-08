#!/usr/bin/python

import feedparser
from time import gmtime, strftime

items = {}
count = 0
regions = { 
           'USA Only',
           'Anywhere in the World',
           'North America Only',
           'Americas Only',
           'Latin America Only',
           'Europe Only',
           'Canada Only',
           'Oceania Only',
           'UK Only',
           'EMEA Only',
           'Other (don’t specify)'
           }
for region in regions:
    items[region] = 0

def read_all_rss_feeds():
    import os
    dirn = "./feeds/"
    for file in os.listdir(dirn):
        if file.endswith(".rss"):
            iterate_over_rss_feed(os.path.join(dirn, file))

def iterate_over_rss_feed(filename):
    global items, regions, count
    d = feedparser.parse(filename)
    for entry in d.entries:
        count += 1
        if not entry.region in regions:
            print(entry.region)
        for region in regions:
            if region in entry.region:
                items[region] += 1

read_all_rss_feeds()

for key, value in items.items():
    percent = round ( 100 * (value / count), 2 )
    print("%s: %i (%s%%)" % (key, value, percent))
