# 此文仅供参考!!!!


### 数据代理(MVVM.js)
- 通过一个对象代理对另一个对象中属性的操作(读/写)
- 通过vm对象来代理data对象中所有属性的操作
- **好处: 更方便的操作data中的数据**
- 基本实现流程
  - 1). 通过Object.defineProperty(vm, key, {})给vm添加与data对象的属性对应的属性
  - 2). 所有添加的属性都包含get/set方法
  - 3). 在get/set方法中去操作data中对应的属性

###### MVVM 数据代理代码实现

    function MVVM(options) {
		// 1. 将配置对象保存到 MVVM 实例对象(vm)里
	     this.$options = options; 
		// 2. 将配置中的data 保存到 vm对象/data中
	     var data = this._data = this.$options.data; 
		// 3. 缓存 vm 对象
	     var me = this;  
	
	     // 4. 数据代理
	     // 实现 vm.xxx -> vm._data.xxx
	     // 遍历data中 所有的属性. 并实现对它的代理
	     Object.keys(data).forEach(function(key) {
	         me._proxy(key); // 5. 实现对key的数据代理
	     });
	
	     observe(data, this);
	
	     this.$compile = new Compile(options.el || document.body, this)
    }

	// _proxy 保存在对象的原型中
	MVVM.prototype = {
	    $watch: function(key, cb, options) {
	        new Watcher(this, key, cb);
	    },
	
	    _proxy: function(key) {
	       // 缓存vm
	        var me = this;
	       // 通过defineProperty 实现对 key的代理
	        Object.defineProperty(me, key, {
	            configurable: false,  // 配置不可修改
	            enumerable: true,  // 属性可枚举
			// 当读取 vm.xx属性时, 会调用get方法得到对应的属性值
	            get: function proxyGetter() { 
	                return me._data[key];
	            },
			//当修改 vm.xx的值时, 调用set方法. 修改data中对应的属性的值
	            set: function proxySetter(newVal) { 
	                me._data[key] = newVal;
	            }
	        });
	    }
	};

----------

####  模板解析(compile.js)
- 模板解析的关键对象: compile对象
- 模板解析的基本流程:
	- 将el的所有子节点取出, 添加到一个新建的文档fragment对象中
	- 对fragment中的所有层次子节点递归进行编译解析处理
	    - 对表达式文本节点进行解析
	    - 对元素节点的指令属性进行解析
	      	- 事件指令解析
	      	- 一般指令解析
	  	- 将解析后的fragment添加到el中显示
	- 解析表达式文本节点
	  	1. 根据正则对象得到匹配出的表达式字符串: 子匹配/RegExp.$1
	  	2. 从data中取出表达式对应的属性值
	  	3. 将属性值设置为文本节点的textContent
  	- 事件指令解析
	  	1. 从指令名中取出事件名
	  	2. 根据指令的值(表达式)从methods中得到对应的事件处理函数对象
	  	3. 给当前元素节点绑定指定事件名和回调函数的dom事件监听
	  	4. 指令解析完后, 移除此指令属性
  	- 一般指令解析
	  	1. 得到指令名和指令值(表达式)
	  	2. 从data中根据表达式得到对应的值
	  	3. 根据指令名确定需要操作元素节点的什么属性
		  	- v-text---textContent属性
		  	- v-html---innerHTML属性
		  	- v-class--class属性
	  	4. 将得到的表达式的值设置到对应的属性上
	  	5. 移除元素的指令属性
	  	
![](http://i.imgur.com/Y4mjoBj.png)

----------

#### 数据劫持-->数据绑定
##### 数据绑定(model==>View):
- 界面的显示是通过读取data中相对应的数据来显示的(初始化)
- 一旦更新了data中的某个属性数据, 所有界面上直接使用或间接使用了此属性的节点都会更新(更新)
##### 数据劫持
- 数据劫持是vue中用来实现数据绑定的一种技术
- 基本思想: 通过defineProperty()来监视data中所有属性(任意层次)数据的变化, 一旦变化就去更新界面
##### 四个重要对象 
- Observer
	- 用来对data及data所有属性数据进行劫持的构造函数
	- data对象以及data内部所有的子对象, 都有创建一个对应的observer对象
	- 为data中的每个属性创建对应的dep对象
	- observer与dep的关系: 一对多
- Dep(Depend):
    - data中的每个属性(所有层次)都对应一个dep对象
    - 创建的时机:
        - 在初始化define data中各个属性时创建对应的dep对象
        - 在data中的某个属性值被设置为新的对象时
	- 对象的结构
	

			{
			id, // 每个dep都有一个唯一的id
			subs //包含n个对应watcher的数组(subscribes的简写)
			}

	- subs属性说明
		- 当一个watcher被创建时, 内部会将当前watcher对象添加到对应的dep对象的subs中
		- 当此data属性的值发生改变时, 所有subs中的watcher都会收到更新的通知, 从而最终更新对应的界面
- Compile
	- 用来解析模板页面的对象的构造函数(一个实例)
	- 利用compile对象解析模板页面
	- 每解析一个表达式(非事件指令)都会创建一个对应的watcher对象, 并建立watcher与dep的关系
	- complie与watcher关系: 一对多的关系
- Watcher:
    - 模板中每个非事件指令或表达式都对应一个watcher对象
    - 监视当前表达式数据的变化
    - 创建的时机: 在初始化编译模板时
    - 对象的组成
    
				{
				vm,  //vm对象
				exp, //对应指令的表达式
				cb, //当表达式所对应的数据发生改变的回调函数
				value, //表达式当前的值
 				depIds //表达式中各级属性所对应的dep对象的集合对象
				        //属性名为dep的id, 属性值为dep
				}

- 总结: dep与watcher的关系: 多对多
     - 一个data中的属性对应对应一个dep, 一个dep中可能包含多个watcher(模板中有几个表达式使用到了属性)
     - 模板中一个非事件表达式对应一个watcher, 一个watcher中可能包含多个dep(表达式中包含了几个data属性)
     - 数据绑定使用到2个核心技术
	       - defineProperty()
	       - 消息订阅与发布
##### 双向数据绑定
- 双向数据绑定是建立在单向数据绑定(model==>View)的基础之上的
- 双向数据绑定的实现流程:
    1. 在解析v-model指令时, 给当前元素添加input监听
    2. 当input的value发生改变时, 将最新的值赋值给当前表达式所对应的data属性


![](http://i.imgur.com/tjPAdtT.png)