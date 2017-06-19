## FS模块： File System
- FS模块是文件操作的封装，提供了文件的读取、写入、更名、删除、遍历目录等操作
- 任何一个程序都没有能力直接操作磁盘. 引入FS模块和OS操作系统建立连接机制
- 异步读取 在读取文件时,后面的代码就紧接着执行
- 同步读取 需要等待文件读取完成后再执行后面的代码


		var fs = require('fs'); 引入FS模块
		fs.readFile(filename,[encoding],[callback(err,data)]) 异步读文件
		- filename 文件路径(文件夹路径+文件名后缀)
		- callback(err,data) 回调函数 (错误优先机制)
		  * err 错误信息
		  * data 最后读取后的数据(返回是一个二进制字节)
		  	 - 文字: buffter.toString()
		
		fs.readFileSync(filename, [encoding]) 同步读取文件
		- filename 文件路径(文件夹路径+文件名后缀)
		- 可以用try{} catch(err){}接收同步读取的错误信息.防止系统崩溃



		fs.writeFile(file, data[, options], callback) 异步写文件
		- file  文件写在哪
		- data 写的内容
		- [options]  以什么方式写
			* {flag:'a'} //追加内容
			* {flag:'r'} //以读取模式打开文件
			* {flag:'w'} //以写入模式打开文件(默认)
		- callback(err)  回调函数
		
		fs.writeFileSync(file, data[, options]) 同步写文件


----------

**官方已建议采用异步的方式**

1.异步的优点: 后面的代码会尽早的执行, 程序执行效能比较高

2.异步的缺点: 程序员变成思维要求高, 出错容易, 调试困难. 嵌套回调函数可读性低

3.同步的优点: 编程简单,对程序员的思维要求比较低

4.同步的缺点: 代码执行效率较低, 在大规模访问情况下, 整个系统的响应速度慢


- 异步的特点:
 - 具有事件和回调函数
 - 只有事件发生,回调函数才执行
- 同步的特点:
	- 没有回调函数,也没有事件
	- 完全按照行号一行一行的执行

----------

	异步读取
	var fs = require('fs');
	console.log('tb_before');
	
	var path ='./test_content.txt';
	
	fs.readFile(path,function (err,data) {
	    if(err){
	      console.error(err);
	    }else{
	      //console.log(data);
	      //console.log(data.toString());
	      console.log('tb_finish');
	    }
	
	});
	for (var i = 0; i < 999999; i++) {
	
	}
	console.log('tb_after'); //按照回调函数什么时候触发时决定的顺序
	
	
	同步读取: try catch方法用来接收错误信息
	var fs1 = require('fs');
	console.log('yb_before');
	
	try{
	  var path1 ='./test_content.txt';
	  var data = fs1.readFileSync(path1); //同步读文件
	  console.log('yb_finish');
	}
	catch(err){
	  console.error(err);
	}
	console.log('yb_after');

----------


	  //异步实现顺序书写. 嵌套的函数
	  //回调地狱
	  fs.writeFile(path,day1,{flag:'a'},function (err) {
	      if(err){
	        console.error(err);
	      }else{
	        console.log('写完1');
	        fs.writeFile(path,day2,{flag:'a'},function (err) {
	          if(err){
	            console.error(err);
	          }else{
	            console.log('写完了2');
	            fs.writeFile(path,day3,{flag:'a'},function (err) {
	              if(err){
	                console.error(err);
	              }else{
	                console.log('写完了3');
	              }
	            });
	          }
	        });
	      }
	  });

#### /favicon.ico处理
 - 使用 路由分发
 - 使用 读文件
 - 返回 数据

#### log(日志)
 - 作用: 记录系统的行为
 - 俗称: 打log (计算机写文件)
 - 信息存储的位置 : 写入文件中

### 绝对路径/相对路径
 - 文件系统
- 绝对路径: 根目录
- 相对路径: 当前目录为基准
 - http url文件路径
- 绝对路径
	- 从http: 开始的路径
	- 从http url文件路径的根目录开始
- 相对路径:
	-  ./ 表示当前目录下的文件. 当前目录就是当前的文件路径最后一个目录
	- ../ 上一层的目录