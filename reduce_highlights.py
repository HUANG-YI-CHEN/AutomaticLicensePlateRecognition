# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os, sys
from matplotlib import pyplot as plt

def reduce_highlights(img_path):
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 先轉成灰階處理
    ret, thresh = cv2.threshold(img_gray, 50, 255, 0)  # 利用 threshold 過濾出高光的部分，目前設定高於 200 即為高光
    contours, hierarchy  = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_zero = np.zeros(img.shape, dtype=np.uint8)    
    # print(len(contours))

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour) 
        img_zero[y:y+h, x:x+w] = 255 
        mask = img_zero 

    print("Highlight part: ")
    # show_img(mask)
    
    # alpha，beta 共同決定高光消除後的模糊程度
    # alpha: 亮度的缩放因子，默認是 0.2， 範圍[0, 2], 值越大，亮度越低
    # beta:  亮度缩放後加上的参数，默認是 0.4， 範圍[0, 2]，值越大，亮度越低
    result = cv2.illuminationChange(img, mask, alpha=0.5, beta=0.77) 
    cv2.imshow("result", result)
    cv2.waitKey(0)
        
    return result

def main():
    img_path = os.path.abspath('')+'\\'+'lenna.jpg'
    if not img_path:
        sys.exit("無法讀取影像...")
    
    reduce_highlights(img_path)
   
if __name__ == '__main__':
    sys.exit(main())