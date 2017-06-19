## SVG

### 什么是SVG?

SVG全称为Scalable Vector Graphics，译为可缩放矢量图形,简称矢量图。是一种用来描述二维矢量图形的XML标记语言。

### SVG与Flash的区别

*   相同点：用于二维矢量图形
*   不同点：
    *   SVG
        *   是一个W3C标准
        *   基于XML，开放的
    *   Flash
        *   封闭的基于二进制格式的

### SVG与Canvas的区别

*   SVG
    *   不依赖于分辨率
    *   使用DOM及事件处理器
        *   DOM专门为SVG开放接口(并不是之前所学习的DOM)
    *   不能实现游戏开发
    *   实现大型渲染区域的应用(例如百度地图)
*   Canvas
    *   依赖于分辨率
    *   是以图片(png|jpg)存在
    *   不能使用DOM及事件处理器
    *   可以实现游戏开发

### SVG的优势

*   不需要专门的编辑器,文本编辑器都可以
*   可被搜索、索引、脚本化及压缩
*   图像不失真(和分辨率无关)

### 注意

*   SVG技术并不是专属于HTML5的
*   SVG技术本身是一套独立的用于描述二维图形
*   HTML5版本之前,以图片形式进行引入
*   HTML5版本之后,允许在HTML页面直接使用SVG技术

### SVG文件(了解)

*   SVG文件的扩展名为".svg"
*   SVG使用的是XML语法
*   浏览器支持运行SVG文件

		<?xml version="1.0" encoding="utf-8" ?>
		<!-- SVG的语法标准(必要的) -->
		<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
		"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
		<!-- xmlns="http://www.w3.org/2000/svg" SVG的命名空间 -->
		<svg version="1.1"
		xmlns="http://www.w3.org/2000/svg">
		    <rect x="100" y="100" width="300" height="100" fill="blue" stroke="black" stroke-width="4"/>
		</svg>


----------
### HTML使用SVG

#### HTML5之前如何使用SVG(了解)


````<img src="01_SvgFile.svg" width="800" height="500">````


#### HTML5之后如何使用SVG

*   在HTML页面中,允许直接定义SVG的元素(标签)
    *   学习有关SVG的一些HTML新元素
*   `<svg>`元素
    *   作用：类似于canvas元素
    *   特点
        *   默认的宽度和高度分别为300px和150px
        *   不具有任何的样式(默认情况下不显示)
    *   目的：表示当前使用SVG语法内容
    *   属性
        *   width和height：设置SVG的区域(高度和宽度)
        *   style：也可以设置CSS的属性
*   SVG的语法内容：绘制的图形


		<svg width="500" height="300" style="background:pink;">
		    <rect x="100" y="100" width="300" height="100" fill="blue" stroke="black" stroke-width="4"/>
		</svg>


## SVG基本形状元素

### 样式属性

*   fill：设置填充样式
*   stroke：设置描边样式
*   stroke-width：设置描边宽度

### 矩形

