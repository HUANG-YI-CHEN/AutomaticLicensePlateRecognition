# Automatic License Plate Recognition
* 影像辨識學習-車牌辨識
* 影像處理步驟
  1. 讀取圖片
  2. 二值化
     1. 將彩色像素轉為黑白像素，取得灰階像素(0-255)，根據像素的值域設定一個灰階值標準，閥值(threshold)
     2. 根據灰階值大於 threshold 設白點，小於 threshold 設黑點，即黑(0)或白(255)
     3. 高斯模糊（高斯濾波）
        * 對圖像每個點，做「中間點」取「周圍點」的平均值
        * 模糊半徑越大，影象就越模糊
        * σ 值的意義及選取，代表離散程度，σ 值小，模板中心係數大，周圍係數小，較不平滑；σ 大，模板中心係數較平均，平滑較明顯
     4. 
  3. 形態學
     1. 侵蝕(erosion)
        * 消除影像中一些雜訊
     2. 膨脹(dilation)
        * 對偵測到的邊緣做增強，填補間隙
     3. 斷開(opening)
        * 平滑輪廓，去除雜訊小點和窄小的細線
        * 必要條件: erosion → dilation → opening
     4. 閉合(closing)
        * 平滑輪廓，填補圖像縫隙和連接斷線
        * 必要條件: erosion → dilation → closing
  4. 切割字母數字
  5. 辨識圖片

<img src="https://www.i-view.com.tw/wp-content/uploads/2020/07/blog-photo-16.png" width = "300" height = "200" alt="車牌辨識" align=center />

# Getting Started
## 系統需求
* `Python 3.0+`, `Git 2.0+`
> 若要使用 `Visual Studio code` 執行，需要裝 `Python`, `Code Runner`。
>> [補充] `Visual Studio code` 安裝
>> 1. `Markdown Preview Github Styling`
>> 2. `Auto-Open Markdown Preview`

>> 上述兩者擇一，即可在編輯 `ReadMe.md` 並即時顯示


## 安裝套件
* 若第一次執行程式，請打開 `CMD` 或 `Powershell` 執行以下安裝指令
```
python -m pip install --upgrade pip
pip install configparser numpy matplotlib pillow opencv-python --upgrade pip
```

## 設定檔
* 圖片來源目錄: `'.\src'`
* 圖片結果目錄: `'.\dst'`
* 預設圖片名稱: `'lenna.jpg'`
* 使用者可以依據需求自行更改，若不更動上述內容，則讀取預設目錄下的圖檔 `'.\src\lenna.jpg'`
* 使用者設定檔 `config.ini` 放置於專案根目錄下
> `config.ini` 內容如下 :
```
[file]
src=
dst=
img=lenna.jpg
```

## 程式執行
1. 切入程式放置資料夾
2. 同時點選 `滑鼠右鍵` 和 `鍵盤Shift`
3. 點擊 `在這裡開啟 Powershell 視窗` 或 `在這裡開啟 CMD 視窗`
4. 在 `Powershell` 或 `CMD` 輸入下列程式命令
```
python sample.py
```

## 參考網站
* [Python 與 OpenCV 基本讀取、顯示與儲存圖片教學](https://blog.gtwang.org/programming/opencv-basic-image-read-and-write-tutorial/)
* [Python影像辨識筆記目錄](https://yanwei-liu.medium.com/computer-vision-with-python-569dc58aff22)
* [影像辨識-古佳怡](https://ct.fg.tp.edu.tw/wp-content/uploads/2017/06/%E5%BD%B1%E5%83%8F%E8%BE%A8%E8%AD%98.pdf)
* [【OpenCV-Python系列Ⅳ】基礎影像處理集合包](https://grady1006.medium.com/opencv-python%E7%B3%BB%E5%88%97%E2%85%B3-%E5%9F%BA%E7%A4%8E%E5%BD%B1%E5%83%8F%E8%99%95%E7%90%86%E9%9B%86%E5%90%88%E5%8C%85-6c46fb2744ab)
* [[影象處理] Python+OpenCV實現車牌區域識別及Sobel運算元](https://iter01.com/90662.html)
* [python中值濾波去除反光_Python 實現中值濾波、均值濾波的方法](https://blog.csdn.net/weixin_35698059/article/details/113650706)
* [python中值濾波去除反光_數學之路-python計算實戰(17)-機器視覺-濾波去噪(中值濾波)](https://blog.csdn.net/weixin_32379547/article/details/113650705)
* [Opencv 去高光或鏡面反射（illuminationChange）_jacke121的專欄-程序員宅基地](http://www.cxyzjd.com/article/jacke121/95736092)
* [error: (-215:Assertion failed) npoints >= 0 && (depth == CV_32F || depth == CV_32S) in function '...](https://www.jianshu.com/p/f7930023dc62)
* [【沒錢ps,我用OpenCV!】Day 1 - 總是要從安裝 OpenCV 開始 + 電腦中圖片的基本概念(灰階、全彩RGB、座標軸、計算圖片大小)](https://ithelp.ithome.com.tw/articles/10235551)
* [【沒錢ps,我用OpenCV!】Day 9 - 日系濾鏡6，運用 OpenCV 降低圖片的高光 reduce highlights](https://ithelp.ithome.com.tw/articles/10240334)
* [[Day19]Matplotlib讓資料視覺化！](https://ithelp.ithome.com.tw/articles/10196239)
* [无缝融合seamlessClone()，调试颜色colorChange()，消除高亮illuminationChange()，纹理扁平化textureFlattening()（OpenCV案例源码cloning_demo.cpp解读](https://www.cnblogs.com/xixixing/p/12335317.html)

## 參考網站[理論]
* [影像辨識處理](https://www.smasoft-tech.com/show/knowledgebase-shemeshiyingxiangqianchuli.htm)
* [Image Algorithm](http://web.ntnu.edu.tw/~algo/Image.html)