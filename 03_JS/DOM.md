# DOM 基础
## Document Object Model 
- 文档对象模型
- DOM就是让我们可以通过JS来操作网页
- 文档
    - 文档指的是整个网页文档
- 对象
    - 将网页中的每一个部分都转换为了一个对象
- 模型
    - 通过模型来表示对象之间的关系,方便我们查找对象

![](http://i.imgur.com/lRO2maM.png)

### DOM 节点
- 节点是构成网页的最基本的单位.网页就是由节点构成的
- 节点又分为多种不同的类型:
    - 文档节点  (doument)
        - 代表整个网页
    - 元素节点    (element)
        - 代表网页中的标签
    - 属性节点    (arreibute)
        - 代表标签中的属性
    - 文本节点    (text)
        - 代表网页中的文本
        
### Document 对象方法
- document.getElementById("id属性值")
	- 根据元素的id属性值,查找一个元素节点
- document.getElementsByTagName("标签名")
	- 根据标签名,查询一组元素节点对象
- document.getElementsByName("name属性值")
	- 根据元素的name属性值,查找一组元素节点对象 (用于表单返回一个数组)
- document.getElementsByClassName('class属性值')
	- 根据class属性值获取一组元素节点对象
- **document.querySelector("CSS选择器")**
	- 根据css选择器去页面中查找对象
	- 只返回一个符合条件的元素
- **document.querySelectorAll("CSS选择器")**
	- 匹配的CSS选择器的所有元素节点列表
	- 将所有符合条件的元素封装到一个数组中返回
- **document.addEventListener()**
	- 第一个参数: 要绑定的事件(字符串格式.没有on)
	- 第二个参数: 回调函数(事件触发时函数执行.形参event)
	- 第三个参数: 是否在捕获阶段触发事件(默认false)
- document.createElement('标签名')
	- 可以根据标签名来创建一个指定的元素节点对象
- document.createTextNode('文本内容')
	- 可以根据文本内容创建一个文本节点对象
	
### Document 对象属性
- document.body
	- 可以用来获取页面中的body元素
- document.documentElement
	- 可以获取页面的根元素
- document.all 
	- 可以获取页面的所有元素

----------


### element方法
- element.childNodes
    - 获取当前元素所有的子节点
    - 包括空白的文本节点
- element.children
	- 获取当前元素所有的子节点
	- 不包括文本节点
- element.firstChild
	- 获取当前元素的第一个子节点
- element.lastChild
	- 获取当前元素的最后一个子节点
- element.prentNode
	- 获取当前元素的父节点
- element.previousSibling
	- 获取当前元素的前一个兄弟节点
	- previousElementSibling(不包括空白文本)
- element.nextSibling
	- 获取当前元素的后一个兄弟节点
	- nextElementSibling (不包括空白文本)
- element.appendChild()
	- 为元素添加一个新的子元素
- element.insertBefore()
	- 在指定的子节点前插入新的子节点
	- 第一个参数:新的节点
	- 第二个参数:要添加新的节点前的子节点
- element.replaceChild()
	- 指定子节点替换现有的
	- 第一个参数: 要插入的节点
	- 第二个参数: 要移除的节点
- element.removeChild()
	- 删除一个子节点
- element.cloneNode()
	- 克隆某个元素
	- 参数: true 表示深度克隆
### element属性
- element.className
	- 设置或返回元素的class属性
- element.innerHTML
	- 获取和设置元素内部的html代码
- element.innerText
	- 获取和设置元素内部的文本内容
- element.nodeValue
	- 文本节点可以通过nodeValue属性获取和设置文本节点的内容
- **element.classList**
	- 操作 class 属性的对象
	- classList.add(); 为一个DOM动态“追加”一个类(class)
	- classList.remove();为一个DOM动态“删除”一个类(class)
	- classList.toggle();切换一个class属性的状态
	- classList.contanins() 是否包含某class属性
	- length 获取类选择器的个数

### arreibute属性相关
- element.getAttribute()
	- 获取指定元素的属性值
- element.removeAttribute()
	- 从元素中删除指定属性
- element.setAttribute()
	- 设置或改变指定属性并指定值
	- 第一个参数: 要添加的属性名
	- 第二个参数: 要添加的属性值
- attr.name
	- 返回属性名
- attr.value
	- 设置或返回属性值
	
### DOM修改CSS样式
- 语法: 元素.style.样式名 = 样式值;
- 样式名需要将其修改为驼峰命名法
- 通过style修改的样式都是元素的内联样式.所以优先级最高
#####  getComputedStyle()
- 第一个参数: 要获取样式的元素
- 第二个参数: 要获取元素的伪类. 不需要的话传null
##### 兼容IE8的获取样式函数
- 第一个参数: 要获取样式的元素
- 第二个参数: 要获取的样式的名字

		function getStyle(obj,name){
		  if(window.getComputedStyle){
		      return getComputedStyle(obj,null)[name];
		  }else{
		      return obj.currentStyle[name];
		    };
		  };
#### 其他CSS样式修改
-  clientWidth
-  clientHeight
	- 获取元素的可见宽度和高度
	- 包括元素的内容区和内边距
	- 只读
- offsetWidth
- offsetHeight 
	- 获取元素整个可见框大小
	- 包括内容区内边距和边框
- offsetParent
	- 返回当前元素的定位父元素
	- 最近开启了定位的祖先元素
	- 如果没有开启定位则返回body
- offsetLeft 水平偏移量
- offsetTop 垂直偏移量 
	- 获取当前元素相对于其定位父元素的偏移量
- scrollHeight
- scrollWidth
	- 获取元素滚动区域的高度和宽度
- scrollTop
	- 垂直滚动条滚动的距离
- scrollLeft
	- 水平滚动条滚动的距离
- clientX
	- 可以获取鼠标指针的水平坐标
- clientY
	- 可以获取鼠标指针的垂直坐标
- pageX
- pageY
	- 可以获取鼠标指针相对于页面的坐标
		

### DOM事件 event
- 事件指的用户和网页或浏览器之间的交互行为
- 需要为事件绑定响应函数来处理事件
	  - e.pageX/Y   绝对定位
	  - e.clientX/Y   基于视口
	  - e.offsetX/Y  相对定位
	  
#### 文档加载
- 浏览器在加载一个页面时,是按照自上向下的顺序加载
- 如果将js代码写在页面最上边,在JS代码执行时,页面还没有加载完毕就会导致无法正常获取到DOM对象
- 解决方法
	- 将js代码写在body标签的下边
	- 将js代码写在````window.onload = function( ){ }; ````里面.onload回调函数会在页面加载完毕以后执行
#### 事件处理中的this 
- 在事件处理程序内的 this 所引用的对象即是设定了该事件处理程序的元素。
- 事件给哪个对象绑定的 this就是哪个对象
#### 取消默认行为
- return false 适合dom0
- event.preventDefault(); 适合dom2
#### 事件对象
- 当浏览器调用事件的响应函数时,每次都会传递进一个事件对象,作为参数
- 在事件对象中封装了当前事件相关的信息.
- **event 作为形参注入到函数里作为事件对象**
#### 冒泡
- 冒泡简单来说就是事件的向上传导. (结构上的关系.不是表现上面的)
- 当后代元素上的事件被触发时,将会导致祖先元素上的相同事件也被触发
- 大部分情况下冒泡都是对开发有利的.它可以简化我们的开发
- 如果不希望发生事件的冒泡.则可以通过事件对象来取消冒泡
- 取消冒泡
	- event.stopPropagation()
	- event.cancelBubble = true
#### 事件委派
- 统一将多个元素上的事件绑定到他们共同的祖先元素上.
- 这样我们只需要绑定一次即可同时处理多个元素上的相同事件
- 这样简化了代码开发.这样也确保新添加的元素上也可以有事件响应函数.
- target属性 ---> 事件由谁触发谁就是target

#### 事件监听 
- addEventListener() 普通浏览器
	- 第一个参数: 要绑定的事件(字符串格式.没有on)
	- 第二个参数: 回调函数(事件触发时函数执行.形参event)
	- 第三个参数: 是否在捕获阶段触发事件(默认false)
- attachEvent() IE浏览器
	- 第一个参数: 绑定的事件 (字符串格式.需要on)
	- 第二个参数: 回调函数

###### 事件监听 (兼容IE8)
参数:

- obj 要绑定事件的对象
- eventStr 事件的字符串
- callback 回调函数.事件触发时调用的函数

		function bind(obj,eventStr,callback){
		     if(obj.addEventListener){
				obj.addEventListener(eventStr,callback,false)
			}else{
				attachEvent()
		    	obj.attachEvent("on"+eventStr,function(){
		    	callback.call(obj);
		  	});
		  }

#### 事件的传播
- 捕获阶段
	- 事件从最外层的元素(document),向目标元素进行事件的捕获
	- 该阶段默认不会触发
- 目标阶段
	- 触发事件的元素.捕获到目标元素则捕获阶段停止
- 冒泡阶段
	- 事件从目标元素向祖先元素中冒泡. 此时开始触发事件
	
![](http://i.imgur.com/4jpYruV.png)

##### 鼠标相关事件
- onclick 鼠标单击事件
- ondbclick 鼠标双击事件
- onmousemove 鼠标移动事件
- onmouseenter 鼠标移入元素时触发
- onmouseleave 鼠标移出元素时触发
- onmouseover 鼠标移到某元素之上时触发
- onmousedown 鼠标按下时
	- contextmenu  右键菜单
	- e.button == 0 左键
	- e.button == 1 滚轮键
	- e.button == 2 右键
- onmouseup 鼠标松开时

##### 键盘相关事件
- onkeydown 某个按键按下时
	- event.keyCode 确认按下的键
- onkeyperss 按键被按下并松开
- onkeyup 按键松开时

##### 其他重要事件
- onload 当页面加载完成时
- onresize 当窗口被调整时
- onscroll  滚动条滚动时触发的事件
- onblur 元素失去焦点时触发
- onfocus 元素获取焦点时触发
- onchange 当input输入值失去焦点发生改变会触发该事件
- oninput 实时记录input表单输入的内容



##### 滚轮相关事件
**ie/chrome : onmousewheel(dom0)**

	event.wheelDelta
		上：120
		下：-120
			
**firefox : DOMMouseScroll 必须用(dom2的标准模式)**

	event.detail
		上：-3
		下：3

- return false阻止的是  dom0 所触发的默认行为
- dom2 需要通过event下面的event.preventDefault();