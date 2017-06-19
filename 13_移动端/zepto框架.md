## 移动端zepto框架
- zepto.js 移动端开发框架；
- API及语句同jquery相似，但文件更小(可压缩至8KB)。
- 是目前功能完备的库中，最小的一个。

#### zepto.js特点

1、针对的是移动端

2、轻量级，压缩版本只有8KB

3、语法大部分同jquery一样，学习成本低，上手快。

4、响应，执行快。

5、同jquery一样都是以$为核心函数。

#### jQuery和zepto相同的语法特性
- 核心函数
	- 选择器字符串
	- Dom   Code
	- 创建html的标签 
	- function(){}
- 核心对象
	- $.each()
	- $.ajax()
	- $.isArray()
- jQuery对象
	- 核心函数调用返回的就是jQuery对象(伪数组)
	- 方法:addClass()   show() find()

#### zepto与jQuery的区别

**attr与prop的区别**

1、prop多用在标签的固有属性，布尔值属性。比如：a标签的href，class，selected，checked等。

2、attr多用在自定义属性上。

jquery中用attr获取布尔值属性且布尔值属性在标签内没有定义的时候会得到undefined；

zepto中用attr也可以获取布尔值属性; 

prop在读取属性的时候优先级高于attr，布尔值属性的读取还是建议用prop;

**坑！zepto中removeProp()的方法。在1.2+版本才支持。**

**Dom配置对象的区别**

zepto在插入dom元素时可以配置对象. 但是jQuery不能配置对象

比如：id，class等

	例子: var $insert = $('<p>我是新添加的p标签</p>', {
		id:'insert',
		class:'insert'
	});


**$each()遍历区别**

$.each(collection, function(index, item){ ... })

- 可以遍历数组,以index，item的形式
- 可以遍历对象，以key-value的形式
- 可以遍历字符串。以index，item的形式(jQuery不可以遍历字符串)
- 遍历json对象以字符串的形式遍历

**offset()区别**  **相对视口偏移量**

jQuery: 

- 获取匹配元素在当前视口的相对偏移。
- 返回的对象包含两个整型属性：top 和 left。此方法只对可见元素有效。

zepto:

- 获得当前元素相对于视口的位置。
- 返回一个对象含有： top, left, width和height(获取的宽高包括内边距和边框)


**获取宽高的区别**

jQuery:  (padding -- 补白)

- width(),height() ---内容区的宽高，没有单位px;
- .css('width') --- 获取内容区的宽高(包括内边距和边框)有单位px;

- innerHeight(),innerWidth() -- 高度宽度包括内边距
- outerHeight(),outerWidth() -- 高度宽度包括内边距和边框


zepto:  (padding -- 补白)

- width(),height() ---内容区的宽高(包括内边距和边框)，没有单位px;
- .css('width') --- 获取内容区的宽高 有单位px;
- 没有innerHeight/width和outerHeight/width 方法

**jQuery小技巧**

单独获取内边距: css('padding')

单独获取边框: css('border-width')

单独获取边框颜色: css('border-color')

**事件委托的区别**

原理就是将事件冒泡到父元素身上. event.target指向的子元素触发
jQuery:

事件委托只是找相应的event.target触发元素进行的回调函数执行,其他的并不关心。

zepto:

委托的事件先被依次放入数组队列里，然后由自身开始往后查找， 期间符合条件的回调函数都会触发，符合条件的元素委托的事件都会执行。

触发条件:

- 委托在同一个父元素身上
- 委托的是同一个事件
- 委托关联是操作与其关联的元素
- 顺序是从当前位置向后

**当触发条件任意一条不符合时, 等同于jQuery的事件委托**

**获取隐藏元素区别**

- 当display:none 时, jquery可以获取隐藏元素的宽高
- 当display:none 时, zepto不可以获取隐藏元素的宽高


#### zepto touch方法
- tap()单击事件 
- singleTap()  单击事件
- doubleTap()  双击事件
- longTap()    当一个元素被按住超过750ms触发。
- swipe() 滑动事件 在一个方向滑动大于30px即为滑动。否则算点击。

swipeLeft, swipeRight, swipeUp, swipeDown 

当元素被划过(同一个方向滑动距离大于30px)时触发。(可选择给定的方向)


**其他绑定事件统一使用on，off标准事件来绑定事件。**
			
	   
#### zepto form表单方法

1、serialize()

在Ajax post请求中将用作提交的表单元素的值编译成 URL-encoded 字符串。key(name)/value

2、serializeArray()

将用作提交的表单元素的值编译成拥有name和value对象组成的数组。
不能使用的表单元素，buttons，未选中的radio buttons/checkboxs 将会被跳过。

3、submit()

为 "submit" 事件绑定一个处理函数，或者触发元素上的 "submit" 事件。
当参数function没有给出时，触发当前表单“submit”事件，并且执行默认的提交表单行为，除非阻止默认行为。

	<form>
	    <input type="password" name="pw" value="123"/>
	    <input type="text" name="val" value="kobe"/>
	    <input type="checkbox" checked="checked" name="rember"/>
	    <input type="submit" value="按钮" name="anniu"/>
	</form>
	$('form').serialize();
	$('form').serializeArray();
