## this
1. 本质上任何函数在执行时都是通过某个对象调用的
2. this就代表调用函数的当前对象
3. 在定义函数时this没有确定, 只有在执行时才确定.谁调用谁就是this
4. 当调用函数时没有明确指定当前对象，this就是全局对象window
5. 通过call和apply去调用一个函数,则call和apply中的第一个参数就是this


### this是谁由函数的调用方式决定
  1.以构造函数形式调用.this就代表即将new出来的对象

  2.以函数的形式调用或在全局环境下 this就是window  fn()

  3.函数作为对象的属性并被调用时. this是调用方法的对象 obj.fn()

  4.使用call和apply调用时,this是第一个参数

  5.回调函数中的this:不是我们指定的

- dom事件回调函数中的this  -- dom元素
- 定时器回调函数  -- window
- arr.forEach(function(index,item){})  -- window
- call和apply 可以让一个函数成为任意指定对象上执行
- call的参数,列表数据 需要一个一个列出来
- apply的参数,数组数据 需要封装为一个数组传递 
	
		例子: var obj = {};
		p.setColor.call(obj, "black");
		相当于obj.setColor('black)  this就是obj