## CSS 高级

### 包含块和定位
- 定位的参照物就是包含块
- 根元素的包含块也称初始包含块(由用户代理:浏览器)
	- 初始包含块是一个视窗大小的矩形(定位参照)
	- 位置以及大小默认和视窗一样但不代表就是视口
	- 根元素不是html元素就是body元素
- 非根元素的相对定位或无定位时的包含块就是离它最近嵌套的块级元素
	- 如果没有,则包含块就是初始包含块
- 非根元素的绝对定位的包含块就是离它最近嵌套的开启了定位的块级元素
	- 从块级元素的padding区域开始排列
	- 如果没有,则包含块就是初始包含块
- margin和padding取百分比都是从包含块内容区的width中获取

	
### 浮动
- 最初用作图片的环绕
- 浮动元素的包含块是离它最近的块级祖先元素
- 浮动时要考虑提升层级分为两级
	- 文字
	- 盒模型 (浮动只提升半级)
- 其他情况下,层级提升只有一级 (盒模型)


----------

### 三列布局
- 实现布局的需求
	- 两边固定. 中间自适应
	- 中间部分必须完整的显示 ((2*left)width + (right)width)
	- 中间区域应该优先加载
- 最初的缺陷
	- 定位: 中间部分没有办法完整的显示. 在浏览器被缩小的情况下会被两边的区域覆盖
	- 浮动: 中间区域没有办法优先加载. 因为改变了html的顺序
- 基于浮动的变相方案
	- 圣杯布局 (伪等高布局)
	- 双飞翼布局
- 两组布局的对比
	- **都是把主列放在文档流最前面，使主列优先加载。**
	- **都是让三列浮动，然后通过负外边距形成三列布局。**
	- 圣杯布局是利用父容器的左、右内边距 + 两个从列相对定位
	- 双飞翼布局是把主列嵌套在一个新的父级块中. 利用主列的左、右外边距进行布局调整


### 圣杯等高布局
1. 为主容器清除浮动.解决浮动造成的高度塌陷
2. 左右元素想要两侧固定的话内容区必须要浮动.并且宽度修正为100%
	- 左右元素的宽度设置为固定值
3. **左元素设置负外边距为-100%**
	- margin为负值时,只修改元素的边界而不改变位置
	- 负值往内缩小. 正值往外扩大
	- 元素排列只认边界
4. **右元素设置负外边距为负的自身宽度的px值**
5. 给外层包裹内容区的容器设置左右的padding值.使其内容在页面中显示
	- 在padding和margin同时可以选择的前提下.优先考虑padding
6. **设置左右包裹元素为相对定位**
7. **设置左右包裹元素各自固定宽度的负偏移量的值.使其撑开位置**
8. 设置body的最小宽度. 使中间内容区必须可以显示
9. 等高实现
	- 设置左右包裹元素和中间内容区元素足够大的padding-bottom的值
	- 再设置跟padding-bottom一样大的负margin-bottom的值
	- 并且给包裹这些元素的父元素设置overflow:hidden
	
