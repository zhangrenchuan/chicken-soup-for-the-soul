## AJAX请求

**1.采用异步方式与后台交互**

2.优点

- 无需刷新整个页面, 减少用户等待时间 (用js语言控制html 局部刷新页面)
- 减轻服务器的负担，AJAX一般只从服务器获取只需要的数据
- 节约网络资源，提高用户体验, 将一些服务器的工作转移到客户端完成
- 基于标准化的对象没有兼容性问题，不需要安装特定的插件, 浏览器都支持Ajax
- 彻底将页面与数据分离

3.缺点:

- 没有浏览历史. 不能回退
- 存在跨域请求的问题
- 对搜索引擎支持比较弱

![](http://i.imgur.com/bw7giWQ.png)
![](http://i.imgur.com/eh1UREq.png)


----------
## 原生API
### xmlHttp
XmlHttp是一套可以在Javascript、VbScript、Jscript等脚本语言中通过http协议传送或从接收XML及其他数据的一套API

XmlHttp最大的用处是可以更新网页的部分内容而不需要刷新整个页面

#### xmlhttp 属性
**readyState 当前的请求状态**

0 (未初始化) 对象已建立，但是尚未初始化（尚未调用open方法） 

1 (初始化) 对象已建立，尚未调用send方法 

2 (发送数据) send方法已调用，但是当前的状态及http头未知 

3 (数据传送中) 已接收部分数据，因为响应及http头不全，这时通过responseBody和responseText获取部分数据会出现错误

4 (完成) 数据接收完毕,此时可以通过通过responseBody和responseText获取完整的回应数据 

xmlHttp.onreadystatechange = function (){}该函数会执行四次


**responseText**

将响应信息作为字符串返回

**responseXML**

将响应信息格式化为Xml Document对象并返回

**status**

返回当前请求的http状态码

- 200: "OK"
- 304: Not Modified
- 404: 未找到页面
- 500: Internal Server Error
 

#### xmlhtp 方法
**open()**
创建一个新的http请求，并指定此请求的方法、URL以及验证信息

接收三个参数:

1. 请求方法 (get/post) httpMethod
2. 发给服务器的文件路径 httpUrl
3. 是否异步发送  默认为true 

**send()**
发送请求到http服务器并接收回应

注意: 

1.post请求必须要在发送前设置请求头
xmlHttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");

2.post请求可以在send()内发送数据内容
xmlHttp.send('username=zrc&password=123');


**abort()** 取消当前请求

XMLHttpRequest.abort();



----------

### 原生API 具体操作
##### 1.建立XMLHttpRequest对象
	window.onload = function(){
		document.getElementById('btn').onclick = function(){
			var xmlhttp;
			if (window.XMLHttpRequest){// code for IE7+, Firefox, Chrome, Opera, Safari
				 xmlhttp=new XMLHttpRequest();
			} else { // code for IE6, IE5
				 xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
			}
		}	
	}
	

也可以封装成一个方法进行调用
	
	function createXmlHttp() {
	  var xmlHttp  = null;
	  if(window.XMLHttpRequest){
	    xmlHttp = new XMLHttpRequest();
	  }else{
	    xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
	  }
	  return xmlHttp;
	}

	var xmlHttp = createXmlHttp();

##### 2.设置回调监听

      xmlHttp.onreadystatechange = function () {
  	  if(xmlHttp.readyState === 4 && xmlHttp.status ===200){
        var result = xmlHttp.responseText;

        //把服务器的返回值显示在页面上
        document.getElementById('btnID').innerHTML = result;
		
		//将服务器返回的结果打印到控制台
        console.log(result);
      }
  	};

##### 3.发送get请求
	//准备发送
	xmlHttp.open('get','/node_ajax/test/get?username=zrc'); 

	//真实发送
	xmlHttp.send();
##### 4.发送post请求
	  //准备发送
	  xmlHttp.open('post','/node_ajax/test/post');
	
	  //post必须需要设置请求头
	  xmlHttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	
	  //真实发送
	  xmlHttp.send('username=zrc&password=123');


----------

## 异步和同步的区别

request.open(method, url, async)  第三个参数:是否异步发送

async 异步 默认为true

sync   同步 设置为false

**区别:**

1.异步: 

- send()方法立即返回, 后面立即获取请求结果但数据(responseText)得不到
- 只能在监听回调中获取(当结果数据返回后回调函数执行)

2.同步: 

- send()方法不会立即返回, 只有在服务器返回结果后才返回
- 在后面可以直接获取返回的结果数据(responseText), 没有必要再设置监听回调