````<rect x="" y="" width="" height="" />`````

*   x和y：表示绘制矩形的左上角坐标值
*   width和height：表示绘制矩形的宽度和高度
*   rx和ry：表示绘制矩形的四个角的水平圆角和垂直圆角
    *   如果rx和ry的值分别为width/2和height/2,绘制圆形

> **注意：**
> 
> *   默认绘制出来的效果：实心矩形效果。
> *   可以实现"空心"的效果：不能实现空心效果。

	<svg width="1000" height="600" style="background:pink;">
	    <!-- 绘制矩形 -->
	    <rect x="10" y="10" width="100" height="100" />
	    <rect x="10" y="120" width="100" height="100" fill="white" stroke="black" />
	    <rect x="10" y="230" width="100" height="100" rx="10" ry="10" />
	    <rect x="10" y="340" width="100" height="100" rx="50" ry="50" style="fill:white;stroke:black;" />
	</svg>

### 圆形

````<cirlcle cx="" cy="" r="" />````

*   cx和cy：表示绘制圆形的圆心坐标值
*   r：表示绘制圆形的半径

		<svg width="1000" height="600" style="background:pink;">
		    <!-- 绘制圆形 -->
		    <circle cx="170" cy="60" r="50" />
		    <circle cx="170" cy="170" r="50" fill="white" stroke="black" />
		</svg>

### 椭圆

````<ellipse cx="" cy="" rx="" ry="" />````

*   cx和cy：表示绘制椭圆的圆心坐标值
*   rx：表示绘制椭圆的水平方向半径
*   ry：表示绘制椭圆的垂直方向半径

		<svg width="1000" height="600" style="background:pink;">
		    <!-- 绘制椭圆 -->
		    <ellipse cx="280" cy="70" rx="50" ry="60" />
		    <ellipse cx="280" cy="190" rx="50" ry="50" />
		    <ellipse cx="280" cy="300" rx="50" ry="30" />
		</svg>

### 线条

````<line x1="" y1="" x2="" y2="" stroke="" />````

*   x1和y1：表示绘制直线的起点坐标值
*   x2和y2：表示绘制直线的终点坐标值
*   stroke：设置绘制直线的样式(颜色)
*   stroke-width：设置绘制直线的宽度

		<svg width="1000" height="600" style="background:pink;">
		    <!-- 绘制直线 -->
		    <line x1="350" y1="10" x2="500" y2="200" stroke="black" stroke-width="10" />
		</svg>


### 折线

````<polyline points="" />````

*   points：表示绘制折线的起点、折点及终点坐标值
    *   格式：x1,y1 x2,y2 x3,y3 xn,yn
*   stroke：设置折线的颜色
*   stroke-width：设置折线的线宽
*   fill：设置与`<svg>`元素的背景色相同

		<svg width="1000" height="600" style="background:pink;">
		    <!-- 绘制折线 -->
		    <polyline points="520,20 520,200" stroke="black" stroke-width="10" />
		    <polyline points="550,20 550,200 700,200 700,20 540,20" stroke="black" stroke-width="20" fill="pink" />
		</svg>

### 多边形

````<polygon points="" />````

*   points：表示绘制多边形的所有点坐标值

		<svg width="1000" height="600" style="background:pink;">
		    <!-- 绘制多边形 -->
		    <polygon points="550,300 550,500 800,500" stroke="black" fill="pink" stroke-width="10" />
		</svg>


> **注意：**
> 
> *   一个HTML页面允许包含多个`<svg>`元素
> *   一个`<svg>`元素允许包含多个图形元素
> *   SVG的图形元素基本都是起始元素
> *   定义图形元素时,只定义开始元素,没有结束元素
>     *   浏览器在运行页面时,并不报错
>     *   浏览器解析这段元素代码时,自动补全结束元素
>     *   自动补全的结束元素是不正确的

----------

### 特效元素

#### 线性渐变

*   基准线 - 起点和终点坐标值

`<linearGradient id="" x1="" y1="" x2="" y2=""></linearGradient>`

*   id：便于其他元素进行引用
*   x1和y1：表示基准线的起点坐标值
    *   值范围为 0-1, 是百分值 0%-100%
*   x2和y2：表示基准线的终点坐标值
    *   值范围为 0-1, 是百分值 0%-100%

`<stop offset="" stop-color=""/>`

*   offset：表示设置渐变颜色的位置
*   stop-color：表示设置的渐变颜色
*   stop-opacity：表示设置渐变颜色的透明度

		<svg width="800" height="500">
		    <defs>
		        <linearGradient id="grd" x1="0" y1="0" x2="1" y2="1">
		            <stop offset="0" stop-color="red" stop-opacity="0.5" />
		            <stop offset="0.5" stop-color="green" stop-opacity="0.5" />
		            <stop offset="1" stop-color="blue" stop-opacity="0.5" />
		        </linearGradient>
		    </defs>
		    <rect x="0" y="0" width="200" height="200" fill="url(#grd)" />
		    <circle cx="400" cy="400" r="100" fill="url(#grd)" />
		</svg>

#### 射线(径向)渐变

*   基准线：中心点和焦点组成
    *   中心点：描述了渐变边缘位置
    *   焦点：描述了渐变的中心

`<radialGradient id="" cx="" cy="" r="" fx="" fy=""></radialGradient>`

*   id：便于其他元素进行引用
*   cx和cy：表示基准线中的中心点坐标值
    *   值范围为 0-1, 是百分值 0%-100%
*   r：设置其边缘位置
    *   值范围为 0-1, 是百分值 0%-100%
*   fx和fy：表示基准线中的焦点坐标值
    *   值范围为 0-1, 是百分值 0%-100%

			<svg width="800" height="500">
			    <defs>
			        <radialGradient id="grd1">
			            <stop offset="0" stop-color="red" />
			            <stop offset="1" stop-color="blue" />
			        </radialGradient>
			        <radialGradient id="grd2" cx="0" cy="0">
			            <stop offset="0" stop-color="red" />
			            <stop offset="1" stop-color="blue" />
			        </radialGradient>
			        <radialGradient id="grd3" r="1">
			            <stop offset="0" stop-color="red" />
			            <stop offset="1" stop-color="blue" />
			        </radialGradient>
			        <radialGradient id="grd4" fx="1" fy="1">
			            <stop offset="0" stop-color="red" />
			            <stop offset="1" stop-color="blue" />
			        </radialGradient>
			        <radialGradient id="grd5">
			            <stop offset="0" stop-color="red" />
			            <stop offset="0.5" stop-color="yellow" />
			            <stop offset="1" stop-color="blue" />
			        </radialGradient>
			        <radialGradient id="grd6" cx="0" cy="0">
			            <stop offset="0" stop-color="red" />
			            <stop offset="0.5" stop-color="yellow" />
			            <stop offset="1" stop-color="blue" />
			        </radialGradient>
			        <radialGradient id="grd7" r="1">
			            <stop offset="0" stop-color="red" />
			            <stop offset="0.5" stop-color="yellow" />
			            <stop offset="1" stop-color="blue" />
			        </radialGradient>
			        <radialGradient id="grd8" fx="1" fy="1">
			            <stop offset="0" stop-color="red" />
			            <stop offset="0.5" stop-color="yellow" />
			            <stop offset="1" stop-color="blue" />
			        </radialGradient>
			    </defs>
			    <rect x="0" y="0" width="200" height="200" fill="url(#grd1)" />
			    <rect x="210" y="0" width="200" height="200" fill="url(#grd2)" />
			    <rect x="420" y="0" width="200" height="200" fill="url(#grd3)" />
			    <rect x="630" y="0" width="200" height="200" fill="url(#grd4)" />
			    <rect x="0" y="210" width="200" height="200" fill="url(#grd5)" />
			    <rect x="210" y="210" width="200" height="200" fill="url(#grd6)" />
			    <rect x="420" y="210" width="200" height="200" fill="url(#grd7)" />
			    <rect x="630" y="210" width="200" height="200" fill="url(#grd8)" />
			</svg>

> **注意：**
> 
> *   渐变元素需要定义id属性,便于其他元素进行引用
> *   渐变元素定义在<defs>元素内
>     
>     *   <defs>元素内定义：表示该元素允许重复使用</defs>
>     
>     </defs>

### 设置滤镜

*   定义元素内：可以重复使用
*   定义元素
    *   表示使用一个滤镜
    *   一般定义id属性：便于其他元素进行引入

> **注意：**
> 
> *   该元素只是滤镜的容器
> *   该元素并不直接显示在HTML页面中

#### 高斯模糊

`<feGaussianBlur in="" stdDeviation="" />`

*   in：设置高斯模糊的样式
    *   SourceGraphic
    *   SourceAlpha
*   stdDeviation：Number值,设置模糊的程度


		<svg width="800" height="500">
		    <defs>
		        <filter id="myfilter">
		            <feGaussianBlur in="SourceGraphic" stdDeviation="5" />
		        </filter>
		    </defs>
		    <rect x="100" y="100" width="100" height="100" filter="url(#myfilter)" />
		</svg>


----------

### Two.js库基础内容

*   SVG的高级内容(动画等效果),不需要掌握原生用法
*   Two.js库用于封装SVG,是以我们更熟悉的方式

#### 特点

*   Two.js支持不同的上下文环境：
    *   SVG
    *   Canvas
    *   WebGL
*   Two.js提供相同(统一)地API方法
*   官网：[http://jonobr1.github.io/two.js/](http://jonobr1.github.io/two.js/)

### 如何使用Two.js库

*   在HTML页面
    *   引入Two.js库文件
    *   定义容器元素
*   在JavaScript代码
    *   获取HTML页面的容器元素
    *   通过Two.js库提供的Two()构造函数创建Two对象

        ```
        var params = {// 创建svg时初始化的数据
          width : 宽度,
          height : 高度
        }
        var two = new Two(params);

        ```

    *   将创建的Two对象添加到HTML页面容器元素内
        `two.appendTo(elem);`
    *   使用Two.js库提供的API方法绘制图形
    *   调用update()方法进行绘制



### Two绘制图形

*   圆形：makeCircle(x, y, radius)
*   直线：makeLine(x1, y1, x2, y2)
*   矩形：makeRectangle(x, y, width, height)
*   圆角矩形：makeRoundedRectangle(x, y, width, height, radius)
*   椭圆：makeEllipse(x, y, width, height)
*   多边形：makePolygon(ox, oy, r, sides)
*   路径：makePath(x1, y1, x2, y2, xN, yN, open)
*   星形：makeStar(ox, oy, or, ir, sides)

### 绘制图形方法

*   基本都返回对应图形对象
    *   调用makeCircle()绘制圆形,并返回圆形对象
*   图形对象的属性
    *   fill：设置填充样式
    *   stroke：设置描边样式
    *   linewidth：设置线条宽度
    *   opacity：设置透明度
    *   cap：设置线条端点形状,默认为"round"
    *   join：设置线条交点形状,默认为"round"
*   图形对象的方法



### 图形分组

*   调用Two对象的makeGroup()方法,进行图形分组
    *   makeGroup()方法任意图形对象作为参数
    *   makeGroup()方法返回分组对象
*   统一对分组对象进行样式的设置

> **注意：**
> 在统一样式设置后,针对不同图形进行个性化样式设置


### 提供动画效果(了解)

*   play()方法：提供一组循环动画
*   pause()方法：提供中止动画效果
*   update()方法：提供更新当前绘制或设置
