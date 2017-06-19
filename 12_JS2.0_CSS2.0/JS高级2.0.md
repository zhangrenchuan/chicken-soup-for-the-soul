## JS高级2.0
### 作用域
- 只是维护自己范围内变量的集合. 实际就是一套规则
- 作用域负责收集并维护由所有声明的标识符组成的一系列查询，并实施一套非常严格的**规则**，确定当前执行的代码对这些标识符的访问权限
- 狭义上来说作用域就是一个对象（更确切的来说应该是集合）
- 广义上来说作用域是一套用来存储变量，并且之后可以方便的找到这些变量的规则
- javascript中最普遍的作用域是函数作用域


### 上下文环境
- 上下文环境也是一个规则
- 代码（全局代码，函数体，eval代码）执行前的准备工作：
    - 1.提升（变量 函数 函数表达式）
    - 2.确定this指向
    - 3.与对应作用域关联(实际就是赋值操作)
    - 4.函数体还需要参数赋值,arguments赋值
- 可以理解为一个看不见摸不着的对象（有若干个属性），虽然看不见摸不着，但确实实实在在存在的，因为所有的变量的值都在里面存储着
- 另外，对于函数来说，上下文环境是在调用时创建的

#### 作用域和上下文环境关系
- 一个作用域内可能包含若干个上下文环境。
- 有可能从来没有过上下文环境(函数从来就没有被调用过)
- 也有可能有过，但在函数被调用完毕后，上下文环境被销毁了
- 除了全局作用域外,每个函数都要创建一个作用域(函数作用域).作用域的查找: 函数作用域+1
- 在程序执行之前就会生成全局上下文环境. 每调用一次函数就产生一次上下文环境.上下文环境的查找: 调用次数+1

---

### 变量左查询&右查询
- 左查询: 赋值符号的左侧
    - 赋值操作的目标
    - 函数调用时实参与形参的关系就是一次左查询
- 右查询: 赋值符号的非左侧
    - 赋值操作的源头

#### 变量查询规则
- 非严格模式:
    - LHS在查询所有的嵌套作用域中遍寻不到所需变量时,全局作用域中会创建具有该名称的变量
    - RHS在查询所有的嵌套作用域中遍寻不到所需的变量时，引擎就会抛出ReferenceError异常
    - 注意: RHS在typeof时不会报异常
- 严格模式:
    - 未查询到变量时RHS和LHS都会抛出ReferenceError异常
- ReferenceError: 在作用域中找不到变量
- typeError: 执行错误. 跟作用域判别无关
    
#### 作用域查找变量
- 先基于作用域链找到最顶层. 如果都没有去原型链上找. 如果有的话就拿来用
- window.xx直接从全局中找
- xx 会一层一层找直到找到全局

        Object.prototype.a = 1;
        (function () {
          //var a = 3;
        	  function foo() {
        	  	  return function () {
        	  	  	  console.log(a); //1
        	  	  	  console.log(window.a);//1
        	  	  }
        	  }
        	  foo()()
        })();

#### typeof 安全机制
- 意义
	- 只在开发和测试程序使用全局变量DEBUG调试模式开关时
	- 为某个缺失的功能写衬垫代码时
- **typeof做右查询最终会返回变量的值的类型并不会报错**
- undefined: 已经在作用域中声明但还没有赋值的变量.typeof返回的是 undefined
- undeclared: 没有在作用域中声明过的变量.typeof返回的还是 undefined

	    console.log(typeof a); //undefined
	    console.log(typeof typeof 42); //string
	
	    var a1;
	    console.log(typeof a1); //undefined
	
	    var b =42;
	    console.log(typeof b); //number
	    var c;
	    b = c;
	    console.log(typeof b); //undefined

---


### 提升(预解析)
- 提升是上下文环境这套规则在管理
- 变量提升
	- 变量的提升是声明的提升
	- 变量提升不受if判断暗示影响照常提升
