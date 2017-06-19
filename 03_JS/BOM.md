# BOM
## Browser Object Model 
- 浏览器对象模型
- BOM对象都是作为window对象的属性保存的
- window 代表浏览器窗口
- navigator 代表浏览器的信息.可用来识别浏览器
- history 浏览器的历史记录
- location 代表浏览器的地址栏信息
- screen 用户的显示器信息

#### window 
- window.innerHeight
	 - 浏览器窗口的内部高度(包括滚动条)
- window.innerWidth 
	 - 浏览器窗口的内部宽度(包括滚动条)
- window.outerWidth
	- 整个浏览器的宽度
- window.outerHeight
	- 整个浏览器的高度
- window.pageXoffset
	- 返回当前页面相对于窗口显示区左上角X的位置
- window.pageYoffset
	- 返回当前页面相对于窗口显示区左上角Y的位置
- window.screenLeft
	- 返回相对于屏幕窗口的x坐标
- window.screenTop
	- 返回相对于屏幕窗口的y坐标
- document.documentElement.clientHeight
	-  获取可见内容的高度(不包括滚动条边框) 
- document.documentElement.clientWidth
	-  获取元素内容区宽度(不包括滚动条边框)
- window.open() 
	- 打开新窗口
- window.close() 
	- 关闭当前窗口
- window.moveTo() 
	- 移动当前窗口
- window.resizeTo() 
	- 调整当前窗口的尺寸
	
![](http://i.imgur.com/NqKJbKn.gif)

#### navigator
- 判断浏览器的信息
- 由于历史原因navigator大部分属性都不能用来识别浏览器了
- 仅剩的属性userAgent可判断浏览器版本

		//通过userAgent来判断浏览器的信息
		if(/firefox/i.test(ua)){
			alert("火狐浏览器");
		}else if(/edge/i.test(ua)){
			alert("Edge浏览器")
		}else if(/chrome/i.test(ua)){
			alert("chrome浏览器");
		}else if(/msie/i.test(ua)){
			alert("ie11以下浏览器");
		}else if("ActiveXObject" in window){
			alert("ie11浏览器");
		}

#### history 
- 该对象代表用户的历史记录
- 由于隐私原因该对象只能控制浏览器向前或向后翻页
- 只可访问当次的历史记录

		//history.length 可以获取当次访问历史记录的数量
		
		//history.back(); 可以回退到上一个页面.功能相当于浏览器的后退按钮
		  
		//history.forward();可以跳转到下一个页面.功能相当于浏览器的前进按钮
		  
		//history.go();可以跳转到指定的页面.
		//需要一个整数作为参数.将会跳转指定数量的页面
		  

#### location
- 表示浏览器地址栏的信息
- 直接输出location会返回当前页面的地址
- 直接修改location的值会使浏览器跳转到修改的地址

		location.assign(); 可以用来跳转到指定的页面.
		  - 需要一个路径作为参数.将会跳转到该路径
		  - 会生成历史记录
		          
		location.replace(); 也可以跳转到指定页面
		  - 同样需要一个地址作为参数
		  - 用法和assign()一样
		  - 不会生成历史记录.不可以回退
		        
		location.reload(true); 刷新当前页面
		  - 在该方法中可以传递一个true.则会强制清空缓存
		        

#### 定时调用定时器
- 每间隔一段时间就调用指定的函数一次
- 可执行多次
- **setInterval()开启一个定时**
- 参数:
	- 回调函数.
	- 函数调用相隔时间的毫秒数
- 返回值:
	- 会返回一个number类型的值
	- 该number就是定时器的标识.需要有一个变量来接收
- **clearInterval() 关闭定时器**
- 参数: 定时器的标识

#### 延时调用定时器
- 函数不马上执行,而是过一段时间以后再执行
- 只执行一次
- **setTimeout()来设置延时调用**
- 参数:
	- 回调函数
	- 延迟执行的毫秒数
- **clearTimeout() 关闭延时调用定时器**


#### 弹窗
- alert() 警告框
- confirm() 确认框 (含有确认和取消按钮)
- prompt() 提示输入框
