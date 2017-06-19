### Vue重要知识支持
1. [].slice.call(伪数组对象): 将伪数组转换为真数组

		  lis = [].slice.call(lis); 
		  console.log(lis instanceof Array);  //true
2. nodeType: 获得节点类型
	- Element元素节点: 1
	- Attr属性节点: 2
	- text文本节点: 3
3. **Object.defineProperty(obj, propertyName, {})** 给对象添加属性(指定描述符)
	- 参数: 要添加属性的对象 / 添加的属性名 / 配置属性对象
	- 数据描述符
	      - configurable: true/false  是否可以重新define
	      - enumerable: true/false 是否可以枚举
	      - value: 指定初始值
	      - writable: true/false value是否可以修改   
	- 存取(访问)描述符
	      - get: 函数, 用来得到当前属性值
	      - set: 函数, 用来监视当前属性值的变化
4. **obj.hasOwnProperty()**  判断某属性是否是obj自身的属性

##### 5. Object.keys(obj) 得到对象自身可枚举属性组成的数组

	var obj = {
	    firstName: 'a',
	    lastName: 'b'
  	};
	(2)["firstName", "lastName"]

##### 6. DocumentFragment 文档碎片
- 高效批量更新多个节点. 
- 通过 `document.createDocumentFragment()` 创建fragment对象
###### fragment实例

	[初始文本]
	<ul id="fragment_test">
	  <li>test1</li>
	  <li>test2</li>
	  <li>test3</li>
	</ul>

	// 创建空的 fragment 对象
	var fragment = document.createDocumentFragment();
	// 获得ul
 	var ul = document.getElementById('fragment_test');

	//剪切ul下的所有子节点到 fragment 对象里
	var child = null;
	while(child = ul.firstChild) {
	  fragment.appendChild(child)
	}
	console.log(fragment); 
  
    //遍历 fragment 中所有的child. 将元素类型的child更新 标签体文本
    var children = fragment.childNodes;
    console.log(children.length); // 7个
    [].slice.call(children).forEach(function (child, index) {
      if (child.nodeType === 1) { //找到所有元素节点
        child.innerHTML = 'fragment'
      }
    });

    // fragment对象里的元素 粘贴进ul里
    ul.appendChild(fragment);

	[页面新的文本]
	fragment
	fragment
	fragment

----------

### 编写项目的方式
- 模块化: 以js文件编写
- 组件化
	- 一个组件标签就代表一个组件对象
	- 编写复杂界面拆分成各个组件并组合使用
- 工程化
	- 通过命令自动化构建项目
	- 如果项目构建是自动化的,则就是工程化
#### 模块和组件
- 模块 --> JS文件 (实现特定的功能)
- 组件 --> 功能模块 (界面由很多组件组成)
	- 组件里可能包含多个JS模块
	- 包含实现页面功能的所有资源