## Express
基于Node.js平台 快速, 开放, 极简的轻量级web开发框架

多数功能只是对HTTP协议中常用操作的封装，更多功能需要插件或整合其他模块来完成

#### 框架的好处:
1. 节省创建一个项目所需的时间
2. 封装公共逻辑, 减少开发量, 使用方便
3. 社区维护. 每个人都可以贡献自己的经验

省时省力.高效快捷 Express就是快的意思

## Express核心特性:
- 接收：设置中间件来响应 HTTP 请求 (请求报文)
- 处理：定义了路由用于执行不同的 HTTP 请求动作 (路由\计算)
- 返回：通过向模板传递参数来动态渲染  HTML 页面 (生成动态页面)

### 网站架构 MVC -- Model View Controller
- Model（模型）通常模型对象负责在数据库中存取数据
- View（视图）　通常视图是依据模型数据创建的网页
- Controller（控制器）从视图读取数据，控制用户输入，并向模型发送数据

思路: 隔离. 三者之间只存在调用关系.内部可以随意修改 接口不变就可以

----------

**Express中的MVC**

Model -- DB

View -- 网页

Controller -- 重点在如何使用Controller和生成视图

----------

#### 安装express
1. npm install -g express-generator 得到Express生成器
2. 当前工作环境下运行命令行  express app4
	- bin  可执行的文件 -- www (核心启动服务器文件)
	- public 对外可以访问的
	- routes 路由 
	- views 视图层的文件



**app4需要依赖的包**

	dependencies: {
	
	"body-parser": "~1.17.1",
	
	"cookie-parser": "~1.4.3",
	
	"debug": "~2.6.3",
	
	"express": "~4.15.2",
	
	"jade": "~1.11.0",
	
	"morgan": "~1.8.1",
	
	"serve-favicon": "~2.4.2"}


3.运行npm install (系统会自动读取package.json中依赖的包依次下载. npm install xxxxx --save 表示把该包添加进依赖包中)

4.运行bin -- www 文件  启动express工程


**app.js**

1. 引入一堆包
2. 引入路由模块
3. 生成express app的实例
4. 设置模版引擎(jade后缀)
5. 使用引入的包
6. 导入路由
7. 向外暴露 new出来的实例app(www引入了app)

----------

#### 静态资源服务
静态文件就是不在程序运行动态变化的文件，将来会直接发送给浏览器。

例如：图片，css 文件等

**app.js中 以下代码设置静态资源服务**
app.use(express.static(path.join(__dirname, 'public')));

- app.use() 调用函数
- static() 静态资源的
- path 进行文件路径解析和拼串
- .join拼接
- (__dirname, 'public') 
	- 第一个参数 当前的工作目录
	- public 实际指的就是对外暴露静态资源public的文件夹
	
原理: 通知服务器 所有的静态资源都在'public'文件夹中了

index 就表示首页 

----------


## 路由
- 定义应用的端点（URIs）以及如何响应客户端的请求。
- 路由是由一个 URI、HTTP 请求和若干个句柄组成
- 它的结构如下：
	````app.METHOD(path, [callback...], callback)````
 - app 是 express 对象的一个实例
 - METHOD 是一个 HTTP 请求方法 （GET、POST等）
 - path 是 url 的文件路径
 - callback 是当路由匹配时要执行的函数，这个回调函数提供商业逻辑


### 工作原理
#### 收到请求
第一行 三部分

- 请求方法		get
- 请求路径		/helloworld
- 协议版本		HTTP/1.1

#### 处理请求
- app.get(  '/helloworld',  function(req, res){}  );
	- 第一个参数: 第一个参数: 路径. 
	- 第二个参数 callback(req,res,next){}
- 发送的路径如果是helloworld 则进行逻辑处理.回调函数执行
- 最核心的思想就是**映射** 
- 把一个路径映射到一个服务（函数）

#### 返回请求
- res.render('index', { title: 'hello World' });(end,write)
- 例子: 优先会去public中找  找到index的话直接返回
	
		app.get('/',function (req,res) {
			  res.end('hello')
		})

----------

