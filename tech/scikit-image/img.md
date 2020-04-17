
# 
* bmp
```
[[[255 255 255]
  [  0   0   0]
  [255 255 255]]

 [[255 255 255]
  [255 255 255]
  [  0   0   0]]]
  
 
[[[0][1][2]][[3][4][5]]]
[[第一行][第二行]]
```


# PLI vs Pillow
PLI :Python Imaging Library  由于PIL不兼容setuptools，再加上更新缓慢等因素
为了继续支持PIL，所以fork了PIL，这就是Pillow的缘起

* Python安装Pillow
>> pip install Pillow
使用
from PIL import Image
im = Image.open("bride.jpg")
im.rotate(45).show()

# skimage在pycharm中显示图片
* 要两行代码io.imshow(img)和最后io.show()同，


# as_gray=True
```
[[1. 0. 1.]
 [1. 1. 0.]]
```


# 图像通道
RGB色彩模式(红色、绿色、蓝色)三个通道

什么叫灰度图？任何颜色都有红、绿、蓝三原色组成，假如原来某点的颜色为RGB(R，G，B)，那么，我们可以通过下面几种方法，将其转换为灰度：
1.浮点算法：Gray=R*0.3+G*0.59+B*0.11
2.整数方法：Gray=(R*30+G*59+B*11)/100
3.移位方法：Gray =(R*76+G*151+B*28)>>8;
4.平均值法：Gray=（R+G+B）/3;
5.仅取绿色：Gray=G；
通过上述任一种方法求得Gray后，将原来的RGB(R,G,B)中的R,G,B统一用Gray替换，形成新的颜色RGB(Gray,Gray,Gray)，用它替换原来的RGB(R,G,B)就是灰度图了。

https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py







































