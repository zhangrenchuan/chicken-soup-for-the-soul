## HTTP服务器建立

### 1.创建：

		var http = require('http') 引入http包
		var server = http.createServer(callback);
		createServer 有一个返回值：server (类型 http.Server)
		回调函数callback 有两个参数：
		  	1.request:请求数据 类型 http.IncomingMessage
		  	2.response:响应返回数据 类型 http.ServerResponse

### 2.监听

	server.listen(port, [host], [backlog], [callback]);
	server监听来自客户端的请求。
	参数：
	    1.port:监听端口号(必须)
	    2.host:指定监听的地址 可选
	    3.backlog:等待队列中客户端的最大连接数据量，默认511，超过这个数据量之后的请求服务器会拒绝连接
	    4.当‘listening’事件触发后，执行回调函数

### 3.关闭

	server.close();
	关闭服务器，再关闭后，不能再提供服务

### 4.实例  

	var http = require('http');
	
	var server = http.createServer(function (request,response) {
	    response.end('hello world')
	  }).listen(3000,function () {
	    console.log('成功申请');
	  });
	
	  setTimeout(function () {
	      server.close(); //关闭服务器
	  }, 5000);


----------

## request  请求数据 HTTP请求

- url 域名
	-  /  表示根目录
- method 请求方法
	- get    请求数据内容都在url中. 请求体没有
	- post  默认传递较多数据.内容在请求体中

## response 返回数据 HTTP响应

**一次性统一设置响应头信息,必须写在发送数据之前**

- **writeHead**(statusCode, [reasonPhrase], [headers]) 
	- statusCode 状态码
	- reasonPhrase 状态码说明
	- headers 对象{ }
	- 'content-type' : //响应类型
	  * 'text/html'  以html格式解析
	  * 'text/plain' 以原始文本解析
	- 'content-length': //响应体长度
	- 'set-cookie' : ['name' = 'zrc'] //设置cookie

````
例子: res.writeHead(200,'OK',{ 'content-Type' :'text/html' }); 
````

**单独设置响应头信息**

- **setHeader**(name,value)  添加或修改响应头信息
	- name 响应头名
	- value 响应头对应的值
	例如 - 'content-type' ,
	* 'text/html'  以html格式解析
	* 'text/plain' 以原始文本解析
- getHeader(name)  获取查找某个响应头信息
- removeHeader(name)  删除响应头某个信息
- statusCode  单独设置状态码

````
例子: res.setHeader('content-Type','text/html');
````

- **write**  发送数据但不断开连接
	- 必须在end之前调用
	- 可调用多次
	- Error: write after end (在end后执行了但是报错了)
- **end** 发送数据同时断开连接
	- 必须调用,否则信息会一直等待
	- 只传输一次
	- 没有参数直接断开连接
	- 多个end执行了但并不一定出来想象的效果
