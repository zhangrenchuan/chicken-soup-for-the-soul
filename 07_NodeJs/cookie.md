## Cookie
#### cookie 作用
1.存储用户个性化的数据

2.把数据存储在浏览器里

#### cookie本质
1.本质是一个存储在浏览器的文本

2.随着http请求自动传递给服务器

#### cookie生命周期
session时间:  浏览器关闭就被删除

绝对时间: 超过设定的时间就被删除

#### cookie 生成
##### 服务器端操作cookie
1. 生成
	- 响应报文中加一个首部字段. 添加cookie
	- res.cookie('name','value')
2. 删除
	- res.clearCookie('name');

#### 浏览器操作cookie
1.引入jQuery框架和 cookie插件
````
	<script src="./jquery-1.10.1.js" type="text/javascript"></script>
````
````
	<script src="./jquery.cookie.js" type="text/javascript"></script>
````

2.设置cookie

````
	$.cookie('name','value')
````

3.修改cookie

````
	$.cookie('name','new value')
````

4.查询cookie

````
	var result = $.cookie('name')
````

````
	console.log(result)
````

5.本地cookie显示在input标签中
````
$('#userName').val(result); val有值代表添加 无值代表读取
````

6.删除cookie

````
$.removeCookie('name')
````


#### cookie用户名自动填充
1.当用户登录成功之后, 服务器向浏览器生成 cookie

	- 名: THE_LAST_LOGIN
	- 值: 用户名

2.浏览器读取cookie. 把cookie的值填充到input标签中

#### cookie优缺点
缺点:

1. 对于用户来说可以直接看到  不安全
2. 浏览器用户可以删除或禁用cookie
3. 很多网站滥用cookie导致用户反感
4. 浪费带宽  每请求一次页面就要发送一次
5. 大小受限  4kb
6. 使用不便 需要使用插件或者封装方法

优点:

1. 减少服务器的cup和内存资源的消耗. 
2. 在各种应用场景中都可以用. 集成在http协议里了


----------

### 题目：sessionStorage, localStorage, 和 cookie 的区别和优缺点
**1.描述 sessionStorage 和 localStorage**

html5中新提供的Web Storage 包括了两种存储方式：sessionStorage 和 localStorage。

- 区别
 - sessionStorage 用于本地存储一次会话的数据. 会话结束后数据也随之销毁		
 - localStorage 用于持久化的本地存储。除非主动删除数据，否则数据是永不过期的
- 共同点
  - localStorage和sessionStorage都具有相同的操作方法
  - 例如setItem、getItem和removeItem等
  - 都有兼容性问题


----------

**2.web storage 和 cookie 的区别**

Web Storage的概念和 cookie 相似，区别是它是为了更大容量存储设计的。

**cookie的缺点：**

- Cookie的**大小**是受限的  大概4kb
- 每次请求一个新的页面的时候Cookie都会被发送过去，无形中浪费了**带宽**
- cookie还需要指定作用域，不可以跨域调用
- cookie使用不方便。
	- Web Storage拥有setItem,getItem,removeItem,clear等方法。
	- cookie需要前端开发者自己封装setCookie，getCookie或者使用插件

**cookie的优势：**

- cookie也是不可以或缺的：
	- cookie的作用是与服务器进行交互，作为**HTTP规范**的一部分而存在 
	- Web Storage仅仅是为了在本地“存储”数据而生
- **兼容性**
	- cookie年头久，浏览器支持性很好
	- web storage 较新，只有比较新的浏览器才支持
