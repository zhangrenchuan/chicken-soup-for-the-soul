# HTML5
### HTML5简介

HTML5 是 HTML 标准的下一个重要版本，用来替代 HTML 4.01，XHTML 1.0 以及 XHTML 1.1。HTML5 也是一种在万维网上构建和呈现内容的标准。

HTML5 是万维网联盟（W3C）和网页超文本技术工作小组（WHATWG）合作的产物。

HTML5 是近十年来 Web 开发标准最巨大的飞跃。HTML5 并非仅仅用来表示 Web 内容，它将 Web 带入一个成熟的应用平台，在 HTML5 平台上，视频、音频、图象、动画，以及同电脑的交互都被标准化。

#### HTML5 引入了许多新元素和属性帮助我们构建现代化的网站。下面是 HTML5 引入的主要特性：

*   新的语义化元素： 比如 `<header>`，`<footer>` 和 `<section>`。
*   表单 2.0： 改进了 HTML Web 表单，为 `<input>` 标签引入了一些新的属性。
*   持久的本地存储： 为了不通过第三方插件实现。
*   WebSocket： 用于 Web 应用程序的下一代双向通信技术。
*   服务器推送事件： HTML5 引入了从 Web 服务器到 Web 浏览器的事件，也被称作服务器推送事件（SSE）。
*   Canvas： 支持用 JavaScript 以编程的方式进行二维绘图。
*   音频和视频： 在网页中嵌入音频或视频而无需借助第三方插件。
*   地理定位： 用户可以选择与我们的网页共享他们的地理位置。
*   拖放： 把同一网页上的条目从一个位置拖放到另一个位置。

#### HTML5 浏览器支持：

最新版 Apple Safari，Mozilla FireFox 和 Opera 支持大部分 HTML5 特性，IE9 也支持一些 HTML5 的功能。

预装在 iPhones，iPads 和 Android 手机上的手机浏览器都对 HTML5 有良好的支持。

----------

### 自定义属性
- 给程序使用的数据，存储在自定义属性中
- 自定义属性只能存储字符串或数字
- 语法规则
	- 必须以 ````data-````前缀开头
	- 多个英文单词使用 ````-```` 连接
	- ````<div data-demo-test="hello world"></div>````
- Dom使用 ```` dataset```` 操作自定义属性
	- 去掉前缀 ```` data-````
	- 连接符内容采用驼峰命名法
	- ````boxDom.dataset.demoTest````
	
### HTML5 新语义标签
- 新增的语音元素等同于DIV. 可以独占一行.也可以设置宽高
- 没有语义的情况下，就需要是使用DIV了。
- **注意：千万不要为了语义而语义**

