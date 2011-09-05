#!/usr/bin/env python

import csv
from xml.sax.saxutils import escape

sitemap = open('assets/sitemap.xml', 'w')
sitemap.write('<?xml version="1.0" encoding="UTF-8"?>\n')
sitemap.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

reader = csv.DictReader(open('sitemap.csv'))

for row in reader:
    sitemap.write('<url>\n')
    sitemap.write('<loc>%s</loc>\n' % escape(row['url']))
    sitemap.write('<changefreq>%s</changefreq>\n' % row['frequency'])
    sitemap.write('</url>\n')

sitemap.write('</urlset>')

