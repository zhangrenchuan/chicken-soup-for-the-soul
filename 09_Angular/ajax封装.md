# ajax封装

## 先弄懂这件事

这篇介绍如何把 AngularJS 里的请求代码封装起来。把地址和请求细节放进服务，控制器就可以专心处理页面数据。

## 笔记与示例

## AJAX 封装

- $http({}) GET请求
	- 第一个参数:请求方式method:'get'
	- 第二个参数: 路由路径url
	- 第三个参数: 请求内容 params:{}
		- 注:post请求对象用data:{}接收
	- 调用success(function(data){})
	- 调用error(function(error){}) 
- $http({}) POST请求
	- 第一个参数:请求方式method:'post'
	- 第二个参数:路由路径url
	- 第三个参数:请求头
		- headers: {'Content-Type': 'application/x-www-form-urlencoded'}
	- 第四个参数:请求内容使用拼串形式
		- data:'username=wukong'+'&'+'age=38'
	- 调用success(function(data){})
	- 调用error(function(error){})
- $http.get()
	- 参数: 请求路由路径
	- 请求内容写在路由路径的 ? 后面
	- ````$http.get('http://localhost:4000/angular_node/get?username=wukong$age=4')````
	- 再调用success(function(data){}) 
- $http.post()
	- 参数: 请求路由路径
	- 请求内容写在对象中
	- ````$http.post('/angular_node/post',{username:'wukong',age:38})````
	- 再调用success(function(data){}) 
- $http.jonsp()
	- 参数: 请求路由路径
	- 需要在后面写 ?callback=JSON_CALLBACK
	- &符号后写请求的内容
	- ````$http.jsonp('http://localhost:4000/angular_node/jsonp?callback=JSON_CALLBACK&username=wukong')````
	- 再调用success(function(data){})
