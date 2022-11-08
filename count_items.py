#!/usr/bin/python

import feedparser
from time import gmtime, strftime

d = feedparser.parse('remote-jobs.rss')
count = 0

for entry in d.entries:
    count += 1

print("Found %i entries" % count)
