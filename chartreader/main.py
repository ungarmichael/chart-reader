# calculating the values using the 
# * reader
# * xaxis
# * yaxis
# * chart
# classes

from reader import Reader
from chart import Chart
import numpy as np
import cv2 as cv

def init():
    global img
    img = cv.imread('./input/1.png')

def test1():
    cv.imshow('ex1',img)
    cv.waitKey(0)
    # img.putpixel((30,60),(155,255,155))
    # cv.imshow('chucksl',img)
    # cv.waitKey(0)
    # values = Reader.loadImageIntoPixels('./input/1.png')
    # res = Chart.readTheDarkestValue(values[132])
    # print(res)
    # img.dr
    # presi()

# def presi(img):    
#     # cv.line(img,(0,0),(511,511),(255,0,0),5)
#     cv.imshow('1.jpg',img)
#     print(img[343,160])
#     cv.waitKey(0)

def main():
    init()
    test1()
    

if __name__ == "__main__":
    main()