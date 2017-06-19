## jQuery  AJXA

#### $.ajax({})

	$.ajax({
		type : 请求方法
		url: 文件路径: url路由
		data: 查询字符串(字符串或定义对象都可以)
		success:function(msg){
			成功的话返回的数据 readyState=4&&status=200
	 	}
		error: funciton(err){
			consolo.log(err)
		}
	})


#### $.get()  发送get请求
参数:

- url  文件路径  路由
- data 查询字符串(Key/value)
- 回调函数 (成功接收到信息的时候调用)
- 控制返回内容数据的格式 xml, html, script, json, text, _default


#### $.post()   发送post请求
参数:

- url  文件路径  路由
- data 查询字符串(Key/value)
- 回调函数 (成功接收到信息的时候调用)
- 控制返回内容数据的格式 xml, html, script, json, text, _default


#### $.getJSON() 发送get请求载入JSON格式数据
参数:

- url  文件路径  路由
- data 查询字符串(Key/value)
- 回调函数 (成功接收到信息的时候调用)