### 路由分解: 一个路由通常由三部分组成
- 路由方法
- 路由路径
- 路由句柄

路由方法和路由路径构成了请求端点




#### 路由方法
HTTP 协议给出的请求方法

- app.get(path, callback [, callback ...]) 只处理get请求
- app.post(path, callback [, callback ...]) 只处理post请求
- app.all(path, callback [, callback ...]) 处理全部请求

		//all 和 * 最后用404兜底用
		app.all('*',function (req,res) {
	  		res.end('404')
		});
#### 路由路径
url中的文件路径 

1.字符串

````
app.get('/',function (req,res) {
  res.end('root')
});
````
````
app.get('/about.text',function (req,res) {
  res.end('about.text')
});
````

2.字符串模式

	- ? 表示前面的字符可有可无
	- + 表示前面的字符有一个或多个
	- * 表示任意字符
	

````
app.get('/ab?cd',function (req,res) {
  res.end('ab?cd')匹配acd和abcd
});
````
````
app.get('/ab+cd',function (req,res) {
  res.end('ab+cd')匹配abcd或abbcd或abbbcd
});
````
````
app.get('/ab*cd',function (req,res) {
  res.end('ab*cd')匹配abcd或abxcd或abxxxxxcd
});
````


3.正则表达式

````
app.get(/a/,function (req,res) {
  匹配含有a的
 });
````



#### 路由句柄 
- 可以为请求处理提供多个回调函数
	1. 一个回调函数处理路由
	2. 多个回调函数处理路由(需要执行next)

**next('route') 当前请求端点内后面的内容直接跳过.找下一个端点**

    
	app.get('/cai',function (req,res,next) {
	  res.write('maicai');
	  next();
	},function (req,res,next) {
	  res.write('xicai');
	  next();
	},function (req,res,next) {
	  res.write('qiecai');
	  next();
	},function (req,res,next) {
	  res.write('zuocai');
	  next();
	});
	
	app.get('/cai',function (req,res,next) {
	  res.end('chaocai');
	})

3.回调函数数组处理路由 or 混合使用函数和数组处理路由(几乎不用)