##### 圣杯等高布局 (代码实现)
	<!DOCTYPE html>
	<html lang="en">
	<head>
	  <meta charset="UTF-8">
	  <title>Title</title>
	  <style type="text/css">
	    * {
	      margin: 0;
	      padding: 0;
	    }
	
	    #header,#footer{
	      background: gainsboro;
	      border: 1px solid salmon;
	      text-align: center;
	    }

		/*1. 清除浮动:让浮动的子元素可以撑开它的父元素*/
	    .clearfix{
	      /*触发haslayout*/
	      *zoom: 1;
	    }
	    .clearfix:after{
	      content:'';
	      display: block;
	      clear: both;
	    }
	
	    /*为body设置最小宽度*/
	    body{
	      min-width: 600px;
	    }
	
	
	    #left,#right{
	      /*6. 设置左右相对定位并且让元素撑开位置*/
	      position: relative;
	
	      background: greenyellow;
	      float: left;
	      width: 200px; /*两边固定*/
	    }
	
	    #left{
	      left:-200px;
	      margin-left: -100%; /*3. left设置负外边距*/
	    }
	
	    #right{
	      right:-200px;
	      margin-left: -200px; /*4. right设置负外边距*/
	    }
	
	    #middle{
	      background: blue;
	
	      /*2. 左右包裹必须浮动.并进行宽度修正 100% */
	      float: left;
	      width: 100%;
	    }
	
		#container{
	      /*5. 显示middle区域*/
	      padding: 0 200px;
		/*伪等高父元素设置overflow:hidden*/
	      overflow: hidden;
	    }


	    /*伪等高实现*/
	    #left,#right,#middle{
	      padding-bottom: 1000px;
	      margin-bottom: -1000px;
	    }

	  </style>
	</head>
	<body>
	  <div id="header">
	      <h4>Header</h4>
	  </div>
	
	  <div id="container" class="clearfix">
	
	    <div id="middle">
	      <h4>M</h4>
	      <h4>M</h4>
	      <h4>M</h4>
	      <h4>M</h4>
	      <h4>M</h4>
	      <h4>M</h4>
	      <h4>M</h4>
	      <h4>M</h4>
	    </div>
	
	    <div id="left">L</div>
	    <div id="right">R</div>
	  </div>
	
	  <div id="footer">
	    <h4>footer</h4>
	  </div>
	</body>
	</html>

![](http://i.imgur.com/0vsmWGd.png)
	

----------

### 双飞翼布局
1. 为主容器清除浮动.解决高度塌陷
2. 左右元素想要两侧固定的话内容区必须要浮动.并且宽度修正为100%
	- 左右元素的宽度设置为固定值并且浮动
3. **左元素设置负外边距为-100%. 改变元素的边界会往内缩**
4. **右元素设置负外边距为负的自身宽度的px值**
5. **在内容区中嵌套一个div让其承载内容区的内容**
6. **设置内容区中div的padding值.使其内容在页面中显示**
	- 在padding和margin同时可以选择的前提下.优先考虑padding
7. 设置body的最小宽度. 使中间内容区必须可以显示
8. 等高实现
	- 同时设置左右元素和中间内容区元素足够大的padding-bottom的值
	- 再设置跟padding-bottom一样大的负margin-bottom的值
	- 并且给包裹这些元素的父元素设置overflow:hidden

##### 双飞翼布局 (代码实现)
	<!DOCTYPE html>
	<html lang="en">
	<head>
	  <meta charset="UTF-8">
	  <title>Title</title>
	  <style type="text/css">
	    * {
	      margin: 0;
	      padding: 0;
	    }
	
	    /*1. 清除浮动:让浮动的子元素可以撑开它的父元素*/
	    .clearfix{
	      /*触发haslayout*/
	      *zoom: 1;
	    }
	    .clearfix:after{
	      content:'';
	      display: block;
	      clear: both;
	    }
	
	    /*7. 设置body最小宽度*/
	    body{
	      min-width: 600px;
	    }
	
	    #header,#footer{
	      background: #cc71ff;
	      border: 1px solid #5fc4fa;
	      text-align: center;
	    }
	
	    #left,#right{
	      background: #f4ff14;
	      width: 200px; /*2.定死高度并且同时浮动*/
	      float: left;
	    }
	
	    #left{
	      margin-left: -100%; /*3. left设置负外边距*/
	    }
	
	    #right{
	      margin-left: -200px; /*4. right设置负外边距*/
	    }
	
	    #middle{
	      background: #26ff26;
	      width: 100%;
	      float: left; /*2. 浮动*/
	    }
	
	    /*6.显示出内容*/
	    #middle-inner{
	      padding: 0 200px; /*优先使用padding*/
	    }
	
	    /*8.伪等高*/
	    #left,#right,#middle{
	      padding-bottom: 1000px;
	      margin-bottom: -1000px;
	    }
	    #container{
	      overflow: hidden;
	    }
	
	  </style>
	</head>
	<body>
	  <div id="header">
	    <h4>Header</h4>
	  </div>
	
	  <div id="container" class="clearfix">
	
	    <div id="middle">
	      <div id="middle-inner">
	        <!--5. 嵌套div 在里面显示内容 -->
	        <h4>M</h4>
	      </div>
	    </div>
	
	    <div id="left">L</div>
	    <div id="right">R</div>
	  </div>
	
	  <div id="footer">
	    <h4>footer</h4>
	  </div>
	
	</body>
	</html>

