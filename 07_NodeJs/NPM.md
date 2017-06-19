## NPM
NPM 是 node 的包管理分发工具，现在已经是 JavaScript 各种包的分发管理平台。

查找npm的网站:[https://www.npmjs.com/](https://www.npmjs.com/ "npm网站")

包含: 模块(一个js文件) 包(一个
文件夹包括json文件和js文件)

1. 在NodeJs 语言中. 包和模块没有本质的不同
2. 包将某个独立的功能封装起来. 用于发布 更新  依赖管理和进行版本控制
3. NodeJs根据CommonJs规范实现包机制.

#### NPM本地安装(JS代码中使用)
1. 在当前工作目录下启动命令行进行安装
2. 命令行输入 npm install PACKAGE_NAME
例子: npm install moment   官网： http://momentjs.cn/ (node时间管理包)
3. 卸载: npm uninstall PACKAGE_NAME

#### NPM全局安装(命令行中使用)
1. 新建文件夹: D:\Study\NodeJs\node_global (建议在NodeJs文件夹下创建)
2. 命令行输入 npm config set prefix "D:\Study\NodeJs\node_globall"
3. 再输入 npm config set registry https://registry.npm.taobao.org
4. 输入要下载的npm包. npm install -g PACKAGE_NAME
5. 卸载:npm uninstall -g PACKAGE_NAME

#### 包的说明文件(package.json)
1. 相当于本地项目的一个文档说明
2. 允许你指定你项目中所使用的node包版本
3. 构建项目更加容易.便于和他人分享
4. npm init 创建一个package文档

#### package.json 属性详解
- name 包名
- version 版本号
- scripts (test)配置npm运行命令
- npm run xxx  npm启动服务
- start test可以省略run
- dependencies 运行依赖的包
	- --save
- devDependencies 开发依赖的包
	- --save-dev
- 向上的尖括号可以管理二级，三级版本
	- 第一个数字一级版本
	- "jquery": "^3.2.1" 
- 波浪线可以管理三级版本。
	- "jquery": "~3.2.1"


			{
		     "name": "npm_command", //包名
		     "version": "1.0.0", //版本
		     "scripts": { //配置npm运行命令
		     "start": "node bin/www"
			 },
			"dependencies": {//运行依赖的包
			     "jquery": "^3.2.1"
			  },
			"devDependencies": {//开发依赖的包
			     "babel": "^6.23.0"
			  }
			 }



#### npm命令详解
- 使用npm命令来下载依赖模块及对项目包(模块)进行管理
- 常用命令：
 - npm init (生成package.json)
 - npm install (安装package.json中的依赖包)
 - npm install packageName -g(全局安装)
 - npm install packageName --save 安装包(局部安装运行依赖)
 - npm install packageName@version --save (安装指定版本的包(局部安装))
 - npm install packageName --save-dev(局部安装--开发依赖)
 - npm info packageName (显示包的信息)
 - npm rm packageName (移除包)
 - npm config get prefix (获取全局安装包的所在地址,并且可见对应的cmd命令)
- 使用npm导致的问题
	- 下载慢
	- 甚至下载不了

#### cnpm(淘宝镜像)
- 将npm上的包同步更新到淘宝镜像上，目前是每10分钟同步一次。
- 配置：npm install -g cnpm --registry=https://registry.npm.taobao.org
- 常用命令：使用 cnpm 代替 npm 即可
- 问题：
 - 会多下载一些文件/文件夹
 - 严重者会导致 webstorm 瘫痪，就像帕金森综合征
- 解决上述问题的办法
 - 修改 npm 的下载指向地址
 - npm config set registry "https://registry.npm.taobao.org"

#### yarn Facebook开发的包管理工具
- yarn是Facebook开源的新的包管理器，可以用来代替npm
- 配置 npm install yarn -g
- 特点：有缓存，没有自己的仓库地址
- 常用命令
 - yarn --version 查看版本号
 - yarn  相当于npm install
 - yarn init  生成一个包
 - yarn global package (全局安装)
 - yarn add package (局部安装)
 - yarn add package --dev  开发依赖
 - yarn remove package  移除包
 - yarn list  查看包
- 地址：https://yarnpkg.com/zh-Hans/

#### cyarn
- 配置：npm install cyarn -g --registry "https://registry.npm.taobao.org"
- 常用命令：将 yarn 使用cyarn代替即可