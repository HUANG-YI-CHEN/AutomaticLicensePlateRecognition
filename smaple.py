# -*- coding: utf-8 -*-
import os, sys
import cv2 as cv
import matplotlib.pyplot as plt
from numpy import tile
try:
    from lib.config import Config
except:
    from config import Config

## System Subroutine ###
clear = lambda: os.system( 'cls' )
unicode_cmd = lambda: os.system( 'chcp 65001 &' )

def alpg(imgPath, dstPath='', write_value=0):
    if not dstPath:
        dstPath = os.path.abspath('')+'\\dst'

    img = ''
    ''' 讀取彩色的圖片 '''
    try:
        img = cv.imread(imgPath)
    except:
        sys.exit("影像讀取失敗...")

    '''
    opencv imread 以BGR 儲存
    plotlib imshow 以RGB 展示
    '''
    img_src = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    ''' 轉換為灰度圖 '''
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    if write_value!=0:
        GrayImage = dstPath+'\\'+'GrayImage.jpg'
        cv.imwrite(GrayImage, img_gray)

    ''' 高斯模糊 '''
    img_gaussian = cv.GaussianBlur(img_gray, (3,3), 5)
    if write_value!=0:
        GaussianBlurImage = dstPath+'\\'+'GaussianBlurImage.jpg'
        cv.imwrite(GaussianBlurImage, img_gaussian)

    ''' Laplacian進行邊緣檢測 '''
    img_sobel = cv.Sobel(img_gaussian, cv.CV_8U, 1, 0, ksize=1)
    img_canny = cv.Canny(img_sobel, 250, 100)
    if write_value!=0:
        SobelImage = dstPath+'\\'+'SobelImage.jpg'
        CannyImage = dstPath+'\\'+'CannyImage.jpg'
        cv.imwrite(SobelImage, img_sobel)
        cv.imwrite(CannyImage, img_canny)

    ''' 進行二值化處理 '''
    i,img_threshold = cv.threshold(img_canny, 0, 255, cv.THRESH_BINARY)
    if write_value!=0:
        ThresholdImage = dstPath+'\\'+'ThresholdImage.jpg'
        cv.imwrite(ThresholdImage, img_threshold)

    ''' 可以侵蝕和擴張 '''
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (43,33))
    img_dilate = cv.dilate(img_threshold, kernel)
    if write_value!=0:
        DilateImage = dstPath+'\\'+'DilateImage.jpg'
        cv.imwrite(DilateImage, img_dilate)

    titles = ['Source Image','Gray Image', 'Gaussian Image', 'Sobel Image',
            'Canny Image', 'threshold Image', 'dilate Image']
    images = [img, img_gray, img_gaussian, img_sobel, img_canny, img_threshold, img_dilate]

    ''' 顯示所有結果 '''
    for i in range(len(titles)):
        plt.subplot(3,3,i+1)
        plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.suptitle('Image Recognition',fontweight ="bold")
    try:
        plt.show()
    except Exception as e:
        raise e
    finally:
        plt.close('all')

def main():
    srcPath=""
    dstPath=""
    imgPath=""

    ''' 讀取 config.ini '''
    cfg= Config()
    try:
        srcPath = cfg.get('file')['src']
        imgPath = cfg.get('file')['img']
    except Exception as e:
        raise e

    ''' 假如路徑為空, 預設路徑為 ".\src" '''
    if not srcPath:
        srcPath = os.path.abspath('')+'\\'+'src'
        if not os.path.exists(srcPath):
            os.mkdir(srcPath)

    ''' 假如路徑為空, 預設路徑為 ".\dst"  '''
    if not dstPath:
        dstPath = os.path.abspath('')+'\\'+'dst'
        if not os.path.exists(dstPath):
            os.mkdir(dstPath)
    if not imgPath:
        imgPath = "lenna.jpg"

    ''' 判斷檔案是否存在, 不存在即離開程式 '''
    imgPath = srcPath+'\\'+imgPath
    if not os.path.exists(imgPath):
        sys.exit("圖片檔不存在...")

    if os.path.exists(dstPath+'\\'+'GrayImage.jpg'):
        os.remove(dstPath+'\\'+'GrayImage.jpg')
    if os.path.exists(dstPath+'\\'+'GaussianBlurImage.jpg'):
        os.remove(dstPath+'\\'+'GaussianBlurImage.jpg')
    if os.path.exists(dstPath+'\\'+'SobelImage.jpg'):
        os.remove(dstPath+'\\'+'SobelImage.jpg')
    if os.path.exists(dstPath+'\\'+'CannyImage.jpg'):
        os.remove(dstPath+'\\'+'CannyImage.jpg')
    if os.path.exists(dstPath+'\\'+'ThresholdImage.jpg'):
        os.remove(dstPath+'\\'+'ThresholdImage.jpg')
    if os.path.exists(dstPath+'\\'+'DilateImage.jpg'):
        os.remove(dstPath+'\\'+'DilateImage.jpg')
    ''' 執行影像辨識 '''
    alpg(imgPath, dstPath, 0)

if __name__ == '__main__':
    unicode_cmd()
    clear()
    main()