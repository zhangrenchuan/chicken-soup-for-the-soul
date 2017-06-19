##  Web Workers API
- 提供了js分线程的实现
- **分线程主要用来处理长时间的工作且不占用主线程的空间和时间**


		Worker: 构造函数, 加载分线程执行的js文件
		Worker.prototype.onmessage: 用于接收另一个线程的回调函数(当接收消息时,回调函数执行)
		Worker.prototype.postMessage: 向另一个线程发送消息
		分线程里的this不是window而是[object DedicatedWorkerGlobalScope]


- 缺点: 
  * worker内代码不能操作DOM(更新UI)
  * 不能跨域加载JS
  * 不是每个浏览器都支持这个新特性

**分线程设计出来是为了处理长时间的工作. 不是为了更新界面**

	  //创建Worker实例
	  var worker = new Worker('worker1.js');
	
	  //通过主线程向分线程的js发送消息(数据)
	  var msg = 'abc';
	  worker.postMessage(msg);
	  console.log('主线程向分线程发送数据 : ',msg);
	
	
	  //绑定接收返回消息的监听回调
	  worker.onmessage = function (e) {
	  	  var result = e.data;
	    console.log('主线程接收到分线程返回的数据 : ',result);
	  }


	  //1. 接收数据
	  var onmessage = function (e) {
	  var data = e.data;
	  console.log('分线程接收到主线程发送的数据 : ',data);
	
	  //2. 处理数据
	  data = data.toUpperCase();
	
	  //3. 返回数据
	  postMessage(data);
	  console.log('分线程向主线程返回数据 : ',data);
	
	  //alert not defined  分线程里不可以更新界面的
	  };
	
	主线程向分线程发送数据: abc
	分线程接收到主线程发送的数据: abc
	
	分线程向主线程返回数据: ABC
	主线程接收到分线程返回的数据: ABC
