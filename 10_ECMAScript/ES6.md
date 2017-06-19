## ECMAScript 6
#### let 关键字
- 使用let声明变量. 与var类似
- 特点:
    - 在块作用域内有效
    - 不能重复声明
    - 不会预处理,不存在变量提升
- 应用:
    - 循环遍历加监听 
    

#### const 关键字
- 使用const定义常量
- 特点:
    - 不可修改
- 应用:
    - 保存不需要改变的数据


#### 变量的解构与赋值
- 从对象或数组中提取数据,并给变量(多个)同时赋值
- 注意点:
    - 对象的结构赋值根据对应的属性名赋值
    - 数组的结构赋值根据对应的下标索引值赋值
- 用途: 
    - 给多个形参赋值
- 例子:

		let {n, a} = {n:'tom', a:12}
		console.log(n,a) //tom,12

	    let arr = [123,'abc',true];
	    let [a,b,c] = arr; 
	    console.log(a,b,c); //123,'abc',true

	    let obj = {name:'kobe',age:39}
		function person({name,age}) {
		  	 console.log(name,age);
		}
	    person(obj)  //kobe 39


#### 模版字符串
- 简化字符串拼接的过程
- 用法
    - 需要拼接的字符串使用 `` 
    - 要变化的部分使用 ${} 定义
- 例子:
	
		let obj = {name:'kobe',age:39}
		//普通字符串拼串
  		console.log('我叫:' + obj.name + ', 我的年龄是:' + obj.age);
		//模版字符串拼接
	    console.log(`我叫:${obj.name},我的年龄是:${obj.age}`);


#### 简化对象的写法
- 省略同名的属性值
- 省略方法的 function

		//普通写法
		let obj = {
		  x : x,
		  getPoint:function () {
		     return this.x 
		  }
	    }

		//简化写法
		let x = 3
		let obj = {
		   x ,
		   getPoint(){
			 return this.x
		  }
		}

---


#### 箭头函数
- 多用来定义回调函数(匿名函数)
- () => {}
- 箭头左边() 放置参数
- 箭头右边{} 函数体

###### 箭头函数特点
- 写法简洁
- 函数体不用大括号时默认自动return返回结果
- 函数体如果有多个语句,需要用{}包裹.要手动返回结果.否则会返回undefined
- 箭头函数没有它自己的this值
- 箭头函数的this不是调用的时候决定的，箭头函数内的this值继承自外围作用域
- **箭头函数里写的 this 其实是包含该箭头函数最近的一个 function 上下文中的 this（如果没有最近的 function，就是全局window）**
- 箭头函数的this查找向作用域的变量查找一样，一层一层的往上找，直到找到window对象

###### 箭头函数基本语法
- 没有参数: ````() => console.log('xxxx')````
- 一个参数: ````i => i+2````
- 多个参数: ````let fun2 = (x,y) => x+y````
- 多个语句: ````let fun3 = (x,y) => {console.log(x,y);return x + y}````


---

#### 三点式运算符
- 替代形参位置. 必须写在形参最后一位
- 遍历实参,赋值到形参里并组成参数数组(可使用数组的方法)
- 可插入数组
- 可遍历字符串返回各个字符

		function fun(...values) {
		  	console.log(values);
		  	values.forEach(function (item,index) {
		    console.log(item,index);
		  	})
		}
	    fun(1,2,3) //[1,2,3]

		let arr = [1,2,3,4,5]
		let str = 'cha';
		let arr1 = ['abc',...arr,...str,'qwe']
		console.log(arr1); 
		["abc", 2, 3, 4, 5, 6, "c", "h", "a", "qwe"]


#### 形参默认值
- 当不传参数的时候默认使用形参里的默认值
- 直接给形参赋值

		  function Point(x=0,y=0) {
		    this.x = x;
		    this.y = y;
		  }
		  let p = new Point()
		  console.log(p);  //x=0,y=0
		  let p1 = new Point1(25,36)
		  console.log(p1); //x=25,y=36

#### class类的继承
1. 通过class定义类
2. 在类中通过constructor定义构造方法
3. 通过new来创建类的实例
4. 通过extends来实现父类对子类的继承
5. 通过super调用父类的构造方法
	- 可重写从父类中继承的一般方法(子类自身重新定义)

例子:
		
	 //class定义类
	  class Person {
	    //通过constructor定义构造方法
	    constructor(name,age){
	      this.name = name;
	      this.age = age;
	      this.showName = function () {
	      	  return this.name
	      }
	    }
	    showName (){ //定义一般的方法
	      console.log(this.name);
	    }
	  }
	  let person = new Person('wukong',39);
	  console.log(person,person.showName()); //
	
	 
	  //定义一个子类 通过extends来实现父类对子类的继承
	  class starPerson extends Person{
	    constructor(name,age,salary){
	      super(name,age); //super调用父类的构造方法
	      this.salary = salary;
	    }
	    showName(){ //父类的方法重写(在子类自身定义方法)
	      console.log(this.name,this.age,this.salary);
	    }
	  }
	  let p2 = new starPerson('sun',12,1235453);
	  console.log(p2); 
	  p2.showName() 

----------

#### promise 对象
- 代表了未来将要发生的事件(通常是一个异步操作)
- promise对象, 可以将异步操作以同步的流程表达出来, 避免了层层嵌套的回调地狱函数
- ES6的Promise是一个构造函数, 用来生成promise实例
- promise对象的3个状态
	- pending: 初始化状态
  	- fullfilled: 成功状态
  	- rejected: 失败状态