![](http://i.imgur.com/GPqesyt.png)

----------

### overflow
- visible	默认值。内容不会被修剪，会呈现在元素框之外。
- hidden	内容会被修剪，并且其余内容是不可见的。
- scroll	内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
- auto	如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。

###### 当父元素,子元素的高宽确定时:
- overflow: auto; 	父元素 < 子元素时,出现滚动条
- overflow: scroll;	不管父元素是不是小于子元素都出滚动条
- overflow: hidden;	子元素溢出部分都会被截掉

----------

### html和body的overflow
1. html元素或body元素中有且只有一个有overflow属性时,这个属性会传给上一层document身上
2. 当且仅当html和body都存在overflow属性时
	- body的overflow属性会作用于body自身上
	- html的overflow属性会作用于上一层document身上

###### 禁止系统滚动条且html,body和视口高度三合一

	html,body{
      /*禁止系统滚动条. 并且把html body 和视口高度三合一*/
      overflow: hidden; 
      height: 100%;
	 }

----------

### 绝对定位模拟固定定位 
- 解决固定定位因为浏览器兼容性或移动端浏览器造成的失效问题
- 实现方法:
	- 首先禁止系统滚动条
	- html和body都有overflow属性时,把滚动条加给body
	- 然后让body充满整个屏幕必须html和body的height都设置100%
	- 看上去滚动条是系统的.然后再用绝对定位模拟固定定位
- 实现原理: 
	- 只有系统滚动条才会移动初始包含块所以把滚动条放到body身上
	- 当body上的滚动条移动时初始包含块不会移动.只是body里的内容移动
	- 当初始包含块不会被移动时, 那么基于初始包含块绝对定位的元素也就不会被移动
	
	
###### 滚动条和初始包含块
- 系统滚动条未出现时, 初始包含块的大小和位置跟视口一模一样
- 系统滚动条出现时, 移动系统滚动条会让初始包含块的位置发生变化, 而视口永远不会动

###### 绝对定位模拟固定定位 (代码实现)
	<!DOCTYPE html>
	<html lang="en">
	<head>
	  <meta charset="UTF-8">
	  <title>Title</title>
	  <style type="text/css">
	    * {
	      margin: 0;
	      padding: 0;
	    }
	
	    /*1. 禁止系统滚动条*/
	    html,body{
	      overflow: hidden;
	      height: 100%;
	    }
	
	    /*2. body出现滚动条模拟固定定位*/
	    body{
	      /*margin: 30px;*/
	      border: 1px solid red;
	      overflow: auto;
	      height: 100%;
	    }
	
	    #test{
	      position: absolute;
	      left: 50px;
	      top: 50px;
	
	      width: 200px;
	      height: 200px;
	      background: greenyellow;
	    }
	  </style>
	</head>
	<body>
	  <div id="test"></div> <!-- 模拟固定定位 -->
	  <div style="height: 30000px"></div> <!-- 模拟滚动条-->
	</body>
	</html>

----------

### 底部粘贴布局
- 需求: footer始终固定在底部 (移动端常用)
- 实现原理:
	1. 必须要有外层包裹元素.显示的内容区要在包裹元素内.底部footer要在包裹元素的外部
	2. 由于footer始终要在底部且靠外层包裹元素高度支撑. 则要给外层包裹元素设置高度100%且最小高度等于视口高度
	3. 由于继承要一级一级实现,所以html和body都要设置height为100%
	4. 由于外层包裹元素高度为视口高度. footer要显示出来必须要设置等同于自身高度负外边距margin-top
	5. 当内容区的内容过多时会发生重叠情况.还要给内容区设置留白区域等同于footer自身高度的padding值
	6. footer位置始终靠外层包裹元素高度来支撑. 所以外层包裹元素还需要清除浮动确保高度始终被子元素撑开

