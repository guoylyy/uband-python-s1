#!/usr/bin/env python

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

text = open(path.join(d, 'output/test.csv')).read()

wordcloud = WordCloud().generate(text)

image = wordcloud.to_image()
image.show()