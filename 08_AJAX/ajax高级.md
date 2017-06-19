## AJXA 高级

**var xhr = new XMLHttpRequest();**

**设置 response 的类型**

- 属性 responseType
- 属性值 
	- 默认值:＂＂ String类型
	- "text" String类型
	- "document" Doument对象类型.返回xml格式使用
	- "json" javascript对象类型. IE不支持
	- "blob" Blob对象类型
	- "arrayBuffer" ArrayBuffer对象类型
- 例子: 
		
		//设置请求返回数据的类型为二进制类型数据
		xhr.responseType = 'blob';  

**获取 response 的数据**

- xhr.response
	- 默认值为空字符串  ""
	- 当请求完成时该属性才有正确的值
- xhr.responseText
	- 默认值为空字符串  ""
	- 只有当 responseType 为"text"或者""时，此属性才能被读取.否则报错
-  xhr.responseXML
	-  默认值为 null
	-  该类型不常用
	- 只有当 responseType 为"text"或者""或者"document"时，此属性才能被读取. 否则报错
	
**报文首部字段**

- 设置请求报文首部字段
	- xhr.setRequestHeader('content-type', 'xxx');
- 获得响应报文首部字段
	- xhr.getResponseHeader('Content-Type:'); 
	- 可能的返回值 : video/x-ms-wmv
	
### AJAX 高级事件系统
**服务器上传数据**

- 附着在 xhr.upload 对象上
- 七大事件
	-  xhr.upload.onloadstart 
	-  **xhr.upload.onprogress** 
		-  每50ms触发一次 
		-  上传数据时触发
		-  xhr.send()之后 xhr.readystate=2之前
		-  此时 xhr.readyState == 1
	-  xhr.upload.onabort 清除
	-  xhr.upload.timeout 超时
	-  xhr.upload.error 出错
	-  **xhr.upload.load** 完成 
		-  上传完成.完全上传完数据时触发 此时xhr.readyState == 1
	- xhr.upload.onloadend 结束


**从服务器下载**

- 附着在 xhr 对象本身上
- 七大事件
	-  xhr.onloadstart 调用send()后触发. 此时readyState == 1
	-  **xhr.onprogress** 
		-  每50ms触发一次 
		-  下载数据时但未完成时触发
		-  xhr.send()之后  readystate=3之后readystate == 4之前
		-  此时 xhr.readyState == 3
	-  xhr.onabort 清除
	-  xhr.timeout 超时
	-  xhr.error 出错
	-  **xhr.load** 完成
		-  下载完成.完全获得服务器数据时触发 此时readyState == 4
	- xhr.onloadend 结束

**readyState 的切换事件**

- 附着在 xhr 对象上
- onreadystatechange 
- readystate状态改变时执行. 总共执行四次

**事件的触发顺序**

![](http://i.imgur.com/BM0WVHw.png)
