## ECMAScript
- 它是一种由ECMA组织（前身为欧洲计算机制造商协会）制定和发布的脚本语言规范
- JavaScript是ECMA的实现
- ECMAScript和JavaScript平时表达同一个意思

#### JS包含三个部分：
- ECMAScript（核心）
- 扩展==>浏览器端
	* BOM（浏览器对象模型）
	* DOM（文档对象模型）
- 扩展==>服务器端
	* Node
	

#### ES的几个重要版本
- ES5 : 09年发布
- ES6(ES2015) : 15年发布, 也称为ECMA2015
- ES7(ES2016) : 16年发布, 也称为ECMA2016  (变化不大)

----------


#### 编写位置
1. 编写到标签指定属性中. 
	- 会造成结构和行为的耦合
	- 不方便后期维护 不推荐使用
2. 使用````<script>````标签创建JS代码区
	-  ````<script type="text/javascript"></script>````
3. 编写在外部js文件里.通过````<script>````标签引入
	-  ````<script type="text/javascript" src="js/new_file.js"></script>````

#### 注释
- 多行注释(不可被嵌套)  /**/
- 单行注释 //

#### JS输出
- 浏览器弹框
	- ````alert("")````
- 控制台输出内容
	- ````console.log()````
- 控制浏览器页面输出内容
	- ````document.write()````
- 开启定时器
	- ````console.time()````
- 停止定时器
	- ````console.timeEnd()````