###### 底部粘贴布局(代码实现)

	<!DOCTYPE html>
	<html lang="en">
	<head>
	  <meta charset="UTF-8">
	  <meta name="viewport" content="width=device-width,initial-scale=1.0">
	  <title>Title</title>
	  <style type="text/css">
	    * {
	      margin: 0;
	      padding: 0;
	    }
	
	    html,body{
	      overflow: hidden;
	      height: 100%;
	    }
	
		/*外层包裹元素*/
	    #warp{
	      height: 100%; /*3.高度必须一级一级拿下来.否则无法继承*/
	      min-height: 100%;/*2.最小高度等于视口高度. 给外层包裹元素*/
	    }
	
	    /*内容区*/
	    #main{
	      line-height: 30px;
	      background: blue;
	      text-align: center;
		/*5.由于内容溢出会覆盖底部. 所以应该给内容区添加一个留白区*/
	      padding: 30px;
	    }
	
	    /*底部*/
	    #footer{
	      height: 30px;
	      background: yellow;
	      text-align: center;
		/*4.负外边距 footer上来固定在底部*/
	      margin-top: -30px; 
	    }
	
	    /*6.footer位置始终靠warp高度来支撑. 最好给warp清除浮动确保高度始终被子元素撑开*/
	    .clearfix{
	      *zoom: 1;
	    }
	    .clearfix:after{
	      content:'';
	      display: block;
	      clear: both;
	    }
	  </style>
	</head>
	<body>
	
	<!--CSS选择器从右往左读性能最好-->
	  <div id="warp" class="clearfix">
	    <div id="main">
	      <!--1.必须要有包裹元素. 显示的内容要在包裹元素内. 底部要在包裹元素外部-->
	      <h4>main</h4> <br>
	      <h4>main</h4> <br>
	      <h4>main</h4> <br>
	      <h4>main</h4> <br>
	      <h4>main</h4> <br>
	      <h4>main</h4> <br>
	    </div>
	  </div>
	  <div id="footer">footer</div>
	</body>
	</html>


----------

### 水平居中
- 元素水平居中: margin: 0 auto;
- 内容水平居中: text-align: center; 

### 水平垂直居中方案一
- 实现方案
	- 使用定位和负外边距
	- 外层包裹元素相对定位
	- 要水平垂直居中的元素绝对定位
	- 设置其left和top为50%. 从包含块中计算
	- 设置margin-left和top为负的自身宽高的一半
- 缺点: 必须知道自身的宽高还需要定位
###### 代码实现
    #wrap{
      position: relative;

      width: 300px;
      height: 300px;
      border: 1px solid blue;
      margin: 0 auto;
    }

    #inner{
      position: absolute;
      left: 50%;
      top:50%;
      margin-left: -50px;
      margin-top: -50px;

      width: 100px;
      height: 100px;
      background: red;
    }


### 水平垂直居中方案二
- 绝对定位盒子特性:
	- left + right + margin(L&R) +  border(L&R) + padding(L&R) + width = 包含块的padding区域的宽度
	- top + bottom + margin(T&B) +  border(T&B) + padding(T&B) + height = 包含块的padding区域的高度
- 实现方案
	- 利用绝对定位盒子的特性
	- 外层包裹元素相对定位
	- 要水平垂直居中的元素绝对定位
	- 其left\top\right\bottom都为0
	- margin为auto
- 缺点: 必须知道自身的宽高还需要定位
###### 代码实现
    #wrap{
      position: relative;

      width: 300px;
      height: 400px;
      border: 1px solid blue;
      margin: 0 auto;
    }

    #inner{
      position: absolute;
      left: 0;
      top:0;
      right: 0;
      bottom:0;
      margin: auto;

      width: 100px;
      height: 100px;
      background: red;
    }


### 水平垂直居中方案三
- 实现方案
	- 利用CSS3的transform中的translate3d
	- 该属性计算都是基于自身计算
	- 设置x轴50%, y轴50%, x轴0
	- 外层包裹元素相对定位
	- 要水平垂直居中的元素绝对定位
	- 设置left和top各为50%
- 缺点: 兼容性问题
###### 代码实现
    #wrap{
      position: relative;

      width: 300px;
      height: 400px;
      border: 1px solid blue;
      margin: 0 auto;
    }

    #inner{
      position: absolute;
      left: 50%;
      top:50%;

      transform: translate3d(-50%,-50%,0); 

      background: red;
    }


