## 数据库大简介

##### 数据存储基本分类
- 内存(内部存储)
	- 特点：速度速度快，掉电数据丢失 (电)
- 外存(外部存储)
	- 特点：速度慢，掉电数据不丢失 (磁)
	- 硬件发展 
		- 纸带
		- 磁带，磁鼓
		- 硬盘 
		- 软盘
		- 光盘
		- u盘
		- ssd
	
##### 数据管理技术的发展过程
- 人工管理阶段(20世纪40年代中--50年代中)
	- 硬件水平	纸带、磁带、无存储设备
	- 软件水平	没有操作系统，只有汇编语言
- 文件系统阶段(20世纪50年代末--60年代中)
	- 硬件水平：磁盘、磁鼓	
	- 软件水平：操作系统和文件系统
- 数据库系统阶段(20世纪60年代末--现在)
	- 硬件水平：磁盘	
	- 软件水平：操作系统和数据库管理系统

##### 数据库（data base）
**关系型数据库 (二维表)**

- 表结构存储的数据. 列的数量固定, 数据类型固定
- 有模式的
- mySQL， SQLserver, oracle(甲骨文)
- SQL 专门用来操作数据库

**非关系型数据库**

- No SQL
	- 很多种，其中一种是 mongodb 
- 没有表结构，也就是没有模式

----------

### No SQL (Not Only SQL)
- 数据库高并发读写的需求
- 海量数据的高效率访问的需求
- 高可扩展性和高可用性的需求

#### 主要有这些特点：
- 非关系型的、 
- 分布式的、
- 开源的、
-水平可扩展的。

----------

## MongoDB
1. 基于分布式文件存储的数据库
2. 介于关系数据库和非关系数据库之间的产品
3. 支持的数据结构非常松散. 可存储比较复杂的数据类型. BSON格式
4. 高性能、易部署、易使用，存储数据非常方便。
5. 模式自由
6. 实时的增删改查

#### 适用场合:
1. 网站数据: MongoDB非常适合实时的插入、更新与查询， 并具备网站实时数据存储所需的复制及高度伸缩性。
2. 缓存：由于性能很高，MongoDB 也适合作为信息基础设施的缓存层
3. 大尺寸，低价值的数据：使用传统的关系型数据库存储一些数据时可能会比较昂贵，在此之前，很多时候程序员往往会选择传统的文件进行存储。
4. 高伸缩性的场景：MongoDB 非常适合由数十或数百台服务器组成的数据库。
5. 用于对象及JSON数据的存储：MongoDB 的BSON数据格式非常适合 文档化格式的存储及查询。

#### 不适合场合:
1. 高度事务性的系统:银行或会计系统
2. 传统的商业智能应用
3. 需要SQL的场景
事务：一系列操作，要么都做要么都不做，如果中间被打断或操作失败，就回滚到初始状态，重新运行