- 应用:
	- 使用promise实现超时处理
	- 使用promise封装处理ajax请求
###### promise基本步骤
- 创建promise对象
	- 此时初始化promise对象的状态为pending状态(初始化状态)
	- ````let promise = new Promise((resolve, reject) => {})````
	- 回调函数第一个参数:成功的状态
		- 成功接收到数据调用resolve().参数是接收的数据 
		- 此时修改promise对象的状态为fullfilled状态(成功状态)
	- 回调函数第二个参数:失败的状态
		- 失败调用reject().参数是返回的失败信息
		- 此时修改promise对象的状态为rejected状态(失败状态)
- 调用promise的方法then()
	- 第一个参数: 成功时的回调函数 (参数是接收的数据)
	- 第二个参数: 失败时的回调函数 (参数是接收失败的信息)

![](http://i.imgur.com/4DJ5anw.png)

实例:

	  function getNews(url) {
	  	  //创建promise对象并初始化promise状态为 pending
	    let promise = new Promise((resolve,reject)=>{
	        //启动异步任务
	      let request = new XMLHttpRequest();
	      request.onreadystatechange = function () {
	        if(request.readyState === 4){
	          if(request.status === 200){
	            let news = request.response;
	            resolve(news); //修改状态为成功
	          }else{
	            reject('请求失败');
	          }
	        }
	      };
	      request.responseType = 'json'; //设置返回的数据类型
	
	      request.open("GET", url); //规定请求的方法并创建链接
	
	      request.send(); //发送请求
	    });
	    return promise;
	  }
	
	  getNews('http://localhost:3000/news?id=1')
	      .then((data)=>{
	        document.write(JSON.stringify(data));
	        return getNews('http://localhost:3000' + data.commentsUrl)
	      },(error)=>{
	        console.log(error);
	      })
	      .then((comments)=>{
	        document.write('<br><br><br>'+JSON.stringify(comments));
	      },(error)=>{
	        console.log(error);
	      })



----------
### ES6其他特性
#### 字符串String扩展
- includes(str) : 判断是否包含指定的字符串
- startsWith(str) : 判断是否以指定字符串开头
- endsWith(str) : 判断是否以指定字符串结尾
- repeat(count) : 重复指定次数

#### 数值Number扩展
- 二进制与八进制数值表示法: 二进制用0b, 八进制用0o
- Number.isFinite(num) : 判断是否是 有限大的数
- Number.isNaN(num) : 判断是否是NaN
- Number.isInteger(num) : 判断是否是整数
- Number.parseInt(str) : 将字符串转换为对应的数值
	- 忽略字符串中的非数字字符
	- 如果第一个字符为非数字返回NaN
- Math.trunc(num) : 直接去除小数部分

#### 数组Array扩展
- Array.from() : 将伪数组对象或可遍历对象转换为真数组
	- 真数组可使用forEach()进行遍历
- Array.of() : 将一系列值转换成数组
	- ````let arr = Array.of(1,'阿斯顿',2,true);````
	- ````[1,'阿斯顿',2,true]````
- find(function(item, index, arr){}) : 找出第一个满足条件返回true的元素
- findIndex(function(item, index, arr){}) : 找出第一个满足条件返回true的元素下标

		  let arr1 = [1,3,5,2,6,7]
		  let result = arr1.find(function (item,index) {
		  	  return item > 3
		  });
		  console.log(result); //5
		
		  let result1 = arr1.findIndex(function (item,index) {
		    return item > 3
		  });
		  console.log(result1); //2

#### 对象Object扩展
- Object.is(value1, value2)
	- 判断两个数据是否完全相等
	- 只要长的一模一样就返回true

			console.log(Object.is(NaN,NaN)); //true
	  	    console.log(Object.is(0,-0));//false
	  		console.log(Object.is(-0,-0));//true

- Object.assign(target, source1, source2..)
	- 将源对象的属性复制到目标对象上
	- 第一个参数: 准备要复制的对象
	- 第二个参数: 被复制的对象

###### 可直接操作````__proto__````隐式原型属性
- 使某一对象的隐式原型属性指向另一个对象
- 则可以从隐式原型属性上访问到另一个对象的所有属性

		let obj = {name:'kobe',age:39}
		let obj1 = {};
		obj1.__proto__ = obj;
		console.log(obj1); //__proto__ age:39,name:'kobe'

----------

####  Set()和Map()数据结构
##### Set容器 : 无序不可重复的多个value的集合体 
- 主要功能: 数组去重
- 语法: ````let set = new Set([1,2,3,4,5,5,5]);````
- Set容器的其他方法
	- add(value) 添加值
    * delete(value) 删除值
    * has(value) 判断是否有该值(返回值是布尔值)
    * clear() 清除
    * size 长度

##### Map容器 : 无序的不重复的多个key-value的集合体 
- 该容器仅支持二维数组
- 前面的值是key值. 后面的值是value值
- 语法: ````let map = new Map([['abc',12]]);````
- 输出: ````Map(1) {"abc" => 12}````
- Map容器的其他方法
  * set(key, value) 添加key-value键值对
  * get(key) 获取key对应的value值
  * delete(key) 删除值
  * has(key) 判断是否有该值(返回值是布尔值)
  * clear() 清除
  * size 一个二维数组是1个长度

#### for_of 循环遍历
- 语法: for(let value of target){}
- 参数:
	- value 变量
	- target 要循环遍历的目标
- 作用
  1. 遍历数组
  2. 遍历Set
  3. 遍历Map
  4. 遍历字符串
  5. **遍历伪数组**
 