## jQuery插件
#### jQuery 日期插件

layDate日期插件致力于成为全球最用心的web日期支撑，为国内外所有从事web应用开发的同仁提供力所能及的动力。

	
	<!DOCTYPE html>
	<html lang="en">
	<head>
	    <meta charset="UTF-8">
	    <title>01_laydate插件的基本使用</title>
	    <script src="laydate/laydate.js"></script>
	</head>
	<body>
	    <input placeholder="请输入日期" class="laydate-icon" onclick="laydate()">
	    <br>
	    <input placeholder="请输入日期" id="hello1">
	    <span class="laydate-icon" onclick="laydate({elem: '#hello1'});"></span>
	</body>
	</html>



**layDate API选项：**

*   elem: '#id', //需显示日期的元素选择器
*   event: 'click', //触发事件
*   format: 'YYYY-MM-DD hh![:mm:](https://assets-cdn.github.com/images/icons/emoji/mm.png ":mm:")ss', //日期格式
*   istime: false, //是否开启时间选择
*   isclear: true, //是否显示清空
*   istoday: true, //是否显示今天
*   issure: true, 是否显示确认
*   festival: true //是否显示节日
*   min: `1900-01-01 00:00:00`, //最小日期
*   max: `2099-12-31 23:59:59`, //最大日期
*   start: `2014-6-15 23:00:00`, //开始日期
*   fixed: false, //是否固定在可视区域
*   zIndex: 99999999, //css z-index
*   choose: function(dates){} //选择好日期的回调


		<!DOCTYPE html>
		<html lang="en">
		<head>
		    <meta charset="UTF-8">
		    <title>02_laydate插件的高级使用</title>
		    <script src="jquery-1.11.3.js"></script>
		    <script src="laydate/laydate.js"></script>
		</head>
		<body>
		    <input id="mydate" placeholder="请输入日期" class="laydate-icon">
		    <script>
		        laydate({
		            elem : "#mydate",
		            event : "focus",
		            istime : true,
		            isclear : false,
		            istoday : false,
		            issure : false
		        });
		    </script>
		</body>
		</html>


----------
### 表单验证插件

表单验证插件主要是针对表单元素的值进行验证，并给出响应的图形以及文字提示。

**常用验证插件**

*   formValidator
*   jQuery.validator
*   easyForm
*   validate.js

#### jQuery.validator插件