![](http://i.imgur.com/avukaOA.jpg)
######  header元素
- header 元素代表“网页”或“section”的页眉。
- 通常包含h1-h6元素或hgroup，作为整个页面或者一个内容块的标题。
- 也可以包裹一节的目录部分，一个搜索框，一个nav，或者任何相关logo。
- 整个页面没有限制header元素的个数，可以拥有多个，可以为每个内容块增加一个header元素
- 注意事项: 
	1. 可以是“网页”或任意“section”的头部部分；
	2. 没有个数限制。
	3. 如果hgroup或h1-h6自己就能工作的很好，那就不要用header。


###### footer元素
- footer元素代表“网页”或“section”的页脚
- 通常含有该节的一些基本信息，譬如：作者，相关文档链接，版权资料。
- 如果footer元素包含了整个节，那么它们就代表附录，索引，提拔，许可协议，标签，类别等一些其他类似信息。
- 注意事项: 
	1. 可以是“网页”或任意“section”的底部部分；
	2. 没有个数限制，除了包裹的内容不一样，其他跟header类似。


###### hgroup元素
- hgroup元素代表“网页”或“section”的标题
- 当元素有多个层级时，该元素可以将h1到h6元素放在其内
- 譬如文章的主标题和副标题的组合
- 注意事项: 
	1. 如果只需要一个h1-h6标签就不用hgroup
	2. 如果有连续多个h1-h6标签就用hgroup
	3. 如果有连续多个标题和其他文章数据，h1-h6标签就用hgroup包住，和其他文章元数据一起放入header标签。


######  nav元素
- nav元素代表页面的导航链接区域。用于定义页面的主要导航部分。
- 用在整个页面主要导航部分上。可以把导航条标签ul放到nav里面


###### article元素
- article代表一个在文档，页面或者网站中自成一体的内容，其目的是为了让开发者独立开发或重用。
- 譬如论坛的帖子，博客上的文章，一篇用户的评论，一个互动的widget小工具。  
- 注意事项: 
	1. 一张页面可以用section划分为简介、文章条目和联系信息。不过在文章内页，最好用article。section不是一般意义上的容器元素，如果想作为样式展示和脚本的便利，可以用div。
	3. article、nav、aside可以理解为特殊的section，所以如果可以用article、nav、aside就不要用section，没实际意义的就用div
	4. article元素可以嵌套article也可以嵌套section. 也可以section 元素嵌套 article 这是一种特殊情况


###### section元素
- section元素代表文档中的“节”或“段”
- “段”可以是指一篇文章里按照主题的分段；“节”可以是指一个页面里的分组。
- section通常还带标题，虽然html5中section会自动给标题h1-h6降级，但是最好手动给他们降级
- 注意事项: 
	1. 一张页面可以用section划分为简介、文章条目和联系信息。不过在文章内页，最好用article。section不是一般意义上的容器元素，如果想作为样式展示和脚本的便利，可以用div。
	2. 表示文档中的节或者段；


###### aside元素 (次要信息)
- aside元素被包含在article元素中作为主要内容的附属信息部分，其中的内容可以是与当前文章有关的相关资料、标签、名词解释等。（特殊的section）
- 在article元素之外使用作为页面或站点全局的附属信息部分。最典型的是侧边栏，其中的内容可以是日志串连，其他组的导航，甚至广告，这些内容相关的页面。
- 注意事项: 
	1. aside在article内表示主要内容的附属信息
	2. 在article之外则可做侧边栏，没有article与之对应，最好不用。
	3. 如果是广告，其他日志链接或者其他分类导航也可以用
	

----------

### HTML5 表单
- <form method="">  请求方式
	- get  	
	- post	
- <label for=""> input提示信息
	- 需要获取input的id属性值关联
	- 点击文字,鼠标光标在输入框内闪烁

##### input 输入类可选属性
- email	  电子邮箱输入框
- tel 		  电话号码输入框
- url		  网页url地址栏输入框
- search     搜索引擎输入框
- number   输入数字
	- max 	最大到
	- min  	最小到
	- step 	以某梯度增加或减少
##### input 选择类可选属性
- range	特定范围内的数值选择器
	- max 	最大到
	- min  	最小到
	- step 	以某梯度增加或减少
- color	颜色选择
- detetime-local	日期选择
	- time
	- date
	- week
	- month

##### 语义化表单新属性
- placeholder  提示用户输入信息
- autocomplete 是否保存用户输入值
	- on 默认值. 自动填充
	- off  关闭自动填充提示
- autofocus 自动获取输入焦点
- novalidate	不对输入进行验证. 填写在from中
- maxlength:" length "控制表单输入项的文本长度
- required	当表单提交时,输入项必须有内容
- pattern	基于正则表达式验证格式. 重要的验证必须放在服务器端
- formaction	在提交按钮中定义一个提交地址. 常用于保存草稿
- formnovalidate	不做表单验证
- DOM操作验证状态方法: setCustomValidity( )  
	- 不符合自定义验证时, 返回给用户一个自定义的字符串内容. 
	- 验证通过时, 可以填写空串. 一定不能写null

----------


### HTML5 history 新方法
- history.pushState ( ) 	增加历史记录
	- state object 数字，字符串，JSON对象
	- title（所有浏览器暂不支持）
	- URL [可选]显示在地址栏的网页地址
- history.replaceState( )     修改历史记录
	- 把当前的历史记录（history entry ）替换成新的历史记录
	- 参数同pushState
- window.onpopstate 当窗口历史记录改变时运行的脚本
	-onpopstate触发时机：相同文档中，两个历史记录前进或后退切换时。

----------

### HTML5 离线存储 API
##### Cookie存储的特点
	1.cookie由服务器创建，第一次响应后，记录在浏览器
	2.每次请求，cookie都会发动到服务器
	3.每次响应，cookie都会推送到浏览器
	4.在浏览器读取cookie比较繁琐
	5.cookie容量小，只有4kb
	- cookie 缺点: 需要在客户端和服务器端来回地传送，繁琐且消耗带宽；

##### Storage存储 : sessionStorage / localStorage
- 数据生命周期：
	- sessionStorage  数据创建到浏览器页签关闭
	- localStorage    数据创建到用户手动清除，或者使用clear(), removeItem(key)删除
- 数据共享：
	- sessionStorage 条件：同一个浏览器页签
	- localStorage   条件：相同域名（协议，域名，端口）的不同网址
- 数据使用场景：
	- 频繁操作且安全性不高的数据
- 可存储的数据格式：
	1. 数字
	2. 字符串
	3. JSON对象，需要使用 JSON.stringify(JSON对象)把其转换成字符串再存储。获取后再调用JSON.parse(JSON的字符串)转成JSON对象再使用。
- 优点:
	- sessionStorage / localStorage 优点: 保存在服务器端. 存储结构化方便提取


###### sessionStorage / localStorage 属性
- setItem("key", "value");   
	- 增加一个数据
- getItem('key') 
	- 获取对应的value值
- removeItem("key");  
	- 删除一个数据
- clear(); 
	- 清除所有
- length
	- 获取数据长度
- key(num)                   
	- 获取指定索引位的key值

![](http://i.imgur.com/jat4BB1.jpg)

----------
### HTML 音视频处理
#### 视频基础内容
**目前实现网页视频播放的技术 - Flash**

*   Flash并不是浏览器原生支持(第三方组件)
*   Flash的性能并不好
*   移动端不支持Flash技术

**HTML 5 提供的视频处理技术 - `<video>`**

*   提供了相对应的基本处理方式
*   提供了高级编程自定义方式

**`<video>`元素所支持的视频格式**

*   MP4格式：视频文件扩展名为".mp4"
*   OGG格式：视频文件扩展名为".ogv"
*   WEBM格式：视频文件扩展名为:".webm"
    *   是由Google公司推出的(最初Chrome并不支持)
    *   是目前唯一一个支持超高清的视频格式

#### 如何使用`<video>`元素

**引入单个视频格式**

	<video src="视频文件的路径" autoplay>
	    浏览器不支持的提示内容
	</video>


*   autoplay属性：自动播放视频
*   width属性：设置视频的宽度
*   height属性：设置视频的高度
*   style属性：设置CSS样式
*   class属性：设置CSS样式


		<video src="../DATA/oceans-clip.mp4" autoplay width="640px" height="400px" style="background:black;">
		    非常抱歉,你的浏览器不支持该视频!
		</video>

**引入多个视频格式**


	<video autoplay>
	    <source src="视频文件的路径" />
	    <source src="视频文件的路径" />
	    <source src="视频文件的路径" />
	    浏览器不支持的提示内容
	</video>




	<!-- 解决了浏览器对视频格式的兼容问题 -->
	<video autoplay>
	    <!--
	        <source>元素
	        * 引入视频文件(一个<video>元素允许包含多个<source>)
	    -->
	    <source src="../DATA/oceans-clip.mp4" />
	    <source src="../DATA/oceans-clip.ogv" />
	    <source src="../DATA/oceans-clip.webm" />
	</video>



#### `<video>`元素的属性

*   autoplay属性：自动播放
*   controls属性：提供控制面板


		<video src="../DATA/oceans-clip.mp4" controls></video>



*   loop属性：循环播放


		<video src="../DATA/oceans-clip.mp4" autoplay loop></video>


*   poster属性：播放之前实现一张图片

		<video src="../DATA/oceans-clip.mp4" controls poster="../DATA/oceans-clip.png"></video>

*   preload属性：预加载视频
    *   none：不预加载
    *   auto：默认值,尽快预加载
    *   metadata：预加载除视频之外的内容(宽度、高度等)

#### 视频高级编程

**事件**

*   play：视频播放时触发
*   pause：视频暂停时触发
*   ended：视频播放结束时触发
*   error：视频播放错误时触发


**方法**

*   play( )：用于播放视频
*   pause( )：用于暂停视频
*   load( )：用于加载视频
*   canPlayType( )：判断当前浏览器是否支持当前视频格式



**属性**

*   paused：如果视频为暂停或未播放时,返回true
*   ended：如果视频播放完毕时,返回true
*   duration：返回当前视频的时长
*   currentTime：获取或设置视频的当前位置


----------

##### 音频基础内容

**目前音频处理技术**

*   Flash技术也可以音频处理
*   Media Player播放器允许嵌入在网页中

**HTML 5提供的音频处理 - `<audio>`**

*   浏览器原生支持
*   性能很好
*   移动端支持

**`<audio>`元素支持的音频格式**

*   mp3 - 音频文件的扩展名为".mp3"
*   ogg
*   wav

#### 如何使用`<audio>`元素

**引入单个音频格式**


	<audio src="音频文件的路径" autoplay>
	    浏览器不支持的提示内容
	</audio>



**引入多个音频格式**

	
	<audio autoplay>
	    <source src="音频文件的路径" />
	    <source src="音频文件的路径" />
	    <source src="音频文件的路径" />
	    浏览器不支持的提示内容
	</audio>



#### `<audio>`元素的特有属性

*   autoplay属性：自动播放
*   controls属性：提供控制面板
*   loop属性：循环播放
*   preload属性：预加载视频
    *   none：不预加载
    *   auto：默认值,尽快预加载
    *   metadata：预加载除视频之外的内容(宽度、高度等)

#### `<audio>`元素的高级编程

**事件**

*   play：视频播放时触发
*   pause：视频暂停时触发
*   ended：视频播放结束时触发
*   error：视频播放错误时触发

**方法**

*   play( )：用于播放视频
*   pause( )：用于暂停视频
*   load( )：用于加载视频
*   canPlayType( )：判断当前浏览器是否支持当前视频格式

**属性**

*   paused：如果视频为暂停或未播放时,返回true
*   ended：如果视频播放完毕时,返回true
*   duration：返回当前视频的时长
*   currentTime：获取或设置视频的当前位置