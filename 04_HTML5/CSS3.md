# CSS3
#### 目标伪类选择器
- :target 选取当前活动的目标元素
- url或者是href带 # (锚名称)指向文档内某个具体的元素。这个被链接的元素就是traget所选取的目标元素

#### 结构化伪类选择器
##### E: nth-of-type(参数)
- E: 表示选择器选中的元素
- nth-of-type 必须是同一层级的元素分组选择
- 可选参数
	- number     选择number指定位置上的元素
	- odd           选择奇数位置上的元素
	- even          选择奇数位置上的元素
	- an+b
		- a 分组的方向及分组的数量(正数从左向右.负数从右向左)
		- b 分组起始的位置 (如果是负则浏览器默认补齐)

##### E:nth-child()(参数)
- E: 表示选择器选中的元素
- nth-of-type 必须是同一层级的元素分组选择
- 同一层级下按照所有元素排序
- 可选参数
	- number     选择number指定位置上的元素
	- odd           选择奇数位置上的元素
	- even          选择奇数位置上的元素
	- an+b
		- a 分组的方向及分组的数量(正数从左向右.负数从右向左)
		- b 分组起始的位置 (如果是负则浏览器默认补齐)
	
![](http://i.imgur.com/ybpMOqV.jpg)

#### :checked状态伪类 & appearance
- :checked 选择器匹配每个已被选中的 input 元素（只用于单选按钮和复选框）
- appearance 清除input标签默认样式

#### 计数器
- counter 插入一个计数器
- counters 插入多个计数器
- counter-increment :num;  创建递增或递减一个或多个计数器。默认值是 1。
-  counter-reset: num; 创建或重置一个或多个计数器。默认值是 0。

#### 属性选择器
- attribute 属性名   value 属性值
- [attribute] 选择器用于选取带有指定属性的元素
- [attribute=value] 选择器用于选取带有指定属性值的元素。
- [attribute^=value] 选择器匹配属性值以指定值开头的每个元素。
- [attribute$=value] 选择器匹配属性值以指定值结尾的每个元素。
- [attribute~=value] 选择器用于选取属性值中包含指定单词的元素。
- [attribute|=value] 选择器用于选取带有以指定值开头的属性值的元素。(指定值必须是整个单词)

#### 伪元素选择器
- ::before 元素前添加伪元素
- ::after 元素后添加伪元素

特点:

1. 必须配合content属性使用。(空值,CSS和函数.也可以混合输出)
2. 伪元素都是行内元素(inline)
3. 双冒号是规范要求，实际开发中使用单冒号，目的是得到IE8的支持
4. 伪元素的文本内容无法被选中，伪元素也无法通过JS获取其对应的DOM.

使用场景:

1. 解决子元素浮动造成的父元素高度塌陷
	- 给父元素添加一个after伪元素
	- 必须添加:content:'""
	- 然后设置伪元素为块元素: display:block; //也可以用table
	- 最后清除浮动: clear:both;
2. 页面中"重复出现"的文本内容
3. 客制化目录前的序号或符号

#### 文本伪类选择器
- ::first-letter 选择一行中的首字母或文字
- ::first-line 选择元素第一行文本
- ::selection 选中文本样式的设置

#### 多媒体选择器
- @media 多媒体选择器
	- print 控制打印机页面的样式
		- arrr() 获取元素属性值
	- screen
		- 监控屏幕

### transition 过渡
- transition-property  设置有过渡效果的CSS属性
- transition-duration 设置过渡持续的时间 (核心)
- transition-delay 设置过渡延迟执行的时间
- transition-timing-function 设置过渡效果的速度曲线 
- 过渡样式覆盖
	- 逗号后的相同CSS名设置的过渡样式，会覆盖前面的过渡样式

### transform 2D变形
##### scale() 缩放函数
- 语法:
	- scale(x , y) 定义 2D 缩放转换，改变元素的宽度和高度。
	- scaleX(n)  定义 2D 缩放转换，改变元素的宽度。 
	- scaleY(n)  定义 2D 缩放转换，改变元素的高度。 
- 特点:
	1. 基于元素中心点缩放
    2. 元素的缩放不影响父元素的布局
    3. 元素的缩放不影响兄弟元素的位置
	4. 行内块元素,块元素有效果. 行内(inline)元素无法使用缩放函数
	5. 使用缩放函数,其内容及子元素也随之缩放
	
##### transform-origin 变形中心点
- 语法:
	- 定义视图在x轴何处
	- 定义视图在y轴何处
	- 可选: left,center,right,length,%
- 特点:
	1. 改变中心点位置,以设置的中心点位置变型
	2. 变换中心点的坐标轴也会随缩放的大小而变化
	3. x和y的值就是变换中心点的圆点位置

##### translate() 位移函数
- 语法:
	- translate(x , y) 定义 2D 转换，沿着 X 和 Y 轴移动元素。 
	- translateX(n) 定义 2D 转换，沿着 X 轴移动元素。 
	- translateY(n) 定义 2D 转换，沿着 Y 轴移动元素。

##### skew() 倾斜函数
- 语法
	- skew(x-angle , y-angle) 定义 2D 倾斜转换，沿着 X 和 Y 轴。 
	- skewX(angle) 定义 2D 倾斜转换，沿着 X 轴。使Y轴倾斜 正值逆时针 负值顺时针.单位deg
	- skewY(angle) 定义 2D 倾斜转换，沿着 Y 轴。使X轴倾斜 正值顺时针.负值逆时针.单位deg
- 特点:
	1. 元素的倾斜不影响父元素的布局
	2. 元素的倾斜不影响兄弟元素的位置
	3. 行内块元素,块元素有效果. 行内(inline)元素无法使用倾斜函数
	4. 使用倾斜函数,其内容及子元素也随之缩放
	5. 对其内容可以添加一个元素对其反倾斜设置.文字就不会倾斜

#####  rotate() 旋转函数
- 语法:
	- routate(angle) 旋转角度.单位deg
- 特点:
	1. 元素的旋转不影响父元素的布局
	2. 元素的旋转不影响兄弟元素的位置
	3. 行内块元素,块元素有效果. 行内(inline)元素无法使用旋转函数
	4. 使用旋转函数,其内容及子元素也随之缩放
	5. 可以设置中心点,以中心点为圆点的边进行旋转
	
	6. 如果中心点和旋转函数写一起会产生每旋转一次就会计算一次中心点

##### 变换函数注意事项
1. 不会影响相邻兄弟元素的位置。
2. 如果父元素没有指定高度，不会导致父元素高度的变化。
3. 只有在块元素中才生效。
4. 元素的文本及其后代元素都会变形。
5. 变换函数与过渡搭配使用时,变换中心点需要设置在原始样式处,不要设置在该样式的状态中.否则每变换一次就会重新计算中心点

##### 贝塞尔曲线函数
- cubic-bezier(n,n,n,n) 在 cubic-bezier 函数中定义自己的值。 0 至 1 之间的数值。 

----------

### transform 3D
##### transform-style 开启3D空间
- flat（默认值）     2D 
- preserve-3d        3D

##### translate3d 3D位移
- translate3d(x,y,z) 定义 3D 位移
- translateZ(n)  定义用z轴 3D位移
	- 负值是屏幕向内
	- 正值是屏幕向外
	- length单位是px

##### transform-origin:(x-axis,y-axis,z-axis) 3D变换中心点
- z-axis   定义视图被置于 Z 轴的何处。默认为0 
- 可选值必须是像素, 负值向内,正值向外.
- 注意: 不能使用关键字和百分比

##### rotate 3D旋转
- rotateX(angle) 定义沿着 X 轴的 3D 旋转。
- rotateY(angle) 定义沿着 Y 轴的 3D 旋转。 
- rotateZ(angle) 定义沿着 Z 轴的 3D 旋转。 

### 景深和景深中心点
##### perspective 景深
- 默认值： 0
- 元素距离视图的距离，单位PX。
- 景深中心点距离3D空间元素的距离
- 为3D空间设有一个近大远小的效果

##### perspective-origin 景深中心点
- perspective-origin: x-axis y-axis
	- 可选值: left. right. center. length. %
	- 默认值: 50% 50%
- 景深中心点必须与景深属性一同使用
- 特点:
    1. 当元素的位置固定时 景深越大,元素越接近实际元素的大小
	2. 当景深固定时,当元素向屏幕内侧移动 (z轴), 元素越小
	3. 当景深固定时,当元素向屏幕外侧移动 (z轴), 元素越大
	
##### backface-visibility 定义3D元素背面是否可见
- visible      背面是可见的。
- hidden     背面是不可见的。

### animation 动画
##### @keyframes 关键帧
- @keyframes animationname {keyframes-selector {css-styles;}}
	- animationname 	   必需。定义动画的名称。 
	- keyframes-selector  必需。动画时长的百分比。
	- css-styles 	          必需。一个或多个合法的 CSS 样式属性。
	
##### keyframes-selector
- 0-100%
- from (与0%相同)
- to (与100%相同)

##### animation-name  动画名称
- @keyframes 动画的名称
- animation-name 属性为 @keyframes关键帧设置的动画规定名称

##### animation-duration  动画执行时间
- 规定动画完成一个周期所花费的秒或毫秒。默认是 0。  单位time
- 注意: 始终规定 animation-duration 属性，否则时长为 0，就不会播放动画了。

##### animation-delay  动画延迟时间
- 规定动画何时开始。. 默认是 0。 单位time

##### animation-timing-function  动画效果
-  规定动画的速度曲线。默认是 "ease"。

##### animation-fill-mode  动画填充
- 属性规定动画在播放之前或之后，其动画效果是否可见。
- 可选值:
	- none 		不改变默认行为。 
	- backwards      在动画未播放时,显示动画的第一帧
	- forwards 	动画播放结束时,显示动画的最后一个帧
	- both 	        播放前和播放后填充模式都被应用

##### animation-iteration-count  动画播放次数
- 定义动画播放的次数
- 可选值:
	- n 定义动画播放次数的数值。默认值是 1 
	- infinite 规定动画应该无限次播放。 

##### animation-play-state  动画运行状态
- 规定动画正在运行还是暂停
- 可选值:
	- running 规定动画正在播放。 默认值 
	- paused 规定动画已暂停
	
#####  animation-direction  动画播放顺序
- 是否应该轮流反向播放动画
- 可选值:
	- normal 	   默认值。动画正常播放。 
	- alternate 动画交替反复播放.必须配合播放次数使用,大于1
	- reverse    动画反向播放 如果反向播放,第一帧是100%{}.最后一帧是0%{}
	
##### animation 简写:
- 可选属性:
	- animation-name  动画名字
	- animation-duration  动画执行时间
	- animation-timing-function  动画执行效果
	- animation-delay 	动画延迟执行时间
	- animation-iteration-count 	动画播放次数
	- animation-direction 	动画播放顺序

----------

### CSS3 边框
- transparent 边框的透明
- border-image：使用图片作为元素的边框。
- border-image-source 设置图片路径。  
- border-image-slice 边框图片切割方式
	- fill   	图片填充边框的四个角。默认值
	- 数字	基于图片边框的切割位置（不需要写单位，默认为px）
	- 百分比    基于图片的宽度或者高度
- border-image-repeat  边框图片显示样式
	- stretch: 	   四个边个图片被拉伸. 默认值
	- round:        四个边的图片重复平铺. 可以保证平铺的完整性       
	- repeat:  	   四个边的图片重复平铺. 
- border-image-width 边框图片的大小
- border-image-outset 边框图像区域超出边框的量。 

##### border-radius 圆角效果
- border-radius：length{1-4}
- border-radius: 水平半径/垂直半径
- 常用的圆角效果:
	- border-radius: 0;  没有圆角效果
	- border-radius:  50%;  如果元素是正方形，显示圆形
	- border-radius:  100% 0 0 0 ; 如果元素是正方形，显示扇形
	- border-radius:  50%; 如果元素是长方形，显示椭圆
	- 上下半圆: 元素宽度是高度的2倍. 并且半径值是元素高度
	- 左右半圆: 元素高度是宽度的2倍. 并且半径值是元素宽度

##### box-shadow  边框阴影效果
- 参数1：投影方式 
	- 默认值是外阴影
	- inset：内阴影类型，可选。如果不设置投影方式为外部阴影
- 参数2： X轴偏移量
	- h-shadow:阴影水平偏移。正值，阴影在元素右侧，负值在元素左侧。
- 参数3： Y轴偏移量
	- v-shadow:阴影垂直偏移。正式，阴影在元素底部，负值在元素顶部。
- 参数4：阴影模糊
	- blur-radius: 阴影的模糊半径，可选。只能为正值，如果设置为0，阴影不具备模糊效果。
- 参数5：阴影扩展
	- spread-radius: 阴影扩展半径。如果取正值，整个阴影都延展扩大，取负值，则整个阴影都缩小。
- 参数6：阴影颜色
	- color: 阴影的颜色。 可选参数

##### outline  元素轮廓
- outline-color  外轮廓颜色
- outline-style   外轮廓样式
- outline-width 外轮廓宽度
- outline-offset:  外轮廓偏移量，不会导致盒子大小改变

##### resize 调整元素盒子大小
- none:  用户不能调整元素宽高。
- both：用户可以调整元素宽高。
- horizontal: 用户只能调整元素宽度
- vertical: 用户只能调整元素高度

----------

### CSS3 背景
##### background-origin 背景原点属性
- border-box;
	- 背景图的background-position起始点（默认左上角（0,0））是从元素边框外边缘开始。
- padding-box;（默认值）
	- 背景图的background-position起始点（默认左上角（0,0））是从元素边框内边距（padding的外边缘）开始。
- content-box;
	- 背景图的background-position起始点（默认左上角（0,0））是从元素内容的边框外边缘（padding的内边缘）开始。

#####  background-clip 背景剪裁属性
- border-box;（默认值）
	- 元素外边框外的背景图片都将被裁裁剪掉。
- padding-box; 
	- 元素内边距区域外的背景图片都将被裁裁剪掉。
- content-box;
	- 元素内容区域外背景图片都将被裁裁剪掉。

##### background-size 背景尺寸属性
- auto; 默认值
	- 保持背景图原始的高度与宽度。就是背景图保持原样。
- length 
	- 设置背景图像的高度和宽度。
	- 第一个值设置宽度，第二个值设置高度。
- % 使用0%~100%的值。
	- 以父元素的百分比来设置背景图像的宽度和高度。
	- 第一个值设置宽度，第二个值设置高度。
- cover
	- 把背景图扩展至足够大，使背景图完全覆盖背景区域。但是背景图的某些部分也许无法显示在背景区域中。
- contain
	- 保持背景图片自身的宽高比例, 确保在元素中完整呈现图片, 使其宽高完全适应内容区域。
	
#####  线性渐变&径向渐变
- linear-gradient()  线性渐变函数
	- 参数(to 水平垂直方向 , 颜色 ) || (旋转角度, 颜色)
	- ````background-image: linear-gradient(to right, red, yellow, blue, green);````
- repeating-linear-gradient(); 重复线性渐变
	
		background: repeating-linear-gradient(
			to right 
			,red 0px
			,red 50px
			,black 50px
			,black 100px
		);

- radial-gradient( )   径向渐变
	- 参数(形状  渐变半径  at  圆心位置 , 颜色 )
	- ```` background-image: radial-gradient(circle, red, blue);````
- repeating-radial-gradient( ); 重复径向渐变

		 background: repeating-radial-gradient(
	                    circle,
	                    transparent,
	                    transparent 10px,
	                    black 10px,
	                    black 20px
		);


----------
### CSS3 文本
- overflow-wrap 浏览器为了防止文本溢出，是否可以在单词内换行。
	- normal   默认情况，浏览器只在“空格”或者“半角”的位置换行。
	- break-word 浏览器自行决定在何处“截断”单词。
- word-break 让文本在任何位置换行
	- normal   中文到边界上的汉字换行，英文整个单词换行。
	- break-all  强行“截断”英文单词。
	- keep-all   不准许“截断”单词。如
- white-space  处理元素中的空白符
	- normal  默认值。空白处会被浏览器忽略。只保留正常的空格。
	- pre  文本空白会被浏览器保留。其行为方式类似HTML的<pre>元素效果。
	- pre-line  与normal类似，空白处会被浏览器忽略。不同点是保留换行符
	- pre-wrap 保留空白符序列，换行单独一行显示
	- nowrap  文本不换行，文本在同一行显示，直到遇到<br/>位置。空白处会被浏览器忽略. 常用场景: 广告

![](http://i.imgur.com/ZOAmjf8.jpg)

- text-shadow 文本阴影
	- offset-x   	   X轴偏移量
	- offset-y   	   Y轴偏移量
	- blur-radius      模糊半径
	- color  		  阴影颜色
- text-overflow: ellipsis; 当文本溢出时，省略号显示。
- text-overflow: clip;  仅仅简单的剪裁，不使用省略号。
	- 上述两个属性需要配合  white-space: nowrap; 和 overflow: hidden 一起使用，且容器需要定义宽度。只在块元素内生效。


----------
### CSS盒子问题
- box-sizing
	- 元素设置宽度按 border-box 宽度计算  
	- 按照怪异盒模型的IE标准来判断的
	- **计算方式: 盒子的边框+内边距+内容区**
	- 优点: 设置边框或内边距时不会影响整体的布局.
	
![](http://i.imgur.com/UKSDu51.jpg)

##### 外边距问题
1. 右外边距失效问题: 当父元素水平空间不足,设置右外边距失效,优先保证左外边距效果.
2. 负外边距: 使用负外边会产生一个元素“悬浮”在另一个元素上面的效果。
	- 注意：被覆盖的元素文本内容不会被覆盖！
	
##### 负外边距应用: 右侧固定宽度效果, 左侧自适应(随着浏览器窗口宽度的变化而变化)
	1. 两列都需要设置浮动
	2. 第一列设置100%的宽度,同时设置右侧外边距为负.绝对值等于第二列的宽度
	3. 第一列元素内需要一个正常文档流的块元素承载.设置右侧外边距等于第二列的宽度
	4. 可以给正常文档流设置高度和背景色,用于覆盖第一列的元素.
	
##### BFC应用: 左侧固定宽度，右侧自适应
	1. 第一列设置固定的宽度, 设置左侧浮动
	2. 第二列设置overflow:hidden. 开启BFC,重新计算元素的宽度. 切记不要设置宽度固定值

##### 两边固定宽度,中间自适应 (圣杯布局)
	1. 先做右侧固定,左侧自适应
	2. 再在左侧自适应中正常文档流的div中包裹另外两列
	3. 在大的div内再做左侧固定,右侧自适应
	4. 可以在设置了overflow:hidden的元素内设置背景色和高度.用于覆盖中间的样式
	
##### 制作多列等宽自适应布局
	1. 父元素声明display:table; 并且设置宽度为100%
	2. 布局元素(子元素) display: teble-cell . 宽度自行设定.
	3. 子元素之间的空隙,通过一个正常的div分隔即可.
	4. 如果存在多行需要, 需要包裹一个display: table-row (相当于<tr>). 
	-  tr是不能设置外边距的,如果需要外边距要重新添加一个div设置高度即可.


----------
### CSS3 伸缩盒模型
- 普通浮动布局的通病:
	1. 使用浮动布局,无法实现等高
	2. 元素间顺序调整不能方便的修改DOM的执行顺序
	3. 不能很好控制子元素的位置
- **伸缩盒模型 (flex)特点:**
	1. 被设置flex的元素称为伸缩容器.
	2. 其内的子元素被称为伸缩项目
	3. 伸缩容器中只有主轴和侧轴
	4. 主轴默认从左开始
	5. 侧轴默认从上开始
	
##### display: flex 
- 声明一个元素为伸缩盒模型. (伸缩容器)
- 该元素会独占一行
此时伸缩容器的子元素自动升级为伸缩项目（flex item），伸缩项目的的特点如下，
	1. 伸缩项目默认沿着主轴排列(从主轴start处-end处).
	2. 所有伸缩项目(子元素)与父元素等高.
	3. 伸缩项目(子元素)自动升级为块元素. 
	4. 伸缩项目也可以再次设置为flex，即flex可以互相嵌套。


##### display: inline-flex 
- 行内伸缩容器
- 可以与其他 inline 元素在同一行。
inline-flex 与其他inline元素的对齐特点:
	1. 伸缩容器中有文本内容,以左边出现的第一个文本的基线或其他元素底边对齐
	2. 伸缩容器中没有文本内容也没有伸缩项目时,以伸缩容器底边位于一行和其他元素对齐
	3. 伸缩容器中没有文本内容时,以第一个伸缩项目(子元素)的底边和其他元素对齐

![](http://i.imgur.com/lyqbxIK.jpg)

##### 设置伸缩容器主轴方向排列方式的影响
- flex-direction: row
	- 设置主轴默认横向，star-end 从左开始到右结束
- flex-direction: row-reverse
	- 反向设置主轴横向, star-end 从右开始到左结束
- flex-direction: column
	- 设置主轴纵向, star - end 从上开始到下结束
(主轴顺时针旋转了90度， 同时侧轴逆时针旋转了90度) 
- flex-direction: column -reverse
	- 反向设置主轴纵向. star - end 从下开始到上结束
(主轴顺时针旋转了90度， 同时侧轴逆时针旋转了90度) 

##### 伸缩容器包裹伸缩项目方式
- flex-wrap: nowrap （默认值）
	- 伸缩容器包裹伸缩项目，伸缩项目会被压缩。但不会换行
- **flex-wrap: wrap** 
	- 伸缩容器包裹伸缩项目。水平空间不够，自动换行，保持原来的大小。
	1. 换行后, 行高等于容器的高度除以行数. 
	2. 默认侧轴拉伸基于行高
- flex-wrap: wrap-reverse
	- 伸缩项目自动换行，保持原来的大小。但此时伸缩项目在主轴flex-start和侧轴flex-end处开始排列。

##### 设置伸缩容器主轴有“足够空间”时，贴着主轴起点排列
- justify-content：flex-start   （默认值）
单个伸缩项目在主轴start处排列

- justify-content：flex-end 
单个伸缩项目在主轴的end处排列

- justify-content：center 
单个伸缩项目位于主轴的中间处排列

- justify-content：space-between 
单个伸缩项目沿着主轴均匀分布，伸缩项目会包裹着剩余空间

- justify-content：space-around 
单个伸缩项目沿着主轴均匀分布，剩余空间会包裹着伸缩项目

##### 设置伸缩容器主轴有“足够空间”时，贴着侧轴起点排列
- align-items：stretch 默认值
单个伸缩项目会沿侧轴被拉伸。前提没有设置宽高属性

- align-items：flex-start
单个伸缩项目位于伸缩容器侧轴start处

- align-items：flex-end
单个伸缩项目位于伸缩容器侧轴end处

- align-items：center
单个伸缩项目位于伸缩容器侧轴中部
元素设置固定高度的话, 放在父元素里合适

- align-items：baseline
单个伸缩项目基线最大(行高或者是字体最大)的那个伸缩项目的基线作为所有伸缩项目的对齐基线. 

##### 伸缩项目贴着侧轴多列均匀排列
	1. 当伸缩容器主轴方向空间不足时，伸缩元素flex-wrap: wrap
	2. 伸缩元素有两行及以上
	3. 当出现多行时, 伸缩容器有固定高度. align-items是基于行的star - end 对齐
	4. 提示：使用 justify-content 属性对齐主轴上的各伸缩项目（水平方向）。
	
- align-content: stretch (默认值)
所有伸缩项目在伸缩容器内沿侧轴方向均匀分配铺满屏幕

- align-content: flex-start
所有伸缩项目在侧轴start处,  均匀多列显示

- align-content: flex-end
所有伸缩项目在测轴end处 均匀多列显示

- align-content: center
所有伸缩项目在测轴中间处 均匀多列显示

- align-content: space-between
所有伸缩项目在测轴处多列显示, 伸缩项目会包裹着剩余空间

- align-content: space-around
所有伸缩项目在测轴处多列显示,, 剩余空间会包裹着伸缩项目

##### 设置伸缩项目自己在侧轴的对齐
- align-self: stretch         
默认值, 伸缩项目自己决定垂直方方充满整个高度（前提不能指定高度）

- align-self: flex-start      
伸缩项目自己决定垂直方向起始位置排版

- align-self: flex-end        
伸缩项目自己决定垂直方向结束位置排版

- align-self: center
伸缩项目自己决定垂直方中间靠齐

- align-self: baseline        
伸缩项目自己决定垂直方方向基线对齐

##### 设置伸缩项目沿主轴排序
- order
	- order : 0 ; 默认值. 沿主轴方向正常排序
	- order : 1-x ; 沿主轴方向重新按order设置的数字排序

##### 设置伸缩项目的初始宽度
	width : length 
	flex-basis : length

- flex-basis是指沿着主轴的初始化长度.  与width重叠时它优先生效
- 注意: 当元素设置了初始宽度，且伸缩容器主轴空间不足，伸缩项目会被压缩。

##### 设置伸缩项目分配主轴剩余空间
- flex-grow
	-  flex-grow : 0  默认值 不分配
	-  flex-grow : num 分配的空间大小
- 当伸缩容器主轴空间足够大时，可以分别设置每个伸缩项目如何分配主轴空间

##### 伸缩项目压缩率
- flex-shrink
	- flex-shrink: 1 默认值
	- flex-shrink: 0 不压缩
- 注意: 以上设置会导致伸缩项目有文本的情况下在主轴方向“溢出”

----------

### CSS3 coumn 多列布局
- column-count 规定元素应该被分隔的列数。 
- column-width 规定列的宽度。 
- column-span  规定元素应该横跨的列数。  
- column-rule 设置所有 column-rule-* 属性的简写属性。 
- column-gap 规定列之间的间隔。 
- column-fill  规定列的填充


----------

## 响应式布局和自适应页面
- 自适应页面:
随着屏幕宽度进行调整. 页面结构不会变化(位置的变化, 隐藏或者是显示)

- 响应式页面:
随着屏幕宽度进行调整. 页面结构会发送变化(位置的变化, 隐藏或者是显示)

##### 多媒体选择器
- @media screen 用于监控屏幕
- 多媒体选择器用法: @media 媒体类型 and （媒体特性） ｛样式｝
- width	监控屏幕大小
	- max-width  小于等于 (最大支持)
	- min-widht   大于等于 (最小支持)
- orientation 	监控屏幕显示方式
	- landscape 	横屏
	- portrait 		竖屏
	
- 例子: 当视口的宽度大于等于768px，小于等于1024px时，.box显示蓝色
	 
		@media screen and (min-width: 768px) and (max-width: 1024px){
		         .box{
		             background-color: #00f;
		     }
		  }

- 例子: 当视口横屏时候, box变成蓝色

		 @media screen and (orientation:landscape){
		            .box{
		                background-color: #00f;
		            }
		        }

#### 手机端视口
######布局视口
- 独立且固定的. 每个浏览器厂商都有自己的设置. 
- 设备自己决定屏幕大小. 一般是980px (特殊情况1024px)
- 布局视口的宽度要比屏幕宽出很多
- 多媒体选择器(screen)监听的是布局视口的宽度.
- 可通过 document.documentElement.clientWidth/clientHiehgt; 获取；
- clintWidth 计算宽度不包括滚动条

###### 可视视口
- 用户正在看到的网站的区域，一般视觉视口和布局视口一致。
- 并且它的CSS像素的数量会随着用户缩放而改变。
- 可通过 window.innerWidth/innerHeight 获取;

###### 理想视口
- 使用meta标签控制布局视口, 把布局视口宽度变成设备视口

		<meta name="viewport" 
		      content="width=device-width,
		      initial-scale=1.0, 
		      maximum-scale=1.0, 
		      user-scalable=no">

#### ````<meta name=”viewport” content=””>````
- width ：可视区域宽度，可以是一个具体的数字也可以是device-width。
- height ：可视区域高度，可以是一个具体的数字也可以是device-height。
- inital-scale：页面首次显示时，可视区域的缩放比例，取值1.0页面按实际比列显示，无任何缩放。
- minimun-scale：可视区域最小缩放级别，取值1.0禁止用户缩放至实际尺寸以下。
- maximun-sacle：可视区域最大缩放级别，取值1.0禁止用户放大至实际尺寸以上。
- user-scalable：用户是否可以对页面进行缩放。yes可以缩放，no禁止缩放。

#### CSS3 新的测量单位
- rem 
	- rem = root em
	- 不同的是它是基于html元素（html = root element）计算。
	- 该单位常与媒体查询一起使用。
	- chrome最小只能支持12px (可以用scale()进行更小的缩放字体)
	- 只要改变html的font-size大小，所有基于该元素计算的元素相关尺寸随之等比改变。
- 测量单位选择: 
	- px：在PC端使用，移动端谨慎使用。
	- em：避免嵌套使用，基于自身字体的大小。
	- %：避免嵌套使用,  基于父元素。
	- rem：基于html元素字体大小。注意Chrome不支持12px以下像素。

#### 渐进增强和优雅降级
- 渐进增强：针对低版本浏览器进行构建页面，保证最基本的功能，然后再针对高级浏览器进行效果、交互等改进和追加功能达到更好的用户体验。
- 优雅降级：一开始就构建完整的功能，然后再针对低版本浏览器进行兼容。

#### less
- less提高了CSS的编写效率, 降低了维护成本. 并未减少代码量
###### 主要用途: 
1. **定义一个变量**, 把CSS中通用的样式值提取声明为一个变量

		Less: 
		@theme-color: #0f0;
		body{
		  	background-color:@theme-color;
		}
		/*------------------*/
		CSS:
		body {
		 	 background-color: #00ff00;
		}

2. **定义一个方法**

		Less:
		.btn( ){
		  outline:none;
		  border:none;
		} 
		.btn-default{
		  .btn( );
		}
		/*------------------*/
		CSS:
		.btn-default {
		  outline: none;
		  border: none;
		}

3. **传参数.** 多个参数之间用逗号隔开

		Less:
		.btn-2(@border-width , @outline-width){
		  	border: @border-width;
		  outline:@outline-width;
		}
		.btn-default-2{
		 	 .btn-2(1px , 2px);
		}
		/*------------------*/
		CSS:
		.btn-default-2 {
		  border: 1px;
		  outline: 2px;
		}


4. 嵌套方式

		Less:
		header{
		  p{
		    color: #0b2cff;
		    span{
		      color: #0f0f0f;
		    }
		  }
		
		/*------------------*/
		CSS:
		header p {
		  color: #0b2cff;
		}
		header p span {
		  color: #0f0f0f;
		}