该插件提供用户方便地实现表单验证，同时还提供大量的定制选项。
官方地址：[http://jqueryvalidation.org/](http://jqueryvalidation.org/)

1. 引入必要文件
  - 引入jQuery库文件
  - 引入插件文件 dist/jquery.validate.js
  - 引入国际化文件 (提示语言文件)
dist--localization--message_zh.js 中文提示语言
2. 在HTML页面定义表单
   - 表单的元素使用HTML5提供的新表单验证功能
   - required 表示必填项
3. 在JS逻辑中填写
   -  通过表单调用validate()核心方法
  $().validate();

**validation基本使用**


	<div id="main">
	    <p>Take a look at the source to see how messages can be customized with metadata.</p>
	    <!-- Custom rules and messages via data- attributes -->
	    <form class="cmxform" id="commentForm" method="post" action="">
	        <fieldset>
	            <legend>Please enter your email address</legend>
	            <p>
	                <label for="cemail">E-Mail *</label>
	                <input id="cemail" name="email" data-rule-required="true" data-rule-email="true" data-msg-required="Please enter your email address" data-msg-email="Please enter a valid email address">
	            </p>
	            <p>
	                <input class="submit" type="submit" value="Submit">
	            </p>
	        </fieldset>
	    </form>
	</div>
	<script>
	    $(document).ready(function() {
	        $("#commentForm").validate();
	    });
	</script>



**validate()验证方法的选项**

<table>
<thead>
<tr>
<th>选项名称</th>
<th>描述说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>debug</td>
<td>设置是否为调试模式，如果为调试模式表单不会被提交。</td>
</tr>
<tr>
<td>submitHandler</td>
<td>表单提交时的回调函数，一般用于提交当前表单。</td>
</tr>
<tr>
<td>rules</td>
<td>设置表单元素的验证规则，格式为key:value。</td>
</tr>
<tr>
<td>messages</td>
<td>设置表单元素验证不通过时的错误提示信息。</td>
</tr>
<tr>
<td>errorClass</td>
<td>自定义错误提示信息的样式。</td>
</tr>
<tr>
<td>ignore</td>
<td>设置哪些表单元素不进行验证。</td>
</tr>
</tbody>
</table>

**validation自定义验证**

- $().validate(options)
- rules  自定义的验证规则
	- key 要验证的表单元素的name属性值
	- value 指定使用的验证规则名称
	
			rules : {
			   email:true, //输入正确的email格式
			   number:true, //输入合法的数字
			}
 
- equalTo : "相同内容的id"
- messages 自定义的错误提示

		messages : {
			key : ' value '
		}


- 自定义错误提示的显示位置(单选和多选框)
	- 自定义的错误提示默认出现在第一个被验证的元素后面
	- 自定义的错误提示应该出现在一组验证元素的后面
	- 自定义了用于显示错误提示信息的标签
		- ````<label for="" class="error"></label>````
		- class 插件底层的错误提示信息的样式
		- for 告知插件当前错误提示信息与哪个指定的验证元素相关

![](http://i.imgur.com/c3sHFLa.png)

**自定义验证方法**

jQuery.validator.addMethod( name, method [, message ] )方法

*   name：设置验证方法的名称。
*   method：回调函数，function(value,element,param){}
    *   value：元素的值
    *   element：元素本身
    *   param：参数
*   message：设置验证不通过的错误提示信息。

----------

## jQuery  UI
jQuery UI能做的事可谓是包罗万象。实际上，jQuery UI在某种意义上并不是插件，而是一个完整的插件库。

jQuery UI中主要包含以下几个功能：

*   Effect（效果）
*   Interactions（交互组件）
*   Widget（部件）
*   此外，还为jQuery和核心动画提供了很多高级效果。

###### 使用
-  引入ui -- jquery-ui.js
-  引入themes -- base -- jquery-ui.css / imagse(同级目录)
-  //引入demos -- demos.css

----------

### Effect（效果）
####  animate( )方法

文档在引入核心效果文件的情况下，扩展的.animate()方法可接受另外一些样式属性。

扩展后animate方法接受以下属性：

*   backgroundColor
*   borderBottomColor
*   borderLeftColor
*   borderRightColor
*   borderTopColor
*   Color
*   outlineColor


		var state = true;
		$( "#button" ).click(function() {
		    if ( state ) {
		        $( "#effect" ).animate({
		            backgroundColor: "#aa0000",
		            color: "#fff",
		            width: 500
		        }, 1000 );
		    } else {
		        $( "#effect" ).animate({
		            backgroundColor: "#fff",
		            color: "#000",
		            width: 240
		        }, 1000 );
		    }
		    state = !state;
		});

----------

#### effect( )方法
- 扩展后animate()方法接受以下属性：

	backgroundColor
	borderBottomColor
	borderLeftColor
	borderRightColor
	borderTopColor
	Color
	outlineColor

![](http://i.imgur.com/nOxK2i0.png)

----------

### Interactions（交互组件）

#### Draggable Widget
####### $( "#draggable" ).draggable();
- start：当拖动开始时触发。
- drag：当鼠标在拖动过程中移动时触发。
- stop：当拖动停止时触发。

####### draggable()的选项
- 约束运动
	- axis：设置只能在x轴或y轴方向拖动。
	- containment：设置在某个区域内拖动。
- 光标样式
	- cursor：设置拖动时鼠标的样式。
	- cursorAt：设置鼠标的相对定位。
	- handle：设置指定元素触发鼠标按下事件才能拖动。
	- cancel：防止在指定元素上拖动。
	- revert：当停止拖动时，元素是否被重置到初始位置。
	- snap：拖动元素是否吸附在其他元素。
	- snapMode：设置拖动元素吸附指定元素的哪个边缘。
	- snap设置为true时该选项有效。
		 - inner|outer|both
		 - ````$( "" ).draggable({ snap: "#id", snapMode: "outer" });````
		
- Draggable Widget允许使用鼠标移动元素。


		<div id="draggable" class="ui-widget-content">
		    <p>Drag me around</p>
		</div>
		
		<script>
		    $( "#draggable" ).draggable();
		</script>

----------
#### Droppable Widget

Droppable Widget为可拖拽小部件创建目标。

*   droppable()的事件
    *   drop：该事件在被允许拖放的元素覆盖时触发。
*   droppable()的选项
    *   accept：指定可拖动的元素可被接受。
    *   activeClass：被允许拖放的元素覆盖时，改变样式。
    *   hoverClass：被允许拖放的元素悬停时，改变样式。

----------

##### jQuery UI Resizeable 缩放效果
- 使用鼠标改变元素的尺寸

  	````$( "#resizable" ).resizable();````

##### jQuery UI selectable 元素选择效果
- 使用鼠标选择单个元素或一组元素
  
	````$( "#selectable" ).selectable();````

##### jQuery UI Sortable 排序效果
- 使用鼠标调整列表中或者网格中元素的排序

  	````$( "#sortable" ).sortable();````

----------
#### Widget (部件)
##### jQuery UI Accordion  折叠面板效果
- 在一个有限的空间内显示用于呈现信息的可折叠的内容面板。
- ````$( "#accordion" ).accordion();````
> **需要注意的是：**
> 
> *   使用`<div>`元素作为折叠面板的容器。
> *   使用`<h3>`元素作为折叠面板的标题。
> *   使用`<div>`元素作为折叠面板的内容。

##### jQuery UI Autocomlete  自动检索完成效果
- 根据用户输入值进行搜索和过滤，让用户快速找到并从预设值列表中选择。
- ````$( "#autocomlete" ).autocomlete();````


#####  jQuery UI Button  按钮效果
- 在一个有限的空间内显示用于呈现信息的可折叠的内容面板。
- ````$( "#button" ).button();````


##### jQuery UI  Datepicker 日历选择器
- Datepicker Widget从弹出框或在线日历选择一个日期。

		<p>Date: <input type="text" id="datepicker"></p>
		<script>
		    $( "#datepicker" ).datepicker();
		</script>


##### jQuery UI  Dialog对话框
Dialog Widget在一个交互覆盖层中打开内容。

*   基本对话框示例


		<div id="dialog" title="Basic dialog">
		    <p>This is the default dialog which is useful for displaying information. The dialog window can be moved, resized and closed with the 'x' icon.</p>
		</div>
		<script>
		    $( "#dialog" ).dialog();
		</script>



*   模式对话框示例


		<div id="dialog-modal" title="Basic modal dialog">
		    <p>Adding the modal overlay screen makes the dialog look more prominent because it dims out the page content.</p>
		</div>
		<script>
		    $( "#dialog-modal" ).dialog({
		        modal: true
		    });
		</script>



*   操作对话框示例


		<div id="dialog" title="Basic dialog">
		    <p>This is an animated dialog which is useful for displaying information. The dialog window can be moved, resized and closed with the 'x' icon.</p>
		</div>
		
		<button id="opener">Open Dialog</button>
		
		<script>
		    $( "#dialog" ).dialog({
		        autoOpen: false,
		        show: {
		            effect: "blind",
		            duration: 1000
		        },
		        hide: {
		            effect: "explode",
		            duration: 1000
		        },
		        buttons : {
		            "OK": function() {
		                $( this ).dialog( "close" );
		            },
		            Cancel: function() {
		                $( this ).dialog( "close" );
		            }
		        }
		    });
		
		    $( "#opener" ).button().click(function() {
		        $( "#dialog" ).dialog( "open" );
		    });
		</script>

##### jQuery UI Tabs页签
- Tabs Widget是一种多面板的单内容区，每个面板与列表中的标题相关。
- ````$( "#tabs" ).tabs();````

##### Tooltip Widget
- Tooltip Widget可自定义的、可主题化的工具提示框，替代原生的工具提示框。

		<p>
		    <label for="age">Your age:</label>
		    <input id="age" title="We ask for your age only for statistical purposes.">
		</p>
		<script>
		    $( document ).tooltip();
		</script>

##### jQuery UI  Menu 菜单
- 带有鼠标和键盘交互的用于导航的可主题化菜单
- ````$( "#menu" ).menu();````

##### jQuery UI  Progressbar 进度条
- 显示一个确定的或不确定的进程状态
- ````$( "#progressbar" ).progressbar({});````

##### jQuery UI  Slider  滑块
- 滑槽滑块
```` $( "#slider" ).slider();````

##### jQuery UI tab键提示信息
- 悬停在链接上，或者使用 tab 键循环切换聚焦在每个元素上。
- ````$( document ).tooltip();````

##### jQuery UI  Spinner 旋转器
- 通过向上/向下按钮和箭头键处理，为输入数值增强文本输入功能。
- ````$( '#spinner').spinner();````

##### Menu Widget

Menu Widget带有鼠标和键盘交互的用于导航的可主题化菜单。

*   禁用页面中默认的鼠标右键功能。

		
		$(document).contextmenu(function (event) {
		    event.preventDefault();
		});



*   自定义鼠标右键菜单。


		$(document).mousedown(function (event) {
		    if(event.button == 2){
		        $( "#menu").removeAttr("style").menu().position({
		            my: "left top",
		            at: "left top",
		            of : event,
		            collision: "fit"
		        });
		    }
		});

![](http://i.imgur.com/zhmd2OO.png)