### 水平垂直居中方案四
- 实现方案
	- 利用display:table
	- 外层包裹元素设置display:table
	- 外层包裹元素设置水平居中和行高(行高等于自身高度)
	- 内容区垂直居中元素设置 display: table-cell
- 缺点: 基线问题难以处理. 纯文本建议用此方法
###### 代码实现
    #wrap{
      display: table;
      line-height: 400px;
      text-align: center; /*可继承属性*/

      width: 300px;
      height: 400px;
      border: 1px solid blue;
      margin: 0 auto;
    }

    #inner{
      display: table-cell;
      background: red;
    }

----------

### BFC
> #### box 盒子概念
- Box 是 CSS 布局的对象和基本单位， 直观点来说，就是一个页面是由很多个 Box 组成的。
- 元素的类型和 display 属性，决定了这个 Box 的类型。 不同类型的 Box， 会参与不同的 Formatting Context（一个决定如何渲染文档的容器）
- block-level box:
	- display 属性为 block, list-item, table 的元素
- inline-level box:
	- display 属性为 inline, inline-block, inline-table 的元素
	

> #### Formatting Context
- Formatting context 是 W3C CSS2.1 规范中的一个概念。
- 它是页面中的一块渲染区域，并且有一套渲染规则，它决定了其子元素将如何布局，以及和其他元素的关系和相互作用。
- 分类:
	- Block fomatting context (简称BFC)
	- Inline formatting context (简称IFC)。

#### BFC 
- 又称"块级格式化上下文"。就是一套规则. 它是一个独立的渲染区域，只有Block-level box参与
- 它规定了内部的Block-level Box如何布局，并且与这个区域外部毫不相干
	
#### BFC布局规则
1. **内部的Box会在垂直方向，一个接一个地放置。 (块级元素独占一行)**
2. **BFC的区域不会与float box重叠.但margin层无效。 (两列布局)**
3. **内部的Box垂直方向的距离由margin决定。属于同一个BFC的 两个相邻 块级盒子 的margin会发生重叠**
4. **计算BFC的高度时，浮动元素也参与计算。 (清除浮动时用)** 
5. BFC就是页面上的一个隔离的独立容器，容器里面的子元素不会影响到外面的元素。反之也如此。
6. 每个元素的margin box的左边， 与包含块border box的左边相接触(对于从左往右的格式化，否则相反)。即使存在浮动也是如此。

#### 开启BFC
- 根元素
- float属性不为none
- position为absolute或fixed
- overflow不为visible
- 除overflow外其他的方法会使margin左右自动失效

#### 解决margin重叠问题
- 方案一: 设置其中一个div的display为inline-block; 不同属于同一个BFC
- 方案二: 嵌套div导致的margin重叠可以为其中一个div添加border使其不相邻解决

###### BFC实现两列布局
	<!DOCTYPE html>
	<html lang="en">
	<head>
	  <meta charset="UTF-8">
	  <title>Title</title>
	  <style type="text/css">
	    * {
	      margin: 0;
	      padding: 0;
	    }
	    html,body{
	      height: 100%;
	    }
	
	    body{
	      min-width: 600px;
	    }
	
	    #left{
	      width: 200px;
	      height: 100%;
	      background: blue;
	
	      float: left;
	    }
	
	    #right{
	      height: 100%;
	      background: yellowgreen;
	      /*BFC的区域不会与float box重叠。开启BFC*/
	      overflow: hidden;
	    }
	  </style>
	</head>
	<body>
	    <div id="left">L</div>
	    <div id="right">R</div>
	</body>
	</html>

----------

### haslayout
- layout是windows IE的一个私有概念，它决定了元素如何对其内容定位和尺寸计算，以及与其他元素的关系和相互作用。
- 当一个元素“拥有布局”时，它会负责本身及其子元素的尺寸和定位。
- 而如果一个元素“没有拥有布局”，那么它的尺寸和位置由最近的拥有布局的祖先元素控制。
- haslayout属性只针对IE6和IE7。

#### haslayout由来
- 早期IE引擎如果所有元素都“拥有布局”的话，会导致很大的性能问题
- 所以只将"拥有布局"应用于实际需要的那些元素
- 所以便出现了“拥有布局”和“没有拥有布局”两种情况

