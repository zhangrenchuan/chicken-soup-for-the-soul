## JS模块化
####  模块化理解
- 将一个复杂的程序依据一定的规则(规范)封装成几个块(文件), 并进行组合在一起
- 块的内部数据实际是私有的, 只是向外部暴露一些接口(方法)与外部其它模块通信

#### 模块化好处
- 避免命名冲突(减少命名空间污染)
- 更好的分离. 按需加载
- 部署方便.高复用性.高可维护性

#### 模块化的问题
- 依赖模糊
- 请求过多
- 维护代价大

#### 模块化的历史演变
###### 全局函数模式:将不同的功能封装成不同的全局函数
- 问题: 全局污染.命名冲突.数据可在外部直接修改

        let msg = 'atguigu.com';
        function foo() {
          console.log('fun()' + msg);
        }
        
        function bar() {
          console.log('bar()' + msg);
        }

###### namespace模式: 简单对象封装
- 作用: 减少了全局变量
- 问题: 不安全(数据不是私有的.外部可以修改)

        let obj = {
          msg : 'kobe',
          foo : function () {
          	  console.log('foo()' + msg);
          }
        };

###### IIFE模式: 匿名函数自调用(闭包)
- IIFE : immediately-invoked function expression(立即调用函数表达式)
- 作用: 数据是私有的, 外部只能通过暴露的方法操作
- 可在参数里进行引用依赖:传入需要依赖的JS(比如jQuery)

	      (function (window,$) {
	          let msg = 'atguigu.com';
	          let foo = function () {
	            console.log('foo()' + msg);
	          };
	          $('body').css('background','blue');
	        
	          window.obj =  {foo};
	      })(window,jQuery);  

###### 引入依赖页面加载多个JS文件
- 问题: 请求过多. 依赖模糊. 难以维护



---

## 模块化规范
### CommonJS
- 说明
    1. 每一个文件都可作为一个模块
    2. 在服务器端: 模块的加载是运行时同步加载的
    3. 在浏览器端: 模块需要提前编译打包处理
- 基本语法
    - 暴露模块
        - module.exports = value (暴露的是exprots对象)
        - exprots.xxx = value (暴露的是exprots对象的一个属性)
    - 引入模块
        - require(模块名)  第三方或自带模块
        - require(文件相对路径) 自定义模块
- 实现:
    - 服务器端: NodeJs
    - 浏览器端: browserif 打包工具
- 区别: 
    - Node.js运行时动态加载模块(同步)
    - Browserify是在转译(编译)时就会加载打包(合并)require的模块

---
#### commonJs_node 模块化
1. 项目构建
	- 下载安装第三方模块````npm install uniq --save````
	- uniq模块: 对数组去重并且排序

	        -modules //模块文件
	            |-module1.js
	            |-module2.js
	            |-module3.js
	        - app.js //主文件
	        -package.json
	            {
	              "name": "commonJS-node",
	              "version": "1.0.0"
	            }

2. 进行模块化编码
 - module1.js

		    //module.exports = value 暴露方法
		    module.exports = {
		      foo() {
		        console.log('moudle1 foo()')
		      }
		    }

   - module2.js

		    //module.exports = {} 暴露对象
		    module.exports = function () {
		      console.log('module2()')
		    }

   - module3.js

		    //exports.xxx = value 暴露exports对象的一个属性
		    exports.foo = function () {
		      console.log('module3 foo()')
		    }
		    
		    exports.bar = function () {
		      console.log('module3 bar()')
		    }
    
3. 主文件引入模块

        //引入第三方模块直接写模块名
        let  uniq = require('uniq'); 
        
        //引入自定义模块写相对路径
        let module1 = require('./modules/module1');
        let module2 = require('./modules/module2');
        let module3 = require('./modules/module3');
        
        module1(); //暴露方法直接调用
        module2.foo(); //暴露对象里的方法
        module3.foo(); //暴露exports对象中的方法
        module3.bar();
        
        
        console.log(module3.arr);
        console.log(uniq(module3.arr));

4. 输出结果
    
        module1
        module2
        module3.foo()
        module3.bar()
        [ 1, 2, 3, 4, 6, 8, 8, 9, 5, 6, 3, 2 ]
        [ 1, 2, 3, 4, 5, 6, 8, 9 ]

---
#### CommonJs_Browserify 模块化
1. 下载browserify第三方模块
	- 通过预编译让前端浏览器可以直接使用 Node NPM 安装的一些库
	- 全局安装: npm install browserify -g
	- 当前工作目录下: npm install browserify --save-dev
2. 创建项目结构

          -js
            |-dist //打包生成编译输出文件的目录
            |-src //源码所在的目录
              |-module1.js
              |-module2.js
              |-module3.js
              |-app.js //应用主源文件 入口文件
          -index.html
          -package.json
            {
              "name": "browserify-CommonJs",
              "version": "1.0.0"
            }
