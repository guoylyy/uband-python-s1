# -*- coding: utf-8 -*-
from os import path
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import csv



def main():
	
	# read the whole text
	reader = csv.reader(open('/Users/kudari/workspaces/final_homework/output/test.csv', 'r'))
	d = {}
	for k, v in reader:
		d[k] = int(v)
	# read the pic
	coloring = np.array(Image.open(path.join(d, "/Users/kudari/workspaces/final_homework/pic2.jpg")))

	# set stopwords
	stopwords = set(STOPWORDS)

	# gerenate a wordcloud image
	# create a wordcloud
	wc = WordCloud(
		max_font_size = 88, 
		background_color = 'white',
		font_path = "/Users/kudari/workspaces/final_homework/Fins-Regular.otf",
		width = 1000,
		height = 860,
		# 设置词云形状
		mask = coloring,
		stopwords = stopwords,
		max_words = 500,
		)

	# generate the cloud
	wc.generate_from_frequencies(frequencies = d)

	# create coloring from image
	image_colors = ImageColorGenerator(coloring)

	# show
	plt.imshow(wc.recolor(color_func = image_colors), interpolation="bilinear")
	plt.axis("off")
	plt.show()
	wc.to_file("/Users/kudari/workspaces/final_homework/test2.png")


if __name__ == "__main__":
    main()
