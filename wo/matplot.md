
# matplot
https://matplotlib.org/

```
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()  # Create a figure containing a single axes.
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
ax.plot([1, 2, 3, 4, 5], [3, 3, 3, 3, 3])
plt.show()
```

# What is interactive mode?

# matplotlib绘图的两种模式“block”和“interactive”
### block
1.plt.plot()只有调用plt.show()或plt.pause()(窗口自动关闭)时才将内存中的图绘制到窗口
2.plt.show()时，暂停执行，直到关闭窗口
3.plt.pause(time)函数也能实现窗口绘图（不需要plt.show）,但窗口只停留time时间便会自动关闭，然后再继续执行后面代码；
4.如果plt.pause()和plt.show()一起使用时，前者相当于只是暂停时间
5.在python脚本模式中默认是block模式的。


```
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,2*np.pi,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(1)
plt.plot(x,y1) # 内存中绘制sin曲线
plt.show() #程序停留在此，直到图像窗口被关闭

plt.figure(2)
plt.plot(x,y2)# 内存中绘制cos曲线
plt.show()

```


在阻塞模式下，上述代码不会一次就把sin和cos两条曲线分别绘制在figure(1)和figure(2)上，而是先画figure(1)，
手动关闭后再画figure(2)。那么阻塞模式下如何实现一起绘制呢？全局只放一个plt.show()，
且在所有绘图函数结束后再放。
见下面只是点：plt.show()的作用：将内存中已经绘制好的图片一次性绘制在对应的坐标系统中。
因此，在block模式下，一般把plt.show()放在最后面，且只放一个，而不是而不是放中间或者放多个。


### interactive模式特点：
1. 开启interactive模式，用plt.ion()，放在绘图之前，关闭该模式用plt.ioff()；
2. 不用plt.show()或plt.pause()，只要plt.plot()等语句就能在窗口中绘图，但是，绘图后窗口立马自动关闭，
你压根都没法看清楚；可以用plt.pause(time)进行延迟自动关闭时间，需要注意的是如果有多个plt.pause()穿插在不同绘图函数下，
那么前面的窗口不会先关闭，会等到最后一个plt.pause()结束后再一起关闭。
该模式下要实现同时绘图，且保持，可用plt.pause(0)，但程序会结束在该位置，手动关闭窗口也不会继续执行了，因此plt.pause(0)应放在程序最后。
3. 该模式下，即使用了plt.show()也依然会自动关闭窗口，可在调用plt.show()之前调用plt.ioff()关闭交互模式，恢复到阻塞模式。
4. ipython模式下，默认是interactive模式


### mat and array
mat() 函数与array()函数生成矩阵所需的数据格式有区别，
mat()函数中数据可以为字符串以分号（;）分割或者为列表形式以逗号（，）分割，
而array()函数中数据只能为后者形式。
其次，两者的类型不同，用mat函数转换为矩阵后才能进行一些线性代数的操作。




