- 函数提升
	- 函数的提升是函数整体的提升 (声明式函数 function关键字)
	- 函数提升优于变量的提升
	- 函数表达式是变量的声明提升 (var或者IIFE)
	- 函数提升会受到if判断暗示影响不会被提升.**在块中不要定义函数**


### 闭包
- 当函数可以访问并记住自己所处的作用域时，就会产生闭包。
- 常见场景:
    - 函数作为返回值
    - 函数作为参数传递

----------

### 值传递与引用值的传递
- **JS中所有的传递都是值的传递. 没有引用传递**
	- 基本值的传递 (基本值都储存在栈里)
	- 引用值的传递 (引用值都储存在堆里)
- JS中变量不可能成为指向另外一个变量的指针
- 基本数据类型总是通过值复制的方式来赋值/传递
- 引用数据类型总是通过引用复制来完成赋值/传递
- **注意: 引用指向的是值而非变量.所以一个引用无法更改另一个引用的指向,但是可以更改不同变量共同指向的值**

> 引用传递:

>  1.同一个引用被多个变量同时指向的时候.任一变量修改引用结果其他变量都会被修改.

> 2.引用修改时,变量也会同时改变

![](http://i.imgur.com/OlnSqjV.png)

![](http://i.imgur.com/bbTDLi8.png)

---

### this
- this是上下文环境管理.跟作用域无关
- 根据**调用位置**上函数的**调用方式**来确定函数中this使用的绑定规则

#### this绑定规则一: 默认绑定
- 无法应用其他规则时的默认规则就是独立函数调用 `foo()`
- 独立函数调用在非严格模式下会绑定给window
- 独立函数调用时this整个机制在严格模式下会绑定给undefined
	- 严格模式下进行函数调用不会影响默认绑定规则

#### this绑定规则二: 隐式绑定
- 隐式绑定的规则是调用位置是否有上下文对象，或者说是否被某个对象拥有或者包含
- 当函数引用有上下文对象时，隐式绑定规则会把函数调用中的 this 绑定到这个上下文对象
- 以 对象 点 的形式调用.谁调用this就指向谁 `obj.foo()`
- 以对象连缀形式调用,this只看离它最近的对象并确认绑定

##### 隐式丢失
- 隐式丢失场景
	- 隐式绑定的形式作赋值
	- 参数的传递
	- 函数传入JS内置的函数.比如setTimeout
- 看似是对象dian的形式,但实际是独立函数形式调用
- 被隐式绑定的函数在丢失绑定对象后导致this的绑定变成默认绑定,即window或undefined上

#### this绑定规则三: 显示绑定
- **call()和apply() 方法实现显示绑定**
	- 第一个参数绑定this
	- 第二个参数赋值

````
Array.apply(null,{length:3}); 
相当于Array(undefined,undefined,undefined)
`````

`````
var b=new Array(3);
相当于 Array(undefined * 3)
`````


> apply() 传递的是数组或伪数组
> 
> 任何有length属性的对象都可称为伪数组
> 
> 只有长度没有值的数组称为稀疏数组(数组中有些API无法使用)

##### 显示绑定的硬绑定
1. 要有一个包裹函数
2. 在包裹函数内必须有一个函数的显示绑定
3. 外层包裹函数的绑定不会影响内层绑定形式
4. 典型应用场景:创建一个包裹函数，传入所有的参数并返回接收到的所有值

		function foo() {
			console.log( this.a );
		}
		
		var a =1;
		var obj = {
			a:2
		};
		
		var bar = function() {
			console.log( this.a ); 
			foo.call( obj ); //硬绑定
		};

		bar(); //1  2

##### bind()硬绑定this
- 返回一个新的函数并指定该新函数的this指向
- 硬绑定解决隐式绑定的隐式丢失(尤其是异步函数时)
- 第一个参数绑定this
- 第二个参数赋值

		function foo() {
			console.log( this.a );
		}
		
		var a = 1; // a是全局对象的属性
		var obj = {
			a: 2,
			foo: foo
		};
		
		setTimeout( foo.bind(obj), 1000 ); // "2"


#### this绑定规则四: new绑定
- JS中构造函数只是一些使用 new 操作符时被调用的普通函数
- 实际并不存在构造函数
- 使用 new 来调用函数，或者说发生构造函数调用时，this 的绑定就是new出来的实例对象


#### this绑定的优先级
new绑定 > 显示绑定 > 隐式绑定 > 默认绑定

#### this的其他绑定
- ES6箭头函数的this要看外层作用域.如果有函数则this绑定该函数的this.如果没有函数则this绑定window
- null 或者 undefined 作为 this 的绑定对象传入call或apply时,this会被忽略. 使用默认绑定规则

#### 柯里化
- 给目标函数预绑定一些参数
- 主要作用在于不会污染全局. 仅作this指向

		function foo(a,b) {
			console.log( "a:" + a + ", b:" + b );
		}
		// 我们的DMZ空对象,“DMZ”（demilitarized zone，非军事区）
		var ø = Object.create( null );//{}
		// 把数组展开成参数
		foo.apply( ø, [2, 3] ); // a:2, b:3
		// 使用bind(..)进行柯里化
		var bar = foo.bind( ø, 2 );
		bar( 3 ); // a:2, b:3


----------

### 对象扩展 - 属性描述符
- 对象所有的属性都具备了属性描述符
- Object.getOwnPropertyDescriptor()方法来获取一个属性的对应描述符

##### 属性的描述符 (元属性:对象属性的属性)
- configurable:true 可配置
- enumerable:true 可枚举
- writable:true 可读写

##### Object.getOwnPropertyDescriptor() 获取属性对应描述符
- 第一个参数: 对象
- 第二个参数: 要获取描述符的对象属性

##### Object.defineProperty() 为对象新增定义或修改属性
- 第一个参数: 对象
- 第二个参数: 新定义或修改的属性名
- 第三个参数: 配置对象(value指定属性值)
- defineProperty的属性描述符的默认值都是false(可配置是否为true)

##### 描述符之 writable
- writable决定是否可以修改属性的值,即value的值
- 当writable为false时,对应的属性的值是无法修改的
- 非严格模式下继续修改会静默失败. 反之会报错(typeError)

##### 描述符之 configurable
- configurable 来决定属性是否可以配置
- 当configurable为false时,对应的属性是无法重新定义和无法删除的。但该对象还可以继续添加属性的。
- 不管是否为严格模式,configurable为false时进行重新定义或删除都会报错. 
- window上的configurable是false.所以不能删
- 例外: configurable为false时, 只允许writable从true到false

		//给对象定义属性(新增)
	    Object.defineProperty(obj,'age',{
	      value:50,
	      writable:true
	    });

		//重新定义属性 
	    Object.defineProperty(obj,'age',{
	      value:40,
	      writable:false
	    });

		//继续添加属性 {name: "wukong", age: 40, sex: "男"}
		Object.defineProperty(obj,'sex',{
		   value:'男',
		});

		//writable为false无法修改 则报错!!! 
		Object.defineProperty(obj,'age',{
		   value:58,
		});

##### 描述符之 enumerable
- enumerable是否支持属性出现在对象属性的遍历中（for in循环）
- 不可枚举的属性不会出现在 `for..in` 循环中

	    var obj = {};
	
	    Object.defineProperty(obj,'a',{
	      value:'a',
	      enumerable:true
	    });
	    Object.defineProperty(obj,'b',{
	      value:'a',
	    });
	    Object.defineProperty(obj,'c',{
	      value:'a',
	    });
	    
	    for(item in obj){
	      console.log(item); //a
	    }

- obj.propertyIsEnumerable() 判断属性是否可枚举 (参数为对象属性)
- Object.keys() 获取可枚举的属性列表 (参数为对象)
- Object.getOwnPropertyNames() 获取所有属性列表 (参数为对象)
- 以上三个方法都不会遍历原型链

	    console.log(obj.propertyIsEnumerable('b')); //false
	    console.log(Object.keys(obj)); // ['a']
	    console.log(Object.getOwnPropertyNames(obj));//(3) ["a", "b", "c"]


##### 描述符小概念
- 属性描述符: 用来形容属性的属性. 
- 数据描述符: 具有writable和value的属性描述符的属性.本质是属性
- 访问描述符: 具有set和get属性描述符的属性. 本质是属性

----------

### 对象扩展 - 对象的不变性
- 注意! JS中所有方法的创建都是浅不变性的，只会影响目标对象和它的直接属性
- 深层次嵌套的影响不了,原型链中的更加影响不了

##### 对象常量属性
- 值不可修改,不可重新定义,不可删除就是常量属性
- 常量属性跟对象无关
- configurable和writable为false就是常量属性

##### 禁止对象扩展属性
- 调用 Object.preventExtensions(obj)
	- 参数: 要求禁止扩展的对象
- 非严格模式下为对象添加新属性会静默失败.反之则会报错(typeError)
- 注意: 之前的属性还是可以进行重新定义和删除的.属性值也可修改

##### 密封对象
- 调用 Object.seal(obj)
	- 参数: 要求被密封的对象
- 密封后原有的属性不可进行重新定义和删除.但属性值可以修改
- 密封对象只针对一层.如果有嵌套对象不会受影响

	      var obj = {
	        name:'wukong',
	        wife:{
	          w1:'小a',
	          w2:'小b'
	        }
	      };
	
	      "use strict";
	      Object.seal(obj); //密封对象
	      delete obj.name; //无法删除
	
	      obj.name = 'bajie'; //可修改属性值
	      obj.wife.w1= 1; //嵌套对象不受影响
	      delete obj.wife.w2; //删除嵌套对象内的属性
	      console.log(obj); //name:"bajie"wife:{w1:1}

##### 冻结对象
- 调用 Object.freeze(obj)
	- 参数: 要求被冻结的对象
- 冻结后禁止了对象扩展属性.原有属性不可重新定义和删除并且属性值也不可以修改


----------

### 对象扩展 - 对象的访问描述符
- 当给属性定义get和set时,这个属性会被定义为 访问描述符
- set和get为属性描述符.可以定义方法
- 当前属性的属性值是根据一个或多个其他属性计算得来时,属性动态查找或获取时调用get方法
- 当其他属性根据当前属性值变化而变化时,监视当前属性时调用set方法 (参数传入value. set中不能有原生属性) 
- set和get方法里可以处理更多的逻辑.并且给属性创造更安全的环境

	    var obj = {
	      get a(){
	        return 1;
	      },
	      set a(val){
	        console.log('set');
	      }
	    };
	    obj.a = 2; //只认set
	    console.log(obj.a); //'set'  1

- 当给属性定义value和writable时,这个属性会被定义为 数据描述符
- 当有访问描述符时,JS会忽略value和writable特性. 这两对无法兼容
- 因为有value和writable时属性称为数据描述符. 而有set和get时属性称为访问描述符

	
	    var obj = {};
	
	    Object.defineProperty(obj,'age',{
	      //value:1,
	      //writable:true, 冲突会报错

	      set : function (value) {
	        if (value<0){ //如果年龄小于0无意义则就等于0
	          console.log('set'); 
	          this._a_ = 0; 
	        }else{
	          this._a_ = value;
	        }
	      },
	      get : function () {
	         return this._a_;
	      }
	    });
	    obj.age = -1; //调用set方法
	    console.log(obj.age); //'set' 0


----------

### 对象扩展 - 存在性检查
- 不能确定属性是否存在于对象中
- `in` 操作符进行存在性检查 (会遍历原型链)
- obj.hasOwnProperty(); 不会遍历原型链，只在对象中查找(参数是要确认存在性的属性名)


----------

### 对象的扩展 - 对象属性的获取
##### 前提:属性是数据描述符.且属性的writable为true
- 先从对象的直接属性去找.找不到去原型链找 (原型链包括对象的直接属性) 
- 如果整条原型链上都没有就返回 undefined

        Foo.prototype.age = 10;
        function Foo() {
            this.age = 8
        }
    
        var foo = new Foo(); //实例对象
    
        console.log(foo.age);//8
        console.log(Foo.prototype.age);//10
    
    
##### 前提: 属性是访问描述符
- 调用get方法获取
- 如果get方法没有,则返回undefined


    function Foo() {}

    var foo = new Foo();

    Object.defineProperty(foo,'age',{
      get:function () {
          return  this._age;
      },
      set:function (value) {
      	  this._age = value
      }
    });
    foo.age = 15;
    console.log(foo.age); //15
    

---

### 对象的扩展 - 对象属性的设置
##### 前提I:属性直接存在于对象中不在原型链上
- 属性为数据描述符: 
    - writbale为true: 直接修改对象中的属性
    - writbale为false: 静默失败或严格模式下报错
- 属性为访问描述符: 
    - 调用set方法 (属性设置只看set)

##### 前提II: 属性直接存在于对象中.也在原型链上
- 属性为数据描述符: 
    - 原型链中的属性不会被修改
    - writbale为true: 直接修改对象中的属性
    - writbale为false: 静默失败或严格模式下报错
- 属性为访问描述符: 
    - 调用set方法 (属性设置只看set)

##### 前提III:属性不直接存在于对象中也不在原型链上
- 属性为数据描述符: 
    - writbale为true: 在对象的直接属性中直接添加属性
    - writbale为false: 静默失败或严格模式下报错
- 属性为访问描述符:
    - 调用set方法 (属性设置只看set)

##### 前提IV: 属性不直接存在于对象中.但在原型链上
- 原型链上属性为数据描述符
    - writbale为true: 在对象的直接属性中添加一个属性，我们称之为屏蔽属性
    - writbale为false: 不会生成屏蔽属性(静默失败).严格模式下报错
- 原型链上属性为访问描述符
    - 调用set方法，不会生成屏蔽属性. 具体看set方法的实现
    

##### 注意事项
- 属性是数据描述符在writable为false时. 有可能在做属性赋值操作时, 属性的值会赋值不上
- 对象中没有该属性. 原型链上有该属性,且属性为访问描述符.或属性是数据描述符且writable为false时,可能在做属性赋值操作时, 属性添加不到对象中

----------

#### 自定义 getElementsByClassName 兼容IE8
- 获取所有className并返回数组
- 功能:获取指定父节点下指定className下的指定节点
- 技术点: 正则表达式杠b (匹配独立单词两边的空白字符)

	    function getElementsByClassName(parentNode,className,targetName) {
	  	   var arr = [];
	
	  	  //找到父节点下的指定class
	      var allNodes = parentNode.getElementsByTagName(targetName);
	
	     //遍历所有的节点
	      for(var i=0;i<allNodes.length;i++){
	
	      //每一个节点里的class中是否有className
	       var reg = new RegExp("\\b" + className + "\\b"); 
	
	       if(reg.test(allNodes[i].className)){
	          arr.push(allNodes[i])
	       }
	     }
	  	  return arr //直接返回出一个数组
	    }

#### 自定义 addClass 方法
	  function addClass(node,className) {
	    //匹配className两边的空白字符
	    var reg = new RegExp("\\b" + className + "\\b");
	    //原来的class中没有就添加class. 有的话直接忽略
	    if(!reg.test(node.className)){ //属性的查找走原型链
	      node.className += (" "+ className) //变量的查找 走的是作用域链
	    }
	  }

#### 自定义 removeClass 方法
	  function removeClass(node,className) {
	    //匹配className两边的空白字符
	    var reg = new RegExp("\\b" + className + "\\b","g");
	    //原来的class中有就删掉 (用空白字符替换)
	    if(reg.test(node.className)){
	      node.className = node.className.replace(reg,"");
	      if(/^\s+$/.test(node.className)){
	        node.removeAttribute("class")
	      }
	    }else{
	      node.removeAttribute("class")
	    }
	  }


----------

## == 操作符
#### ==操作符解析
- 第一大类(有的状态): String. Number. Boolean. Object
- 第二大类(无的状态): Undefined. Null
- 第一大类和第二大类比较永远都是false
- 第二大类之间比较永远是true
- 对象与对象之间比较比较的都是栈中保存的地址值
- NaN 不等于NaN

#### null和undefined
- null是关键字. undefined是标识符
- 初始的想法:
	- var a = null 当引用数据类型用
	- var a = undefined 当基本数据类型用	

#### parseInt() 和 parseFloat()
- 字符串: 第一位是数字则转换成Number. 否则都是NaN
- 其他(不包括Number类型): NaN

#### Number()
- 字符串: 去除字符串两边空白字符和引号.
	- 如果是合法数字就转换为数字. 否则是NaN
	- 空白字符串转换为 0 
- Boolean: true为1. false为0
- Null: 0
- Undefined: NaN
- Object: NaN

#### valueOf() 和toString()
- valueOf() 对象转换成原始类型的值（数值、字符串和布尔值）
	- 对象转基本数据类型 --> 拆包(包装类)
- toString() 对象转换为字符串时，会调用它的toString()方法
	- new String()
	- new Number()
	- new Boolean() 
	- 以上都是装包 (包装类)

#### 相同数据类型比较 (包括全等===)
- 必须类型相同. 值也相同  ==才能返回true
- 对象不等于对象. 除非发生引用值的传递
- NaN 永远不等于NaN

#### 不同数据类型比较
- == 趋于数字化
- 基本数据类型 --> 调用Number()方法
- 引用数据类型 --> 首先调用valueOf() 方法
	- 如果返回是基本数据类型 --> 直接进行比较 调用Number()方法
    - 如果返回是引用数据类型 --> 再调用本身的 toString() 方法
    	- 如果返回是基本数据类型 --> 直接进行比较
	    - 如果返回是引用数据类型 (除非重写对象)  --> 报错
	- 例外: Date 先调用toString再调用valueOf

#### 引用数据类型方法重写的比较实例

    function Test() {
    	  this.toString = function () {
    	  	  return 1;
    	  }
    }

    //方法的重写
    Array.prototype.valueOf = function () {
    	  return new Test();
    };

    Array.prototype.toString = function () {
    	  return 1
    };
    console.log([""] == false); //false

#### == 操作符总结
- undefined == null，结果是true。且它俩与所有其他值比较的结果都是false。
- String == Boolean，需要两个操作数同时转为Number。
- String/Boolean == Number，需要String/Boolean转为Number。
- Object == Primitive，需要Object转为Primitive(具体通过valueOf和toString方法)。
	- Date 先调用tostring 后调用valueof
	

#### == 操作符的坑

	[] == []  //false
	{} == {} //false
	var a={}; var b=a; b==a //true
	NaN == NaN  //false
	null == fasle  //false
	null == ""  //false
	null == undefined //true
	parseInt(null)  //NaN
	parseInt("")  //NaN
	parseInt(true)  //NaN
	Number("11111ssss")  //NaN
	!1 == 2  //false
	0.1+0.2 == 0.3 //false

	[""].valueOf()  // [""]
	[""].toString()  //""
	[""] == 0  //true
	[""] == false  //true
	

![](http://i.imgur.com/WlwF05e.png)