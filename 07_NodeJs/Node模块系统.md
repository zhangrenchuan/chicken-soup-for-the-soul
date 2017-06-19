## node模块系统
- 让NodeJs文件可以互相调用
- 每一个JS文件都是一个模块
- 模块的好处:
	1. 封装代码
	2. 复用性好
	3. 扩展性
	4. 可维护性好

----------

	
	require 用来引入一个js文件	
	var name = require('js文件路径')


	exports 向外暴露(只能返回object)对象
	如果直接暴露一个对象则返回一个空的Object
	需要使用如下办法进行暴露属性或方法:
	- exports.name = value
	- exports.名 = 值  --> 暴露属性
	- exports.fnname = function(){}
	- exports.函数名 = 函数 -->暴露方法
	不向外暴露: 不能被外界访问的称为私有属性和私有方法.


	module.exports 向外暴露只返回对象本身
	- module.exports = name 
	- module.exports = 值  --> 直接暴露对象属性
	- module.exports.name = value;
	- module.exports.func = function(){}
	- module.exports = [1, 3, 5]
	- 只指向一个对象

##### exports例子

	var name = 'wukong';
	exports.name = name;
	exports.age = 2000;
	
	exports.info = {
	    home: 'huaguoshan',
	    weapon: 'bang'
	};
	
	exports.flyFun = function () {
	    console.log('fei')
	};
	
	//私有属性
	var title = 'horse';
	//私有方法
	function feedHorse() {
	    console.log('yang ma');
	}
	----------------------
	// 1.引入的对象 观察
	var wukong = require('./1.myModule.js');
	
	// 2. 打印被引用模块的属性
	console.log(wukong.name); //wukong
	
	// 3. 调用被引用模块的方法
	wukong.flyFun(); //fei
	
	// 4. 打印被引用模块的私有属性 
	console.log(wukong.title);//返回undefined
	
	// 5. 调用被引用模块的私有方法 
	console.log(wukong.feedHorse());//会报错

#### module.exports例子

	var bajie = {
	    name : 'bajie',
	    age : 2000,
	    home : '高老庄',
	    skill : function () {
	        console.log('巨能吃');
	    }
	};
	----------------------
	var bajie = require('./1.myModule.js');
	console.log(bajie);
	----------------------
	//exports.bajie = bajie;
	/*
	{ bajie:
	 { name: 'bajie',
	 age: 2000,
	 home: '高老庄',
	 skill: [Function: skill] } }
	*/
	
	module.exports = bajie;
	/*module.exports = 值  --> 直接暴露对象属性
	 { name: 'bajie',
	 age: 2000,
	 home: '高老庄',
	 skill: [Function: skill] }
	*/
	
	module.exports.bajie = bajie;
	/*module.exports.name = value; 等同exports
	{ bajie: 
	   { name: 'bajie',
	     age: 2000,
	     home: '高老庄',
	     skill: [Function: skill] } }
	*/



#### exports 与 module.exports 的区别
- exports 必须使用名值对的方式向外暴露数据,返回是一个对象；但是书写方便
- module.exports 可以使用名值对的形式，也可以直接暴露一个对象整体；书写繁琐