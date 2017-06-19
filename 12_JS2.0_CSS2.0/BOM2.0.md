## BOM2.0
### BOM
- ECMAScript 是 JavaScript 的核心，但如果要在 Web 中使用 JavaScript，那么 BOM（浏览器对象模型）则无疑才是真正的核心。
- BOM 提供了很多对象，用于访问浏览器的功能，这些功能与任何网页内容无关。

### window对象
- **BOM 的核心对象是 window，它表示浏览器的一个实例**
- 在浏览器中，window 对象有双重角色
	- 既是通过 JavaScript 访问浏览器窗口的一个接口
	- 又是 ECMAScript 规定的 Global 对象。
- 这意味着在网页中定义的任何一个对象、变量和函数，都以 window 作为其 Global 对象，因此有权访问 isNaN()、isFinite()、parseInt()、parseFloat() 等方法。
- window.navigator.userAgent 可以查看浏览器

### 全局变量和window对象属性的差别
- 全局变量不能通过 delete 运算符删除，而 window 对象上定义的属性可以
- 因为window属性上的configurable: true

### 数据携带
- close() 仅用于关闭浏览器窗口
- open() 可以打开一个新的窗口
	- 该方法可用作跨窗口携带数据
	- opener属性可以把新窗口中的数据传递给旧窗口
	
### 定时器面试题
面试题I

	setTimeout(function () {
      	  console.log(1);
      },1000);
    
      console.log(2);
      
      for (var i=0;i<1000000;i++){
        console.log('a');
      }

      //2   --->  1w*a ---> 1

面试题II


	//同时输出5个5
      for (var i=0;i<5;i++){
        setTimeout(function () {
        	  console.log(i);
        },0)
      }

面试题III


	//一秒之后同时输出5个5
      for (var i=0;i<5;i++){
        setTimeout(function () {
          console.log(i);
        },1000)
      }

面试题IV

	//一秒之后同时输出0,1,2,3,4
      for (var i=0;i<5;i++){
        (function (i) {
        	  setTimeout(function () {
        	  	  console.log(i);
        	  },1000)
        })(i)
      }

面试题V

 	// 每隔一秒输出一个0; 1; 2; 3; 4
     for (var i=0;i<5;i++){
       (function (i) {
         setTimeout(function () {
           console.log(i);
         },1000 * i)
       })(i)
     }

面试题VI

	// 先输出1W个a 同时输出0,1,2,3,4
     for (var i=0;i<5;i++){
       (function (i) {
         setTimeout(function () {
           console.log(i);
         },1000 * i)
       })(i)
     }

     //循环事件肯定大于 5 秒
     for (var i=0;i<10000;i++){
       console.log('a');
     }

面试题VII

	  //直接输出 0,1,2,3,4
      //相当于 console.log(i)
      for (var i=0;i<5;i++){
         setTimeout((function () {
         	  console.log(i);
         })(),1000)
      }

面试题VIII

	//1,4,1w*a,同时出来3,2
	function printing() {
      console.log(1);
      setTimeout(function() { console.log(2); }, 1000);
      setTimeout(function() { console.log(3); }, 0);
      console.log(4);
      
      for(var i=0;i<10000;i++){
        console.log('a');
      }
    }

    printing();
    
- 调用printing()执行函数. 先执行 console.log(1);
- setTimeout告诉异步线程.现在计时延迟1秒后执行然后在执行队列排队等待
- setTimeout告诉异步线程.现在立马执行.然后在执行队列排队等待
- 执行console.log(4);
- 执行for循环
- for执行完成后JS线程空闲了. 异步线程就把执行队列等待的任务扔给JS
- JS立马输出执行队列中的任务

----------
### property属性和attribute属性
- property: 对象上的直接属性
- attribute: DOM对html自定义和预定义属性的封装
- 浏览器和用户实际操作的都是property属性

##### attribute和property的关系
- 非布尔值属性:  property和attribute永远都会实时同步
- 布尔值属性:
	- 未干扰property属性: attribute会同步property
	- 干扰过property属性: attribute不会同步property
- 操作属性的时候, 最好操作property
- 操作布尔值属性时, 尤其是使用jQuery库时, 最好使用prop()方法
- 操作非布尔值属性时, 考虑性能的话可以使用 attr()方法