3. 进行模块化编码
    - module1.js

		    //module.exports = value 暴露方法
		    module.exports = {
		      foo() {
		        console.log('moudle1 foo()')
		      }
		    }

   - module2.js

		    //module.exports = {} 暴露对象
		    module.exports = function () {
		      console.log('module2()')
		    }

   - module3.js

		    //exports.xxx = value 暴露exports对象的一个属性
		    exports.foo = function () {
		      console.log('module3 foo()')
		    }
		    
		    exports.bar = function () {
		      console.log('module3 bar()')
		    }
4. 主文件引入模块

        let module1 = require('./module1');
        let module2 = require('./module2');
        let module3 = require('./module3');
        
        module1();
        module2.foo();
        module3.foo();
        module3.bar();

5. 打包处理模块文件
	- 命令运行: browserify 源代码主文件 -o 输出文件
	- ````browserify js/src/app.js -o js/dist/bundle.js````
6. HTML页面引入编译后的js文件
	- ````<script type="text/javascript" src="js/dist/bundle.js"></script> ````
7. 浏览器控制台输出

        module1
        module2
        module3.foo()
        module3.bar()

---
### AMD
- 说明
    - Asynchronous Module Definition(异步模块定义)
    - 专门用于浏览器端, 模块的加载是异步的 
- 基本语法
    - 暴露模块
        - 定义没有依赖的模块
           ```` define(function(){return 模块})````
        - 定义有依赖的模块
           ```` define(['module1','module2'],function(m1,m2){return 模块})````
    - 引入模块
        - ````require(['module1', 'module2'], function(m1, m2){使用m1/m2})````
- 实现(浏览器)
    - html页面引入require.js文件

---
#### AMD 模块化
1. 下载````require.js```` 并在html页面引入
    - 官网: http://www.requirejs.cn/
2. 创建项目结构

	       |-js
	        |-libs //用来放第三方库的文件夹
	          |-require.js
	        |-modules //用来放模块文件的文件夹
	          |-alerter.js
	          |-dataService.js
	        |-main.js //模版主文件
	       |-index.html //页面
3. 编写模块
    - 定义没有依赖的模块 --> dataService.js
    
            define(function () {
              let name = 'kobe';
              function getName() {
                return name
              }
              //暴露模块
              return {getName}
            });
    - 定义有依赖的模块 --> alerter.js
    
            define(['dataService','jquery'],function (dataService,$) {
              let msg = 'atguigu.com';
              function showMsg() {
                console.log(msg + '-' + dataService.getName());
              }
              $('body').css('background','red');
              //暴露模块
              return {showMsg}
            });
4. 应用主入口 --> main.js
    - 配置模块 requirejs.config({})
    - 模块公共路径 baseUrl
    - 模块名与模块路径映射 paths:{}
    - 配置不支持AMD规范的第三方库 shim:{}
    
            requirejs.config({
              //公共路径
              baseUrl: "js/",
            
              //模块标识名与模块路径映射
              paths: {
                //第三方库
                'jquery':'./libs/jquery-1.10.1',
                'angular':'./libs/angular',
                'angular-ui-router':'./libs/angular-ui-router',
                //自定义模块   index.html的角度上查找路径
                "dataService": "modules/dataService",
                "alerter": "modules/alerter"
              },
            
              //配置不支持AMD规范的第三方库
              shim:{
                'angular':{
                  exports:'angular'
                },
                'angular-ui-router':{
                  exports:'angular-ui-router',
                  deps:['angular'] //传该文件需要依赖的文件
                }
              }
            });
    - 引入模块 require
    - 第一个参数:[] 传入模块名
    - 第二个参数:函数
        
            require(['alerter','angular'],function (alerter,angular) {
              console.log(angular);
              alerter.showMsg()
            });
5. 页面使用模块
	- data-mian指定主入口的js文件
	- src指定AMD依赖的require.js文件
	- ````<script data-main="js/main.js" src="js/libs/require.js"></script>````
6. 浏览器控制台输出
    
	    atguigu.com-kobe
	    浏览器页面为红色

---
### CMD
- 说明
    -  Common Module Definition(通用模块定义)
    -  专门用于浏览器端, 模块的加载是异步的 
    -  模块使用时才会加载执行
- 基本语法
    - 暴露模块
        - 定义没有依赖的模块
        
                    define(function(require, exports, module){
                        exports.xxx = value,
                        module.exports = value
                        
                    })
        - 定义有依赖的模块
        
                define(function(require, exports, module){
                	//引入依赖模块(同步)
                	var module2 = require('./module2')
                	//暴露模块
                	exports.xxx = value
                })
    - 引入模块
    
                define(function (require) { })
