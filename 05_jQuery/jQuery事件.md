## jQuery中的事件

### 页面加载

原生DOM中的事件具有页面加载的内容onload事件，在jQuery中同样提供了对应的内容ready()函数。

**ready与onload之间的区别：**

<table>
<thead>
<tr>
<th>onload</th>
<th>ready</th>
</tr>
</thead>
<tbody>
<tr>
<td>没有简写方式</td>
<td>具有简写方式</td>
</tr>
<tr>
<td>当HTML页面所有内容加载完毕后才执行onload</td>
<td>当DOM节点加载完毕后就执行ready</td>
</tr>
<tr>
<td>一个HTML页面只能编写一个onload</td>
<td>一个HTML页面允许同时编写多个ready</td>
</tr>
</tbody>
</table>

**ready()的编写方式：**

*   $(document).ready(function(){});
*   $().ready(function(){});
*   $(function(){});

### 事件绑定

jQuery中提供了事件绑定与解绑机制，类似于原生DOM中的addEventListener()方法。

**jQuery的事件绑定：**

*   单事件绑定

单事件绑定就是指为指定元素绑定一个指定的事件，例如click、change等。


	<div id="panel">
	    <h5 class="head">什么是jQuery?</h5>
	    <div class="content">
	        jQuery是继Prototype之后又一个优秀的JavaScript库，它是一个由 John Resig 创建于2006年1月的开源项目。jQuery凭借简洁的语法和跨平台的兼容性，极大地简化了JavaScript开发人员遍历HTML文档、操作DOM、处理事件、执行动画和开发Ajax。它独特而又优雅的代码风格改变了JavaScript程序员的设计思路和编写程序的方式。
	    </div>
	</div>
	
	<script>
	    $("#panel h5.head").bind("click",function(){
	        var $content = $(this).next("div.content");
	        if($content.is(":visible")){
	           $content.hide();
	        }else{
	           $content.show();
	        }
	    })
	</script>



*   多事件绑定

多事件绑定就是为指定元素同时绑定多个指定的事件，例如同时绑定mouseover和mouseout事件等。


	<div id="panel">
	    <h5 class="head">什么是jQuery?</h5>
	    <div class="content">
	        jQuery是继Prototype之后又一个优秀的JavaScript库，它是一个由 John Resig 创建于2006年1月的开源项目。jQuery凭借简洁的语法和跨平台的兼容性，极大地简化了JavaScript开发人员遍历HTML文档、操作DOM、处理事件、执行动画和开发Ajax。它独特而又优雅的代码风格改变了JavaScript程序员的设计思路和编写程序的方式。
	    </div>
	</div>
	
	<script>
	   $("#panel h5.head").bind("mouseover mouseout",function(){
	       var $content = $(this).next("div.content");
	       if($content.is(":visible")){
	           $content.hide();
	       }else{
	           $content.show();
	       }
	   });
	</script>


### 模拟操作

模拟操作就是指通过程序模拟用户在页面中的操作，比如用户点击某个按钮的事件完成一个效果，jQuery中可以通过该方法模拟用户点击按钮事件。也就是说，不需要用户的操作行为，而是我们通过程序来模拟用户操作。


	<button id="btn">点击我</button>
	<div id="test"></div>
	
	<script>
	    $('#btn').bind("click", function(){
	        $('#test').append("<p>我的绑定函数1</p>");
	    }).bind("click", function(){
	        $('#test').append("<p>我的绑定函数2</p>");
	    }).bind("click", function(){
	        $('#test').append("<p>我的绑定函数3</p>");
	    });
	    $('#btn').trigger("click");
	</script>



----------

### 事件冒泡

**什么是事件冒泡**

在一个对象上触发某类事件（比如单击onclick事件），如果此对象定义了此事件的处理程序，那么此事件就会调用这个处理程序，如果没有定义此事件处理程序或者事件返回true，那么这个事件会向这个对象的父级对象传播，从里到外，直至它被处理（父级对象所有同类事件都将被激活），或者它到达了对象层次的最顶层，即document对象（有些浏览器是window）。

**阻止事件冒泡**

*   DOM标准：event.stopPropagation()
*   IE: event.cancelBubble=true

### 事件对象

**什么是事件对象**

事件是一种JavaScript结构，它会在元素获得处理事件的机会时被传递给被调用的事件处理程序。这个对象中包含与事件相关的信息，也提供了可以影响事件在DOM中传递进程的一些方法。

**事件对象的常用属性**

*   srcElement/target : 事件源对象
*   eventPhase : 事件所处的传播阶段
*   clientX/offsetX/pageX/screenX/x：事件发生的X坐标
*   clientY/offsetY/pageY/screenY/y：事件发生的Y坐标
*   which/keyCode/charCode : 键盘事件中按下的按键
*   button：鼠标哪个按键被按下了
*   cancelBubble ：是否取消事件冒泡
*   returnValue : 是否阻止事件默认行为

**阻止默认行为**

所谓默认行为，就是指页面中默认具有的一些行为，例如表单提交、连接跳转等效果。

*   `event.preventDefault();`
*   `return false;`