![](http://wx1.sinaimg.cn/mw690/824389a9ly1fe7rr1ug1yj208u093q3y.jpg)

![](http://wx2.sinaimg.cn/mw690/824389a9ly1fe7rr2h4swj20e909ldha.jpg)


#### 路由句柄响应方法
 
常用方法

1.res.render()	渲染视图模板。

2.res.redirect()   重定向页面

3.**res.send()	发送各种类型的响应。**

![](http://i.imgur.com/lvcTMEY.png)
![](http://i.imgur.com/mubTnts.jpg)


----------

## 路由场景

**use()使用引入的包或一个函数**

- use表示所有的请求都匹配
- 第一个参数: 匹配路径. 第二个参数 回调函数(路径匹配时执行)
- 文件路径匹配. 如果不写默认就是根目录 '/'
- use属于前导匹配. 以路径最前的一部分整体作为考察的根据.不按照整个字符串匹配

		
		例子: /abc 匹配路径是abc的   /ab 匹配路径是ab的

		var app = express();

		app.use('/abc',function (req,res,next) {console.log('use');});

		app.use('/ab',function (req,res,next) {console.log('use');});


**all()**

- all表示所有的请求都匹配.
- 文件路径匹配的话必须要写'/',否则会出错
- all属于完全匹配 路径的字符串要完全一样

		//all 和 * 最后用404兜底用
		app.all('*',function (req,res) {
		  res.end('404 not found')
		});

**next('route')**

- 跳过剩余路由

		//跳过切菜和做菜直接炒菜.
		app.get('/cai',function (req,res,next) {
		  res.write('买菜');
		  next();
		},function (req,res,next) {
		  res.write('洗菜');
		  next('route');
		},function (req,res,next) {
		  res.write('切菜');
		  next();
		},function (req,res,next) {
		  res.write('做菜');
		  next();
		});
		
		app.get('/cai',function (req,res,next) {
		  res.end('炒菜');
		});


### 路由模块化
- 避免多人同时修改一个文件
- 好处: 
	- 代码管理维护方便
	- 团队合作
	- 可移植性与可扩展性强
- 使用express.Router()创建模块化
	- Router 实例是一个完整的中间件和路由系统，功能相当于app.一般称之为 “mini-app”。

原理: 引入包. 暴露包. 使用包

1. 创建模块文件js  (routes文件下)
  - 静态资源放置在public文件下
2. app.js中引入模块文件js (require) 
3. 模块文件进行暴露
4. 路由模块化用use使用引入包
 	- 前导匹配考察的是路径
	- 导入到模块. 匹配到的路径就被"吃掉"
	- 剩下的路径再去模块文件里寻找
	- 如果不以 / 开头 那么必须以 / 开头


			1.创建模块  //生成router对象
			var express = require('express');
			var router = express.Router(); 
			
			//前导匹配 是wukong则发送语句 
			//router相当于app
			router.get('/wukong',function (req,res,next) {
			  res.send('悟空')
			});
			
			router.get('/bajie',function (req,res,next) {
			  res.send('八戒')
			});
			//暴露
			module.exports = router;

			2.使用模块
			//引入
			var xiyou = require('./routes/xiyou.js');

			//使用
			//第一个参数是匹配路径. 第二个参数是引入包的名字
			app.use('/xiyou',xiyou);
			
**路由思想模型:**

一个路由端点理论上可以有无穷多个句柄（处理函数）

句柄调用的次序就是程序静态编写的次序 需要考虑 next() 和 next('route')
![](http://i.imgur.com/euovsIF.jpg)

----------

**工程需求**

1.显示页面

2.获取用户输入

- 路由处理
- 获得用户的输入数据

3.处理用户数据

- 查询数据库
- 处理计算逻辑

4.返回处理结果

npm install mongoose --save 添加到工程依赖的列表中

----------

## 模版
动态生成HTML. 一个HTML预处理语言

**核心: 拼接替换字符串**
![](http://i.imgur.com/qKhxu8K.jpg)


### ejs 模版引擎
ejs （Embedded JavaScript）
简单，粗暴，有效 嵌入式的js
![](http://i.imgur.com/Pl7hcQ7.jpg)

- 把js代码嵌入到html代码中
- 模版(html框架) + 代码(对象) = 动态生成HTML
- **需要配合res.render()函数. 渲染一个html页面**

````
安装:
进入工作目录 运行命令： npm install ejs -save
````

#### 标签系统语法
- <% code %> 运行JavaScript 代码。

- <%= code %> 替换字串. 没有的会报错
- <%- code %>：显示原始 HTML 内容。

#### 模版步骤

**1.app.set()设置模版所在路径**
		
	app.set('views', path.join(__dirname, 'views'));

**2.设置模版格式**
	
	app.set('view engine', 'ejs');

**3.在views文件夹下创建模版文件.以ejs后缀结尾**

**4.动态生成html**

	app.get('路径',callback(req,res,next)) 
	
	res.render(参数: 1.模版文件  2. 数据(对象格式))



例子1:

	app.get('/',function (req,res,next) {
		res.render('test.ejs',{username:'北京'});
	})
	<%= username %> , 欢迎你

例子2:

	app.get('/',function (req,res,next) {
	  var Oj = {
	    username:"周杰伦",
	    weapon:'唱歌',
	    kouhao:['你发如雪凄美了离别','我焚香感动了谁','邀明月','举杯']
	  };
	  res.render('test1.ejs',Oj);});
	
	<ul>
	    <% for(var i=0;i<kouhao.length;i++){
	        var result = kouhao[i]
	    %>
	        <li> <%= result %> </li>
	    <%
	    }
	    %>
	</ul>

----------
**includes**

原理: 把文件找出来并替换它. 方便管理添加删除数据

<%- include('footer.ejs')%> 

参数 -- 文件路径

例子: 

	<%- include('header.ejs')%>
	姓名:<%= name%>
	<br>
	年纪:<%= age%>
	<br>
	武器:<%= weapon%>
	<br>
	<%- include('footer.ejs')%>

----------
#### 获得用户输入的数据方法

get: 用户的数据在url的queryString里

- req.query.NAME

post: 用户的数据在请求报文的请求体里

- req.body.NAME

数据在 url 的文件路径中

- req.params.id

		//可以利用id去数据库找到数据, 生成网页
		app.get('group/topic/:id',function (req,res,next) {
	  		var id = req.params.id;
	  		res.send('id: '+ id)
		});

#### 服务器返回页面与数据都是动态加入的

1. 后台程序员使用模版的方式注入数据
2. 前端程序员使用ajax的方式获得数据


#### res 返回内容的函数
- res.write()
	- 多次的写入数据
	- nodejs 原生
- res.end()
	- 写完数据,断开连接
	- nodejs原生
- res.send()
	- 转义之后写数据
	- express 提供的
- res.render('xx.ejs',{ })
	- 通过ejs文件渲染页面
	- 第一个参数:ejs文件名. 第二个参数: 对象
- res.redirect('url') 
	- 重定向到一个页面(参数:路径)
- res.download('url','文件名')
	- 下载某文件(第一个参数:路径文件. 第二个参数:重命名该文件)


----------


#### view 层：views 文件夹 (渲染页面)
- ejs 文件

#### control 层：
- routes文件夹  routes_user.js 文件 --- 负责路由跳转
- business_logic 文件夹
	- logic_user.js 文件 --- 负责登录注册逻辑处理
	- logic_item.js 文件 --- 负责用户输入表单逻辑处理
	
#### model 层：
- dao 文件夹
	- db.js 文件 --- 负责数据库的交互
- public --- 展示静态页面
- app.js --- 管理路由. 

安装npm install express app4 / mongoose / ejs
![](http://i.imgur.com/G3Es6tG.png)
----------

## 用户登录注册

**第一步:**

1.routes文件夹创建 routes_user.js 文件 只用来负责路由跳转

2.app.js引入路由文件'routes_user.js' 并使用

	var routesUser = require('./routes/routes_user.js');
	app.use('/',routesUser);

3.'routes_user.js' 启动express和引入db数据库文件
	
	var router = require('express').Router();
	var db = require('../dao/db.js');
	//暴露
	module.exports = router;


4.db.js文件写入正常启动服务器代码(test是数据库名称)

	var mongoose = require('mongoose');
	mongoose.connect('mongodb://127.0.0.1:27017/test');
	var connection = mongoose.connection;
	
	connection.on('error',function (err) {
	  console.error(err);
	});
	
	connection.on('open',function () {
	  console.log('连接成功');
	});
	
	//userSchema创建用户登录注册的表头需要的信息
	var userSchema = new mongoose.Schema({
	  username:String,
	  password:String,
	  email:String
	});
	
	var UserModel = mongoose.model('user',userSchema);
		

**第二步:**

1. business_ logic 文件夹下创建 logic_user.js 文件 负责登录注册逻辑

2. 'routes_user.js' 引入登录注册的逻辑(请求方法区分post和get)
	
		var userLogic = require('../business_logic/logic_user.js');
		router.post('/login',userLogic.postLogin);
		router.post('/register',userLogic.postRegister);

3. logic_user.js 写入登录注册逻辑

		var db = require('../dao/db.js');

		//登录逻辑
		function postLogin(req,res,next) {
		  	var username = req.body.username;
		  	var password = req.body.password;
	
	  	db.findUser(username,function (err,doc) {
		    if(doc){
		      if(password === doc.password){ //密码匹配则登录成功
        		res.send('欢迎回来')
      		  }else{
        		res.send('用户名或密码错误')
     		  }
    		}else{
      			res.send('用户名不存在,请注册')
    		}
		  });
		}
		//暴露登录逻辑
		exports.postLogin = postLogin;


		//注册逻辑
		function postRegister(req,res,next) {
		  var username = req.body.username;
		  var password = req.body.password;
		  var email = req.body.email;
		
		  db.findUser(username,function (err,doc) {
		    if(err){
		      console.log(err);
		    }else{
		      if(doc){
		        res.send('用户名已存在.')
		      }else{
		        db.addUser(username,password,email,function (err) {
		          if(err){
		            console.log(err);
		          }else{
		            res.send('注册成功请返回登录')
		          }
		        });
		      }
		    }
		  })
		}
		//暴露注册逻辑
		exports.postRegister = postRegister;

4. db.js编写对应函数

		//登录时找用户名是否存在
		function findUser(username,cb) {
		  UserModel.findOne({username:username},function (err,doc) {
		  	  if(err){
		        cb(err);
		      }else{
		        cb(null,doc);
		      }
		  })
		}
		exports.findUser = findUser;
		
		
		//没有用户名就直接添加到数据库中
		function addUser(username,password,email,cb) {
		  var addEntity = new UserModel({
		    username:username,
		    password:password,
		    email:email
		  });
		  addEntity.save(function (err) {
		  	  if(err){
		  	    cb(err);
		      }else{
		        cb(null);
		      }
		  });
		
		}
		exports.addUser = addUser;


## 登录后进行表单操作
第三步:

1. business_ logic 文件夹下创建logic_item.js 文件 负责表单操作
2. routes_user.js 引入 logic_item.js

		var itemLogic = require('../business_logic/logic_item.js');
		router.post('/addItem',itemLogic.addItem);

3. db.js文件夹写入表单操作的代码

		var itemSchema = new mongoose.Schema({
		  userID: String,  //关联某个用户
		  title: String,
		  post_date: {type: Date},
		  finish_state: {type: Number, default: 1}
		});
		var itemModel = mongoose.model('item',itemSchema);
		
		//把表单数据添加到数据库中
		function addItem(title,userID,cb) {
		  var itemEntity = new itemModel({
		    userID:userID,
		    title:title,
		    post_date:new Date()
		  });
		  itemEntity.save(function (err,doc) {
		  	  if(err){
		  	    cb(err)
		      }else{
		  	    cb(null,doc)
		      }
		  })
		
		}
		exports.addItem = addItem;
		
		//查找表单内容
		function findItems(userID,cb) {
		  itemModel.find({userID:userID},function (err,docs) {
		  	  if(err){
		  	    cb(err);
		      }else{
		        cb(null,docs);
		      }
		  })
		}
		exports.findItems = findItems;

4. logic_item.js 写入添加表单数据
	
		var db = require('../dao/db.js');
		var userlogic = require('./logic_user');
		
		function addItem(req,res,next) {
		  var title = req.body.title;
		
		  var userID = global.userID;
		  db.addItem(title,userID,function (err,doc) {
		    if(err){
		      console.log(err);
		    }else{
		      userlogic.indexPage(userID,res)
		    }
		  });
		}
		exports.addItem = addItem;

第四步:

1. 实时把新添加的表单内容渲染到页面中
2. views文件夹创建 item_list.ejs (同静态文件html)
3. logic_user.js 修改代码改成登录成功后渲染指定页面
	
	
		db.findUser(username,function (err,doc) {
	    if(doc){
	      if(password === doc.password){
	        var userID = doc._id;
	        global.userID = userID;
	        //渲染用户首页
	        indexPage(userID,res)
	      }else{
	        res.send('用户名或密码错误')
	      }
	    }else{
	      res.send('用户名不存在,请注册')
	    }
	 	});

		function indexPage(userID,res,req) {
		  db.findItems(userID,function (err,docs) {
		    if(err){
		      res.send('出错了')
		    }else{
		      var dataObj = {
		        items:docs,
		      };
		      res.render('item_list.ejs',dataObj)
		    }
		  });
		}
		exports.indexPage = indexPage;

	
4. ejs文件写入如下代码进行页面动态渲染

		<ul>
	        <%
	            for (var i = 0; i < items.length; i++) {
	                var item = items[i];
	
	        %>

	        <li>  
	            <%= item.title%>
	            <a href="/finish/<%= item._id%>/?state=yes">完成</a>,
	            <a href="/edit/<%= item._id%>">修改</a>,
	            <a href="/delete/<%= item._id%>"
	            onclick="return confirm('删除以后不能恢复的，确定？')">删除</a>
	        </li>
	        <%
	        }
	        %>
	    </ul>
