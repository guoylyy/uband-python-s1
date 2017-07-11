# -*- coding: utf-8 -*-
import wordcloud
import scipy
from PIL import Image



    
def generate_img(texts):

    bg = imread('D:\S1 homework\test.jpg')
    text = open('dt01.txt','r').read()
    word =wordcloud(
        background_color='white',
        mask=bg).generate(text)
    
    image_colors = ImageColorGenerator(bg)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    word.to_file(path.join(d, "test.png"))
    
if __name__ == "__main__":
    generate_img('dt01.txt')