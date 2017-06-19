## JSON & XML

#### JavaScript Object Notation

1.javascript对象标记

2.具有特定格式的字符串

3.对应的一种文件  xxx.json


#### Extensive Markup Language

1.可扩展标记语言

2.对应的一种文件: xxx.xml


**json和xml相同点:**

1. 具有层级结构. 保存结构化数据
2. 可通过JavaScript解析
3. 数据可通过AJAX 进行传输
4. 纯文本. 独立于特定的语言
5. 可在网络上传输 (客户端发送服务器, 服务器返回客户端)
6. 可做配置文件
7. 具有"自我描述性" (人类可读)

**json优势:**

1. 体积更小

2. 节省带宽

3. JS操作更方便


----------

### JSON
- 名值对必须是双引号的字符串. 
- 不允许有注释

**JSON类型**

(key类型是字符串. value可以是num,str,bool,null,{},[])

1. 对象{key1 : value1, key2 : value2}
2. 数组[value1, value2] 

**JSON工具对象**

object parse(json)   json字符串转obj对象

	var obj = JSON.parse(str);

string stringify(object)  obj对象转成jason字符串

	var srt = JSON.stringify(obj)


**json 字符串与 js对象**

区别:

1. json是符合某种规范格式的字符串
2. js对象是堆空间中的一段内存

联系:

1. 存储的信息相同
2. 规范很像
3. 非常容易互相转化