- 实现(浏览器)
    - html页面引入 ````Sea.js```` 文件
    - seajs.use() 指定模版主文件路径

---
#### CMD 模块化
1. 下载 ````sea.js````并在html页面引入
2. 构建项目
    
	       |-js
	        |-libs //用来放第三方的库
	          |-sea.js
	        |-modules //用来放模块文件
	          |-module1.js
	          |-module2.js
	          |-module3.js
	          |-main.js
	       |-index.html //页面
3. 定义模版代码
    - module1.js
    
            define(function (require,exports,module) {
              let name = 'wukong';
              function getName() {
              	  return name
              }
            
              module.exports = getName //暴露方法
            });
    - module2.js
    
            define(function (require,exports,module) {
              let module1 = require('./module1');
            
              let msg = 'atguigu.com';
              function showMsg() {
                console.log(msg + module1()); //调用module1
              }
            
              module.exports = {showMsg} //暴露对象
            });
    - module3.js
    
            define(function (require,exports,module) {
        	  exports.KEY = 'NBA GAMES';
            })  
4. main.js 主文件

        define(function (require) {
           //同步引入
    	  let module2 = require('./module2');
    	  module2.showMsg() //对象调用
    
          //异步引入
          require.async('./module3',function (module3) {
      	     console.log(module3.KEY);
          })
        });
5. html页面代码
	- 引入sea.js文件
    	- ````<script src="js/libs/sea.js"></script>````
    - 使用模块(指定主文件js)
         - ````seajs.use('./js/modules/main.js');````
6. 浏览器控制台输出
    
        atguigu.comwukong
        NBA GAMES

----------

- module.exports暴露方法
	- function getName() {}
	- module.exports = getName 
	- let module1 = require('./module1');
	- module1()
- module.exports暴露对象
	- function getName() {}
	- module.exports ={getName} 
	- let module1 = require('./module1');
	- module1.getName()
	
----------

## ES6 模块
- 说明
    - 依赖模块需要编译打包处理
- 语法
    - 暴露模块: export
    	- 实际暴露的就是一个对象
    - 默认暴露: export default xxx
	    - 暴露任意数据可接收任意数据
    - 引入模块: import xx from  xx
	    - 接收的变量是对象
	    - 也可以对应模块名字进行解构赋值
- 实现
    -  使用Babel将ES6编译为ES5代码
    -  使用Browserify编译打包js

---
#### ES6 模块化
1. 创建package.json

          {
            "name" : "es6-babel-browserify",
            "version" : "1.0.0"
          }
2. 安装babel-cli, babel-preset-es2015和browserify
    - npm install babel-cli browserify -g
    - npm install babel-preset-es2015 --save-dev 
    - npm install browserify --save-dev
3. 创建 .babelrc 文件
    
    	{
            "presets": ["es2015"]
         }
4. 编码
    - js/src/module1.js
    
            //分别暴露多个数据 暴露本质是一个对象
        
            export function foo() {
            	  console.log('我是foo()方法');
            }
            
            
            export function bar() {
              console.log('我是bar()方法');
            }
            
            export  let msg = 'atguigu.com';
    - js/src/module2.js
    
            //统一暴露
        
            let data = 'NBA';
            function fun1() {
            	  console.log('我是fun1方法' + '_' + data);
            }
            
            function fun2() {
            	  console.log('我是fun2方法'+ '_' +data);
            }
            
            export {fun1,fun2}
    - js/src/module3.js
    
            //默认暴露. 
			//默认接收暴露的任意数据类型. 通常是对象
        
            export  default {
              name: 'Tom',
              setName: function (name) {
                this.name = name
              }
            }
5. 主文件引入
	- 引入其他模块语法
	- import 变量 from 模块所在路径的模块文件
	

	        //引入第三方JS库
	        import $ from 'jquery'
	        
	        //引入其他模块 
	        
	        import {foo,bar} from './module1'  //解构赋值
	        import {msg} from './module1'
	        
	        import module2 from './module2'
	        
	        import  obj from './module3'
	        
	        foo();
	        bar();
	        console.log(msg);
	        
	        module2.fun1();
	        module2.fun2();
	        
	        obj.setName('kobe');
	        console.log(obj);
	        
	        $('body').css('background','pink');
6. 编译
    - 使用Babel将ES6编译为ES5代码
    - babel 要转换的js文件路径 -d 转换后的目标路径
    - ````babel js/src -d js/lib````
    - 使用Browserify编译js
    - ````browserify js/lib/main.js -o js/lib/bundle.js````
7. html代码引入
    - ````<script type="text/javascript" src="js/lib/bundle.js"></script>````
8. 浏览器控制台输出

        我是foo()方法
        我是bar()方法
        atguigu.com
        我是fun1方法_NBA
        我是fun2方法_NBA
        - 页面显示粉色