#### 默认拥有布局的元素
	html, body, table, tr, td, img, hr,
	input, select, textarea, button,
	iframe, embed, object, applet, marquee

#### 怎么触发haslayout
- float: left或right
- display: inline-block
- position: absolute
- width: 除auto外任何值
- height: 除auto外任何值
- zoom: 除normal外任何值(zoom: 1无法在IE5.0中触发haslayout)
- writing-mode: tb-rl
	
- 在IE7中，以下属性也可以触发元素的haslayout
	- min-height: 任意值
	- min-width: 任意值
	- max-height: 除none 外任意值
	- max-width: 除none 外任意值
	- overflow: 除visible外任意值，仅用于块级元素
	- overflow-x: 除visible 外任意值，仅用于块级元素
	- overflow-y: 除visible 外任意值，仅用于块级元素
	- position: fixed

----------

### 清除浮动
- 让浮动的子元素撑起父元素的高度
###### 清除浮动方法一: 给父元素直接设置高度
缺点: 扩展性不好
	
	#wrap{
      border:1px solid;
      /*1. 直接添加高度*/
      height: 400px;
    }

    #inner{
      float: left;
      width: 100px;
      height: 100px;
      background: green;
    }

	<div id="wrap">
	     <div id="inner"></div>
	</div>

###### 清除浮动方法二: 开启BFC
缺点: IE6浏览器不支持. 有可能会造成一些不可预知的结果

    #wrap{
      border:1px solid;

      /*2. 开启BFC 缺点: 无法兼容IE6*/
      overflow: hidden;
    }

    #inner{
      float: left;
      width: 100px;
      height: 100px;
      background: green;
    }

	<div id="wrap">
	     <div id="inner"></div>
	</div>

###### 清除浮动方法三: 空标签清除浮动
缺点: 结构行为样式不统一

    #wrap{
      border:1px solid;
    }

    #inner{
      float: left;
      width: 100px;
      height: 100px;
      background: green;
    }

	  <div id="wrap">
	     <div id="inner"></div>
	     <div style="clear: both"></div> 
	  </div>

###### 清除浮动方法四: br标签清除
缺点: 利用html标签属性. 增加了结构

    #wrap{
      border:1px solid;
    }

    #inner{
      float: left;
      width: 100px;
      height: 100px;
      background: green;
    }

	  <div id="wrap">
	    <div id="inner"></div>
	    <br clear="all"> 
	  </div>

### 清除浮动方法五: 伪元素 (推荐使用)

    #wrap{
      border:1px solid;
    }

    #inner{
      float: left;
      width: 100px;
      height: 100px;
      background: green;
    }

    .clearfix{
      *zomm:1; /*兼容IE6和IE7. 触发了haslayout*/
    }
    .clearfix:after{
      content: '.';
      display: block;
      clear: both;
      height: 0;
      visibility: hidden;
    }

	  <div id="wrap" class="clearfix">
	     <div id="inner"></div>
	  </div>


#### 文本出现省略号
1. 处理的元素首先是块元素
2. 截断多余部分
3. 设置文本不换行
4. 文本溢出时出现省略号

		  display: block;
	      overflow: hidden;
	      white-space: nowrap;
	      text-overflow: ellipsis;

----------

### CSS3 过渡
- transition: 属性书写顺序
	- 首选过渡时间 transition-duration
	- 过渡CSS样式 transition-property
	- 过渡速度曲线 (可设置贝塞尔曲线)
	- 延迟时间 transition-delay
- transition 事件
	- obj.addEventListener('transitionend',function(){},false);
	- Webkit内核：obj.addEventListener('webkitTransitionEnd',function(){},false);
	
### CSS3 2d变换
- **旋转 transform:rotate(360deg)** 
	- 正值:顺时针旋转
	- 负值:逆时针旋转
	- 只能设单值。正数表示顺时针旋转，负数表示逆时针旋转
