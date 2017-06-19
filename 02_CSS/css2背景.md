## CSS2 背景
##### background-color 设置背景颜色

##### background-image 设置背景图片
- ````background-image：url（"图片的路径"）;````

##### background-repeat 设置背景图片的重复方式

	- repeat 默认值. 使背景图片在水平和垂直两个方向重复.以铺满元素
	- repeat-x 水平方向重复
	- repeat-y 垂直方向重复
	- no-repeat 图片不重复

##### background-position 设置背景图片显示位置
- 默认背景图片是从左上角开始显示. 
- 设置方式:
	1. 通过位置的关键字来设置背景图片的位置
		- left top right bottom center
		- 使用这些关键字两两组合设置图片位置
		- 如果只设置一个关键字则第二个默认为center
	2. 可以指定一个水平方向和垂直方向的偏移量来设置图片位置
		-  background-position：x偏移量 y偏移量 
		-  x偏移量：正值 向右移动；负值 向左移动
		-  y偏移量：正值 向下移动；负值 向上移动

##### background-attachment 设置背景图片是否随屏幕滚动

	- scroll 默认值. 背景会随屏幕滚动
	- fixed 背景相对于窗口固定定位.不会随屏幕滚动
	- 使用场景: 网页的整体背景
	
##### background 简写
- 可以同时设置所有的背景相关的样式
- 对样式的编写顺序和数量没有任何要求
- 多个背景图片之间可以用逗号隔开
- ````background：red url() no-repeat top center````

##### img标签和background-image的区别
1.使用img元素引入图片,图片与网页同步加载,如果网页过大,影响页面加载速度

	- 使用img的场景: 重要的页面图片元素.例如 网站logo,商品图片

2.使用背景图引入图片,网页加载后,或者与网页一起加载.不会影响页面的加载速度

	- 使用背景图片的场景:非重要的页面图片元素,例如 小图片