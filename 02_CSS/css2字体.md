## CSS2 字体样式
##### font-family 字体族
- 规定元素的字体系列
- 把多个字体作为一个"回退"系统保存.保证浏览器的支持
- ````Microsoft YaHei, tahoma, arial, Hiragino Sans GB, sans-serif````

##### font 字体类型
- 衬线字体(serif)：在字的笔划开始及结束的地方有额外的装饰
- 非衬线字体(sans-serif) : 没有额外的装饰，笔划粗细大致差不多。用于严肃场景
- 等宽字体  monospace
- 草书字体  cursive
- 虚幻字体  fantasy

##### font-size 设置字体大小

	- medium 默认值。一般浏览器默认是16px. chrome最小支持到12px
	- smaller 把 font-size 设置为比父元素更小的尺寸。
	- larger  把 font-size 设置为比父元素更大的尺寸。
	- length  把 font-size 设置为一个固定的值(常用)。单位px
	- %   把 font-size 设置为基于父元素的一个百分比值。
	- 可继承
- 注意：font-size 会影响 line-height 属性 进而影响一行中基线的位置

##### font-style 字体样式

	- normal  默认值。浏览器显示一个标准的字体样式。
	- italic  浏览器会显示一个斜体的字体样式。 
	- oblique 浏览器会显示一个倾斜的字体样式。
	- 可继承

##### font-weight 字体的粗细

	- normal 默认值。定义标准的字符。 
	- bold 定义粗体字符。 常用
	- bolder 定义更粗的字符。
	- lighter 定义更细的字符。 
	- 可继承

##### font-variant 小型大写字母字体

	- normal 默认值。浏览器会显示一个标准的字体。 
	- small-caps 浏览器会显示小型大写字母的字体。
	- 可继承

##### font简写
- 常见写法 font：字体样式 小型大写字母 字体粗细 字体大小/行高 字体族(多个)  

![](http://i.imgur.com/aEr4Kpd.jpg)