- **斜切 transform:skew(45deg,15deg)**
	- 第一个参数代表与y轴之间的角度
	- 第二个参数代表与x轴之间的角度
	- 正值:正斜杠方向
	- 负值:反斜杠方向
	- skewX(45deg):参数值以deg为单位 代表与y轴之间的角度
	- skewY(45deg):参数值以deg为单位 代表与x轴之间的角度
- **缩放 transform:scale(2)**
	- 表示X轴和Y轴等值缩放。
	- 默认值为1，要缩小请设0.01～0.99之间的值
	- 要放大请设超过1的值。
	- X轴缩放，可以用scaleX(.5)相当于scale(.5, 1)。
	- Y轴缩放，可以用scaleY(.5)相当于scale(1, .5)
	- 负数会先将元素反转再缩放
- **位移 transform:translate(-100px,200px)**
	- 第一个参数代表x轴位移偏移量
	- 第一个参数代表y轴位移偏移量
	- 正值:往左/往下
	- 负值:往右/往上
	- translateX(200px):代表x轴位移偏移量
	- translateY(200px):代表y轴位移偏移量
- **变换基点 transform-origin**
	- 可设置left, right, bottom, top, center, %, px值
	- px值偏移量参照左上角 (0,0) 点
	- rotate:参照中心点变换
	- skew:参照中心点变换
	- scale:参照中心点变换
	- translate:参照本身
	
#### 2d变化多组合
- 执行顺序: 从右往左. 
- 只认最初点和最终点.并以组合变换形式进行变换
- 当translate位移在最左时, 位移位置不受变化
- 当translate位移在最右时, 位移位置受矩阵计算影响
- transform多组合有rotate切换时, 变换个数和变换种类以及书写顺序必须一致. 否则过渡会失效


----------

### flex 伸缩盒模型
#### old flex
- display: -webkit-box; (移动端支持)
- 容器布局方向
	- -webkit-box-orient: vertical; 垂直排列
	- -webkit-box-orient: horizontal; 水平排列
- 项目布局方向
	- -webkit-box-direction: normal; 默认方向显示子元素
	- -webkit-box-direction: reverse; 反方向显示子元素
- 水平方向富裕空间管理
	- 富裕空间的管理只是用来确定富裕空间的位置. 并不给项目增加空间
	- -webkit-box-pack: center; 富裕空间水平方向去两侧
	- -webkit-box-pack: start; 富裕空间去右侧
	- -webkit-box-pack: end; 富裕空间去左侧
	- -webkit-box-pack: justify; 富裕空间平均分配到项目之间
- 垂直方向富裕空间管理
	- -webkit-box-align: center; 富裕空间垂直方向去两侧
	- -webkit-box-align: start; 富裕空间去底部
	- -webkit-box-align: end; 富裕空间去顶部
- 弹性空间管理
	- 将富裕空间按比例分配到每个项目中上. 会改变项目的空间
	- 设置在项目元素内
	- -webkit-box-flex: 1;

#### new flex
- display: flex;
- 容器布局方向
	- flex-direction: row;  水平排列
	- flex-direction: column;  垂直排列
- 项目布局方向
	- flex-direction: row-reverse;  水平反方向显示子元素
	- flex-direction: column-reverse;  垂直反方向显示子元素
- 水平方向富裕空间管理
	- 富裕空间的管理只是用来确定富裕空间的位置. 并不给项目增加空间
	- justify-content: center; 富裕空间水平方向在两侧
	- justify-content: start; 富裕空间在右边
	- justify-content: end; 富裕空间在左边
	- justify-content: space-between; 富裕空间平均分配到项目之间
	- justify-content: space-around; 富裕空间平均分配到每个项目两边
- 垂直方向富裕空间管理
	- align-items: center; 富裕空间垂直方向去两侧
	- align-items: flex-start; 富裕空间去底部
	- align-items: flex-end; 富裕空间去顶部
	- align-items: baseline; 富裕空间按基线分配
	- align-items: stretch; 没有高度的情况下让项目占满整个高度
- 弹性空间管理
	- 将富裕空间按比例分配到每个项目中上. 会改变项目的空间
	- 设置在项目元素内
	- flex-grow: 1;
- 平均分配
	- flex:1;
	- 等同于 `flex-grow: 1;flex-shrink: 1;flex-basis: 0;`
	