----------
![](http://i.imgur.com/63b3NSW.jpg)

mongo.exe  客户端

mongod.exe 启动mongoDB的服务

mongoimport.exe 导入文件

----------

## MongoDB 三层操作:
##### 数据库级操作   database
##### 集合类操作  collection
##### 文档级操作 document
![](http://i.imgur.com/JDQlpHu.jpg)
![](http://i.imgur.com/eg0QmAm.jpg)

#### 数据库级操作   database

	查看mongo
	- mongo
	Help查看命令提示
	- db.help();
	切换/创建数据库
	- use dbName 当创建一个集合的时候会自动创建当前数据库
	查询所有数据库 
	- show dbs;
	删除当前使用数据库 (慎用)
	- db.dropDatabase();
	修复当前数据库
	- db.repairDatabase();
	查看当前使用的数据库
	- db.getName();
	显示当前db状态
	- db.stats();
	查看当前db的链接机器地址
	- db.getMongo();



#### 集合类操作  collection

	创建一个集合
	- db.createCollection(“collName”);
	得到指定名称的集合
	- db.getCollection("account");
	得到当前db的所有集合
	- db.getCollectionNames();
	- show collections(集合名)
	显示当前db所有集合的状态
	- db.printCollectionStats();
	删除集合 (慎用)
	- db.collectionNames.drop()


#### 文档类操作 document
**ObjectID**

MongoDB 要求每一个Document必须有 _id 字段并且这个字段必须唯一
ObjectId是"_id"的默认类型。ObjectId 使用12字节的存储空间，每个字节二位十六进制数字，是一个24位的字符串
![](http://i.imgur.com/534IJXX.jpg)

**数据文件和内存**

1. MongoDB每个数据库都有自己的独立文件。
2. 每个库由一个名字空间文件和多个数据文件组成
	- 名字空间文件以 .ns 结尾
	- 数据文件按照数据量大小由0开始增长
	- 第一个数据文件为64M，翻倍增长直至2G

3. 数据库启动后会产生一个6bytes的mongd.lock数据文件，用于防止同一个实例多次运行，非正常退出后需要删除此文件才能重启成功。

![](http://i.imgur.com/QQKrRxp.png)


----------


## MongoDB  CRUD  
##### C reate new records  增
##### R retrieve existing records  查
##### U pdate existing records  改
##### D elete existing records  删

#### BSON
- JSON-like ： field and value pairs.
- BSON 是 json 的二进制表现形式，但是有更多的类型信息

#### 类型：
- 任何 BSON 类型，例如：Double, String, Array, Binary data
- other documents, arrays, 或者 arrays of documents

#### Document
- Collection 里面存的是 Document 
- Document 的具体表现方法就是 BSON

----------

#### 读的基本逻辑
1. 从db对象中获取collection
2. 对collection对象调用find函数
3. 明确查询条件
4. 调整结果集
![](http://i.imgur.com/S3bGnZo.png)
![](http://i.imgur.com/nyRXrr1.jpg)

#### 写(改)数据的基本逻辑
1. 修改数据逻辑:insert, update, delete data
2. 修改数据作用于 collection
3. 插入新数据
![](http://i.imgur.com/bQdIKxz.png)
![](http://i.imgur.com/dbvGXv2.png)
![](http://i.imgur.com/fUJoBO1.jpg)
![](http://i.imgur.com/ARGSun6.jpg)


####  增加Create
- db.collection.insert()
- Mongodb 要求每个 Document 必须有一个唯一的 _id field
- 如果程序员没有设置 _id，那么系统自动加入，使用的是一个唯一的 ObjectId
- 如果程序员自己设置了 _id ，那么程序员必须保证这个值唯一

![](http://i.imgur.com/36RhF5K.png)

注意:MongoDB 是基于文档的所以没有列名的约束，即使每个 document 中的数据都不同，也是可以插入的。因为ObjectId不同

----------


#### 删除Delete
- db.collection.remove()
- 默认删除所有符合条件的Document

![](http://i.imgur.com/eBBXClZ.png)

删除所有数据(慎重)

- db.jobs.remove({})

只删除一个

- db.jobs.remove( { job_id: “GG" }, 1 )
- 如果 justOne 为 true那么就是只删除一个{justOne:true}

删除符合条件的数据

- db.inventory.remove({ job_id: “GG" })

      
#### 修改Update
- db.collection.update()三个参数

#### 查询条件
- 修改内容前缀条件
	- $inc  递增
	- $rename 重命名
	- $set 修改某个 field(域) 字段的值
	- $unset 删除 field(域)
	- $min 比较并取得最小值
	- $max 比较并取得最大值
	- **没有前缀条件会把整个内容全部替换. 慎重!**
- 修改约束
 - multi:true  修改多个
 - upsert:true 符合条件就修改
 
![](http://i.imgur.com/2jtr9zK.png)

- 以上示例: 找到所有age大于18的users, 把status设置为A
### 查询Retrieve
- db.collection.find() 
#### 参数
- query criteria  -- 查询条件
- projections  -- 投影（显示的列）
	- 1(true) 显示
	- 0(false) 不显示
	- db.jobs.find({},{job_id:1, job_title:1, _id:0})
- 返回值
	- Cursor  -- 游标

可以继续调用函数 limits, skips, and sort orders.

#### 查询所有元素
- db.collection.find()
- db.collection.find({})

#### 常用查询之比较判断

	$gt	大于
	- db.jobs.find({job_id:'GG', min_salary:{$gt:4}}
	
	$gte	大于等于
	- db.jobs.find({job_id:'GG', min_salary:{$gte:4}})
	
	$lt	小于
	- db.jobs.find({job_id:'GG', min_salary:{$lt:4}})
	
	$lte	小于等于
	- db.jobs.find({job_id:'GG', min_salary:{$lte:4}})
	
	$ne	不等于
	- db.jobs.find({job_id:'GG', min_salary:{$ne:4}})
	
	$in	在…中
	- db.jobs.find({job_id:'GG', min_salary:{$in:[4,5]}})
	
	$nin	不 在…中
	- db.jobs.find({job_id:'GG', min_salary:{$nin:[4,5]}})


#### 常用查询之逻辑判断 (写在数组里)
- $or	 逻辑或
- $and 逻辑与
- $not 逻辑非 
- $nor 逻辑或非


		$or
		找到 job_id 是 ’GG’ ,  并且(min_salary小于等于2， min_salary大于等于4)
		db.jobs.find({job_id:'GG', $or:[{min_salary:{$lte:2}}, {min_salary:{$gte:4}}]})
		
		$and
		db.jobs.find({$and:[{job_id:'GG'}, {min_salary:{$gt:2}}, {min_salary:{$lt:5}} ]})
		db.jobs.find({job_id:'GG', min_salary:{$gt:2}, min_salary:{$lt:5}})
		
		$and&$or
		db.jobs.find({$and:[{job_id:'GG'}, {$or:[{min_salary:{$lte:2}}, {min_salary:{$gte:4}}]}]})
		
		$not
		- 执行逻辑NOT运算，选择出不能匹配表达式的文档 ，包括没有指定键的文档。
		- $not操作符不能独立使用，必须跟其他操作一起使用（除$regex）
		db.jobs.find({min_salary:{$not:{$gt:10000}}})
		
		$nor
		- 执行逻辑NOR运算,指定一个至少包含两个表达式的数组，选择出都不满足该数组中所有表达式的文档。
		db.jobs.find({$nor:[{job_id:'GG'}, {job_id:'IT_PROG'}]})



#### 常用查询之存在判断

查询是否存在$exists

- true 选择存在该字段的文档；
- false 选择不包含该字段的文档


		db.jobs.find({job_desc:{$exists:true}})
		//选择所有文档,选出的文档符合job_desc存在
		
		db.jobs.find({job_desc:{$exists:flase}})
		//选择所有文档,选出的文档符合job_desc不存在


查询null

- 配合 $in 和 $exists 来查询 null
- 必须两个逻辑同时存在

	
		db.jobs.find({$and:[{job_desc:{$exists:true}}, {job_desc:{$in:[null]}}]})
		//首先选出文档符合job_desc存在的.并且job_desc的值在null的范围内
		
		解释：必须两个逻辑同时存在
		如果只有 $exists , 那么所有存在job_desc字段的document 都被查出来了
		如果只有 $in， 那么所有不存在 job_desc 字段的document 都被查出来了
		不存的字段也是null


#### 常用查询之查询数组
例子: db.jobs.find({work_day:{$in:[3, 4]}})

**查询某个位置的值**

1. 使用 . 运算符
2. 使用 ‘’ 引起来

db.jobs.find({"work_day.1":2})

**$all**
在数组中指定包含条件所有的
{ field: { $all: [ <value> , <value1> ... ] }

**$size**
数组查询指定长度的数组
{field: {$size: value} }

#### 常用查询之其他
$where

操作符功能强大而且灵活，他可以使用任意的JavaScript作为查询的一部分,包含JavaScript表达式的字符串或者JavaScript函数

$regex

操作符查询中可以对字符串的执行正则匹配。 MongoDB使用Perl兼容的正则表达式（PCRE)库来匹配正则表达式.


#### 常用查询之内嵌文档查询

- 精确匹配内嵌文档
- 每一个字段都要匹配
- 顺序也要匹配. 十分严格
- 相等匹配内嵌文档
- 使用 . 符号查询下面的内嵌文档


----------

### 游标 cursor

**指向结果集的指针**

**可以只用游标来遍历结果集**

**有效期: 10分钟**

**db.collection.find() 返回值就是一个游标**

**懒加载:**

- 在命令行中如果不使用一个变量存储游标，默认会自动显示前20个Document
- 使用 DBQuery.shellBatchSize 修改默认数量
- 输入 it 之后 命令行会返回接下来的20个Document



注意:如果程序员第二次使用这个cursor，那么没有返回值，因为cursor已经迭到最后，所以没有输出

**处理游标的函数**

cursor.hasNext()	检查是否有后续结果

cursor.next()	取得下一个 Document

![](http://i.imgur.com/OhnnLHY.jpg)

#### 处理游标的三个函数 sort ，skip， limit
这三个函数可以组成方法链式调用的形式.返回的都是cursor对象

**sort**

得到的子集合进行排序，可以按照多个键进行正反排序

sort的参数是一个对象

- key表示需要排序的字段
- value表示排序是升序还是降序 

sort({document:1})//正数是升序，负数是降序

**skip**

忽略前面的部分文档，如果文档总数量小于忽略的数量，则返回空集合
注意: 由于性能原因，尽量不要使用skip略过大量数据

**limit**

限制游标返回的数量，指定了上限


#### 游标处理分页效果
Sort 

Skip((页数-1)*每页的条目数量)   页数从1开始计数

Limit(每页的条目数量)


	正序排列. 每三个一页 从第0个起
	db.collection.find({},{}).sort({min_salary:1}).skip((1-1)*3).limit(3)
	db.collection.find({},{}).sort({min_salary:1}).skip((2-1)*3).limit(3)
	db.collection.find({},{}).sort({min_salary:1}).skip((3-1)*3).limit(3)
	db.collection.find({},{}).sort({min_salary:1}).skip((4-1)*3).limit(3)


----------

## mongoose
### 简介

- **Mongoose 是MongoDB的一个对象模型工具，是 nodejs 操作 MongoDB 的第三方框架**，可以在异步的环境下执行。

- 同时它也是针对MongoDB操作的一个对象模型库，封装了MongoDB对文档的的一些增删改查等常用方法，让NodeJS操作Mongodb数据库变得更加灵活简单。

### 安装&引用&使用

- 安装mongoose：

		npm install mongoose

- 引用mongoose：

		var mongoose = require("mongoose");

- 发起连接

		mongoose.connect('mongodb://127.0.0.1:27017/xxx');

- 当出错的时候

		connection.on('error',function (err) {
	  		console.error(err);
	 	 });

- 当打开的时候

		connection.on('open',function () {
  			console.log('连接成功');
	  	});

----------

### mongoose核心概念
1. Schema : 模式，规范
2. Model ： 模型，函数
3. Entity ： 实体，实例，对象

----------
### schema
#### 含义:

- 一种以文件形式存储的数据库模型骨架
- 规定了数据的name和value格式
- 不具备操作数据库的能力
- 其实就是一种数据存储格式(相当于表格头部信息)

		var PerSchema = new mongoose.Schema({
		  name:String,
		  age:Number,
		  gender:{type:Number,default:1},  //default的参数是默认值
		  address:String,
		  uniqueSkill:String
		});


----------

### model

操作数据库.映射到数据库的表

- 第一个参数: 集合名称
- 第二个名称: 集合的schema结构对象

		//创建Model  表体内容 
		var PersonModel = mongoose.model('person',PerSchema);


----------

### entity
- 由 Model 创建的实体指代某一条具体的文档
- 通过实例把内存中的对象保存到数据库中
- 和model一样都是操作数据库的

		var xxxEntity = new PersonModel(xxx);


----------
## mongoose的增删改查
### 增 create/save
- **model层的方法**
	- **Model.create(文档数据, callback)**
	

			var zrc = {
			  name:'zrc',
			  age:24,
			  gender:1,
			  address:'bj',
			  uniqueSkill:'html5'
			};
			
			PersonModel.create(zrc,function (err,doc) {
				if(err){
				    console.error(err);
			    }else{
				    console.log(doc);
			    }
			});



- **entity层的方法**
	- **Entity.save( callback )**

			var lwd = {
			  name:'lwd',
			  age:24,
			  address:'fj',
			  uniqueSkill:'piano'
			};
			
			var lwdEntity = new PersonModel(lwd);
			
			lwdEntity.save(function (err,doc) {//把内存中的对象保存到数据库中
			  if(err){
			    console.error(err);
			  }else{
			    console.log(doc);
			  }
			});


----------
### 删 remove
- **model层的方法**
	- **model.remove(查询条件,callback);**

			
			//查询条件
			var query = {
			  name :'qqq'
			};
			
			PersonModel.remove(query,function (err,doc) {
				if(err){
			      console.error(err)
			    }else{
				    console.log(doc);
			    }
			});


- **entity层的方法**
	- **entityObj.remove( callback )**

			
			mongoose给每个对象添加一个_id. 再通过_id找到对应对象进行增删改查
			由于model的回调函数中的doc是entity类型.所以可以利用以下方式删除
			映射的是内存中的doc.删除的是硬盘里数据库的doc
			
			PersonModel.findById('58de1299e8397f3f0c97b498',function (err,doc) {
				  if(err){
				    console.error(err)
				  }else{
				    console.log(doc); //entity类型.
				    doc.remove(function (err,doc) {//删除该ID
				      if(err){
				        console.error(err)
				      }else {
				        console.log(doc); //这是保留在内存中的doc
				      }
				    });
			  	}
			  });


----------
### 改 update/save
- **model层的方法**
	- **modelObj.update(查询条件, 更新对象, callback);**

			
			//查询条件
			var query = {
			  name :'aaa'
			};
			
			//更新对象
			var updateObj = {
			  $set:{
			    age:3
			  }
			};
			
			//model层修改  obj.update(查询条件,更新对象,回调函数)
			PersonModel.update(query,updateObj,function (err,doc) {
			  if(err){
			    console.error(err)
			  }else{
				console.log(doc)
			 }
			});
			````
			- **entity层的方法**
				- **entityObj.save(callback);**


- **entity层修改**

		PersonModel.findById('58de12afeadb1b3df4b47888',function (err,doc) {
		  if(err){
		    console.error(err)
		  }else{
		    doc.age = 20; //1. 先在内存中赋值
		    doc.save(function (err,doc2) {//2. 把doc的内存写进数据库中
		    	if(err){
		    	    console.error(err);
		        }else{
		    	    console.log('修改了');
		    	    console.log(doc2);//3.新的内存同步到数据库中
		        }
		    });
		  }
		});


----------
### 查 find
- **find查询(所有查询 或 条件查询)**
	- model.find(查询条件, 过滤条件(投影), callback(err,docs));
- 回调函数中的返回值是一个数组


		//find查询所有数据
		PersonModel.find({},function (err,docs) { //错误优先
		  if(err){
		    console.error(err);
		  }else{
		    console.log(docs); //docs返回值是一个数组类型.数组里是一个entity对象
		  }
		});
		
		//find查询某一条件的数据
		PersonModel.find({name:'zrc'},{_id:0,name:1,age:1},function (err,docs) {
		  if(err){
		    console.error(err);
		  }else{
		    console.log(docs);//返回值仍旧是一个数组
		  }
		});


- **findOne 单条查询**
 - model.findOne(查询条件, 过滤条件(投影), callback(err,doc));
 - 回调函数返回值是一个对象


			PersonModel.findOne({name:'lwd'},{_id:0,name:1,age:1},function (err,doc) {
			  if(err){
			    console.error(err);
			  }else{
			    console.log(doc);//findOne 返回值是一个对象. 如果有多个则取第一个数据
			  }
			});


- **findById 根据ID查询**
	- model.findById (_id, callback);
	- 找不到id时返回为null. 既为空值.


			PersonModel.findById({_id:'58de125ccf84a33808fffd73'},function (err,doc) {
			  if(err){
			    console.error(err);
			  }else{
			    console.log(doc);
			  }
			});
			
			//findById不写_id也可以
			PersonModel.findById('58de125ccf84a33808fffd73',{age:0},function (err,doc) {
			  if(err){
			    console.error(err);
			  }else{
			    console.log(doc);//findById 返回值是一个对象.
			  }
			});


----------
### 查询条件
- **"$lt"**(小于)
- **"$lte"**(小于等于)
- **"$gt"**(大于)
- **"$gte"**(大于等于)
- **"$ne"**(不等于)
- **"$in"**(可单值和多个值的匹配)
- **"$or"**(查询多个键值的任意给定值)
- **"$exists"**(表示是否存在的意思)


		//查询所有nage大于18的数据
		MonsterModel.find({"age":{"$gt":18}},function(error,docs){});
		
		//查询所有nage小于60的数据	
		MonsterModel.find({"age":{"$lt":60}},function(error,docs){});
		
		//查询所有nage大于18小于60的数据		
		MonsterModel.find({"age":{"$gt":18,"$lt":60}},function(error,docs){});
		
		//查询age不等于24的所有数据
		MonsterModel.find({age:{ $ne:24}},function(error,docs){});	
		
		//查询name不等于tom、age>=18的所有数据
		MonsterModel.find({name:{$ne:"路人甲"},age:{$gte:3}},function(error,docs){});
		
		//查询age等于20的所有数据
		MonsterModel.find({age:{$in:2}},function(error,docs){});
			
		//可以把多个值组织成一个数组	
		MonsterModel.find({age:{$in:[2,3]}},function(error,docs){}); 
		
		//查询name为yaya或age为28的全部文档
		MonsterModel.find({"$or":[{"name":"yellowBrow"},{"age":500}]},function(error,docs){});
		
		//查询所有存在name属性的文档
		MonsterModel.find({name: {$exists: true}},function(error,docs){});
		
		//查询所有不存在telephone属性的文档
		MonsterModel.find({telephone: {$exists: false}},function(error,docs){});


----------
### mongoose 游标
- model.find()的返回值就是游标
- 游标可以做一些翻页的动作


最常用的查询选项就是限制返回结果的结果数量(limit函数)、忽略一点数量的结果(skip函数)以及排序(sort函数)。

### 游标的三大函数

##### sort 函数代表排序的方向，1是升序，-1是降序。
- 方法：find(Conditions,fields,options,callback);
- 参数:
	- 查询条件 
	- 投影(1为显示,0为不显示)    
	- sort函数排序 
	- 回调函数
- 代码：

		//查询所有数据，并按照age降序顺序返回数据docs
		Model.find({},null,{sort:{age:-1}},function(err,docs){});


##### skip 函数跳过指定数量的匹配结果，返回余下的查询结果。
- 方法：find(Conditions,fields,options,callback);
- 参数:
	- 查询条件 
	- 投影(1为显示,0为不显示)  
	- sort函数排序 
	- 回调函数
- 代码;

		// 如果查询结果数量中少于4个的话，则不会返回任何结果。
		Model.find({},null,{skip:4},function(err,docs){
	    		console.log(docs);
		});
			

##### limit 函数 限制结果数量
- 方法：find(Conditions,fields,options,callback);
- 参数:
	- 查询条件 
	- 投影(1为显示,0为不显示)  
	- sort函数排序 
	- 回调函数
- 代码：

		// 如果匹配的结果不到20个，则返回匹配数量的结果，也就是说limit函数指定的是上限而非下限。
		Model.find({},null,{limit:20},function(err,docs){
    			console.log(docs);	
		});
		
