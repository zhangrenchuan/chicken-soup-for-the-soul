## 环境配置

**命令行**

- 呼出命令行
	- win + R -->  cmd
- 盘符跳转
	- 盘符名 + 冒号
- 在文件夹中跳转
	- cd + 空格 + 文件夹名称
- tab键 
	- 自动补全
- 运行文件
	- 输入文件名回车即可
- 查看当前目录下的文件列表
	- dir
- 清屏
	- cls
- 打印环境变量
	- path



**环境变量核心思想**

- 帮助用户查找文件
- 整个文件的绝对路径(从盘符起) 需要放进字符串里

**NodeJs命令行**

- node -v  
	- 查看版本号
- node -h
	- 帮助文件
- node 文件路径
	- 读取文件内容
- node script.js
	- 用node软件去执行某一个js文件
- IP地址
 - http://127.0.0.1:端口号  回环地址
 - localhost  本机 
 - 本机IPv4地址



 **五步创建服务器**

1.http 模块对象

2.createServer

3.server 监听(.listen申请端口号1024-65535)

4.回调函数: 1. 访问事件 createServer

5.回调函数: 2. 端口监听事件 listen


	  //1.引入http包
	  //require是一个函数. 返回值是一个对象
	  var http = require('http');
	
	  //2.访问的处理逻辑
	  function serverHandler(request,response) {
	      //request  请求数据
	      //response 返回数据
	    response.end('hello world')
	  }
	
	  //3.创建服务器  createServer里注册访问处理的逻辑
	  //每当有请求,回调函数就执行一次
	  var server = http.createServer(serverHandler);
	
	  //4.用浏览器访问监听的端口号
	  //listen 向操作系统申请端口号  1024-65535之间的
	  //申请成功的时候 创建回调函数 弹出提示
	  function linstenHandler() {
	      console.log('申请成功');
	  }
	  server.listen(3000,linstenHandler);
	  //http://127.0.0.1:3000  回环地址
	  //192.168.1.6:3000 本机IPv4地址


**常见错误**

- EADDRINUSE  端口号被占用
- E
- ADDR
- IN
- USE

解决办法: 1. 杀死进程. 2.修改端口号

绝对路径: 从盘符根目录开始 C:/

相对路径: 相当于当前文件夹(./ 当前目录)(../ 上一级目录)
程序 - 死人.. 进程 - 活人

----------

## 全局对象与工具
#### 2-1.node global
全局空间. 避免污染全局空间

#### 2-2.console
- console.log('log'); 
- console.info('info');
- console.error('error');
- console.warn('warn'); 
	- log info 正常显示信息
	- error 出错信息 红色显示
	- warn 警告信息 红色显示
	- log info互为别名. error warn互为别名
- console.trace(); 打印调用堆栈追踪函数的调用轨迹
- console.time(); / console.timeEnd();
	- 计时器. 可以计时中间执行代码的时间. 传入一个字符串接收时间

#### 2-3. 定时器
- setTimeout   延迟执行定时器
	- clearTimeout();
- setInterval   反复循环定时器
	- clearInterval();
- setImmediate(callback[, arg][, ...]) 立即执行定时器
	- clearImmediate()