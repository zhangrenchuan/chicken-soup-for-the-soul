## ECMAScript 5 
#### 严格模式
- 除了正常运行的模式(混杂模式).ES5添加了第二种运行模式:严格模式
- 目的
    - 消除Javascript语法的一些不合理、不严谨之处，减少一些怪异行为
	- 消除代码运行的一些不安全之处，为代码的安全运行保驾护航
	- 为未来新版本的Javascript做好铺垫
- 使用:
    - 全局作用域或函数中定义一个````'use strict'````字符串
- 语法限制
	1.  必须使用var声明变量
	2.  禁止自定义函数中的this指向window
	3.  新增eval的自身作用域.不能再修改全局中的变量
	    - eval()解析里面的字符串. 并运行里面的字符串代码
	4.  对象不能有重名属性

----------

#### JSON字符串方法
- JSON.stringify(obj/arr)
    - js对象(数组)转换为json的对象(数组)
- JSON.parse(json)
    - json的对象(数组)转换为js对象(数组)

----------

#### Object扩展方法
##### get propertyName(){} 
- 用来得到当前属性值的回调函数
##### set propertyName(){} 
- 用来监视当前属性值变化的回调函数
##### Object.create(prototype, [descriptors])
- 指定 对象的原型创建新的对象
- 第一个参数: 对象
    - 传入对象的原型属性可被新创建的对象访问
    - 新创建的对象的隐式原型属性指向第一个参数里对象的显示原型属性 
- 第二个参数: 为新的对象指定新的属性, 并对属性进行描述(对象)
    - value : 通过value指定值
    - writable : 标识当前属性值是否是可修改的, 默认为true可修改
    
**例**

	  var obj = {
	    name:'wukong',
	    age:39
	  };
	  var obj1 = {};
	  
	  obj1 = Object.create(obj,{ //obj是obj1的原型对象
	    sex:{
	      value:'男',
	      writable:true //可修改属性
	    }
	  });
	
	  obj1.sex = "女";
	  console.log(obj1.sex); //女

##### Object.defineProperties(object, descriptors)
- 第一个参数: 要扩展属性的对象
- 第二个参数: 为对象指定新的属性(对象).使用存取器属性
    - get : 用来得到当前属性值的回调函数. 通过get设置的不能直接修改属性
    - set : 用来监视当前属性值变化的回调函数
    
**例**

	  var obj = {
	    firstName:'wukong',
	    lastName:"sun"
	  };
	  Object.defineProperties(obj,{
	      fullName:{
	        get:function () {
	        	  return this.firstName + "-" + this.lastName
	        },
	        set:function (data) {
	        	var names = data.split('-');
	        	this.firstName = names[0]
	            this.lastName = names[1]
	        }
	      }
	  })
	  console.log(obj.fullName); //wukong-sun

	  obj.firstName = 'tim';
	  obj.lastName = 'duncan'
	  console.log(obj.fullName); //tim-duncan
	
	  obj2.fullName = "zrc-sss";
	  console.log(obj.fullName); //zrc-sss



----------

#### Array扩展方法
##### indexOf(value) 
- 得到 数组值 在数组中出现第一次的下标

##### lastIndexOf(value)
- 得到 数组值 在数组中最后一次出现的下标

##### forEach(function(item, index){})
- 遍历数组
- 第一个参数: 数组元素
- 第二个参数: 数组元素下标

##### map(function(item, index){})
- 遍历数组
- 可在遍历数组后对数组元素进行修改
- 并返回加工后的新数组值
- 需要一个变量来接收

		var arr = [1,2,3,4,5,5];
		var arr1 = arr.map(function (item,index) {
		  	  return item +10
		})
		console.log(arr,arr1); //[10,20,30,40,50,50]

##### filter(function(item, index){})
- 遍历数组
- 可在遍历数组后对数组元素进行过滤操作
- 返回条件为true的元素值
- 需要一个变量来接收

		var arr = [1,2,3,4,5,5];
		var arr1 = arr.filter(function (item,index) {
		  	  return item > 2
		})
		console.log(arr,arr1); //[3,4,5,5]


----------

#### Function扩展方法
##### Function.prototype.bind(obj)
- 将函数内的this绑定为obj, 并将函数返回

##### 区别bind()与call()和apply()
- 都能指定函数的this
- call()/apply()是指向this之后立即调用函数
- bind()是指定this之后将函数返回.需要手动再调用