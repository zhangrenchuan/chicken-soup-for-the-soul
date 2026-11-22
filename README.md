# 前端开发学习笔记

这套笔记从 HTML、CSS 和 JavaScript 讲起，再介绍浏览器操作、网络请求、Node.js 和常见前端框架。每篇开头都有一段白话导读，可以先看它解决什么问题，再看术语和代码。

## 网页导航

[导航页入口](docs/index.html)包含章节索引、关键词搜索和文章翻页。下载仓库 ZIP 或克隆后，用浏览器打开 `docs/index.html`，即可离线阅读。维护笔记后，运行 `python3 scripts/build_navigation.py` 重新生成网页，需安装 Python 3 与自带 RDoc 的 Ruby。

[查看 v2.0.0 更新记录](CHANGELOG.md)。

## 从哪里开始

1. 想做出第一个网页，按第 1～3 章学习。先做出页面结构，再加样式，最后让按钮能响应点击。
2. 想让网页加载数据，先看第 3 章的 DOM 和 JSON，再看第 8 章的 AJAX。想自己写接口时，再学第 7 章的 Node.js 和 HTTP。
3. 想学组件开发，可以看 React 和 Vue 章节。AngularJS、Zepto、部分 React 和 Vue 示例来自旧版项目。运行前先核对版本。

## 章节目录

### 1. HTML：页面结构

- [HTML入门](01_HTML/HTML入门.md)

### 2. CSS：样式与布局

- [css基础](02_CSS/css基础.md)
- [浮动与父元素高度](02_CSS/浮动_高度塌陷.md)
- [定位](02_CSS/定位.md)
- [css2文本](02_CSS/css2文本.md)
- [css2字体](02_CSS/css2字体.md)
- [css2背景](02_CSS/css2背景.md)
- [css2垂直对齐](02_CSS/css2垂直对齐.md)

### 3. JavaScript 基础

- [ECMAScript 与 JavaScript](03_JS/Ecma.md)
- [JS基本语法](03_JS/JS基本语法.md)
- [JS数据类型](03_JS/JS数据类型.md)
- [JS运算符](03_JS/JS运算符.md)
- [JS语句](03_JS/JS语句.md)
- [JS对象](03_JS/JS对象.md)
- [JS函数](03_JS/JS函数.md)
- [JS数组](03_JS/JS数组.md)
- [JS内置对象方法](03_JS/JS内置对象方法.md)
- [正则表达式](03_JS/正则表达式.md)
- [DOM](03_JS/DOM.md)
- [BOM](03_JS/BOM.md)
- [JSON](03_JS/JSON.md)

### 4. HTML5 与 CSS3：图形、表单和动画

- [HTML5](04_HTML5/HTML5.md)
- [CSS3](04_HTML5/CSS3.md)
- [canvas](04_HTML5/canvas.md)
- [SVG](04_HTML5/SVG.md)
- [HTML5地理定位](04_HTML5/HTML5地理定位.md)

### 5. jQuery：操作旧项目中的页面

- [jQuery入门](05_jQuery/jQuery入门.md)
- [jQuery选择器](05_jQuery/jQuery选择器.md)
- [用 jQuery 修改页面](05_jQuery/jQuery_DOM操作.md)
- [jQuery事件](05_jQuery/jQuery事件.md)
- [$冲突问题](05_jQuery/$冲突问题.md)
- [jQuery动画](05_jQuery/jQuery动画.md)
- [jQuery类数组操作](05_jQuery/jQuery类数组操作.md)
- [jQuery插件](05_jQuery/jQuery插件.md)

### 6. JavaScript 进阶：作用域、闭包和原型

- [数据类型](06_JavaScript高级/数据类型.md)
- [原型](06_JavaScript高级/原型.md)
- [this](06_JavaScript高级/this.md)
- [提升](06_JavaScript高级/提升.md)
- [上下文环境对象](06_JavaScript高级/上下文环境对象.md)
- [作用域与作用域链](06_JavaScript高级/作用域.md)
- [闭包](06_JavaScript高级/闭包.md)
- [对象创建模式](06_JavaScript高级/对象创建模式.md)
- [原型链继承](06_JavaScript高级/原型链继承.md)
- [线程机制](06_JavaScript高级/线程机制.md)
- [JS引擎](06_JavaScript高级/JS引擎.md)
- [Web Workers API](06_JavaScript高级/Web Workers API.md)

### 7. Node.js：文件、HTTP 与服务端

- [Node基础](07_NodeJs/Node基础.md)
- [HTTP入门](07_NodeJs/HTTP入门.md)
- [HTTP服务器建立](07_NodeJs/HTTP服务器建立.md)
- [路由](07_NodeJs/路由.md)
- [Buffer 缓冲区](07_NodeJs/buffter缓冲区.md)
- [FS模块](07_NodeJs/FS模块.md)
- [Node模块系统](07_NodeJs/Node模块系统.md)
- [NPM](07_NodeJs/NPM.md)
- [路径](07_NodeJs/路径.md)
- [模块分类](07_NodeJs/模块分类.md)
- [数据库Mongoose](07_NodeJs/数据库Mongoose.md)
- [Express](07_NodeJs/Express.md)
- [cookie](07_NodeJs/cookie.md)
- [JSON&XML](07_NodeJs/JSON&XML.md)

### 8. AJAX：请求数据与更新页面

- [简介](08_AJAX/简介.md)
- [ajax请求](08_AJAX/ajax请求.md)
- [前后端交互](08_AJAX/前后端交互.md)
- [用 jQuery 发请求](08_AJAX/jQuery_AJAX.md)
- [小练习](08_AJAX/ajax基础练习--省市县三级联动.md)
- [跨域请求](08_AJAX/跨域请求.md)
- [前端模版引擎](08_AJAX/前端模版引擎.md)
- [上传下载文件](08_AJAX/上传下载文件.md)
- [ajax高级](08_AJAX/ajax高级.md)
- [版本控制工具](08_AJAX/版本控制工具.md)

### 9. AngularJS 1.x（旧版）

- [简介](09_Angular/简介.md)
- [四个重要概念](09_Angular/四个重要概念.md)
- [四个重要对象](09_Angular/四个重要对象.md)
- [三个页面语法](09_Angular/三个页面语法.md)
- [三个对象详解](09_Angular/三个对象详解.md)
- [两个重要扩展模块](09_Angular/两个重要扩展模块.md)
- [ajax封装](09_Angular/ajax封装.md)

### 10. ECMAScript、模块化与构建

- [简介](10_ECMAScript/简介.md)
- [ES5](10_ECMAScript/ES5.md)
- [ES6](10_ECMAScript/ES6.md)
- [ES7](10_ECMAScript/ES7.md)
- [JS模块化](10_ECMAScript/JS模块化.md)
- [自动化工具](10_ECMAScript/自动化工具.md)

### 11. React：组件、状态与路由

- [入门](11_ReactJs/入门.md)
- [props：接收父组件的数据](11_ReactJs/组件属性のprops.md)
- [ref：访问页面元素](11_ReactJs/组件属性のrefs.md)
- [state：保存组件状态](11_ReactJs/组件属性のstate.md)
- [生命周期](11_ReactJs/生命周期.md)
- [脚手架](11_ReactJs/脚手架.md)
- [在 React 中获取数据](11_ReactJs/react_ajax.md)
- [服务器渲染](11_ReactJs/服务器渲染.md)
- [React 界面组件库](11_ReactJs/react_ui.md)
- [组件通信](11_ReactJs/组件通信.md)
- [React Router 路由](11_ReactJs/react_router.md)

### 12. JavaScript 与 CSS 进阶练习

- [JS高级2.0](12_JS2.0_CSS2.0/JS高级2.0.md)
- [正则表达式2.0](12_JS2.0_CSS2.0/正则表达式2.0.md)
- [BOM2.0](12_JS2.0_CSS2.0/BOM2.0.md)
- [DOM2.0](12_JS2.0_CSS2.0/DOM2.0.md)
- [CSS高级](12_JS2.0_CSS2.0/CSS高级.md)

### 13. 移动网页：像素、视口和适配

- [像素概念](13_移动端/像素概念.md)
- [视口概念](13_移动端/视口概念.md)
- [缩放行为](13_移动端/缩放行为.md)
- [META标签](13_移动端/META标签.md)
- [适配方案](13_移动端/适配方案.md)
- [画一条物理像素宽的线](13_移动端/1物理像素的实现.md)
- [移动端事件&问题综合](13_移动端/移动端事件&问题综合.md)
- [移动端价值链&浏览器](13_移动端/移动端价值链&浏览器.md)
- [zepto框架](13_移动端/zepto框架.md)

### 14. Vue：基础用法与原理（含旧版示例）

- [概述](14_Vue/概述.md)
- [使用Vue](14_Vue/使用Vue.md)
- [生命周期](14_Vue/生命周期.md)
- [重要属性](14_Vue/重要属性.md)
- [插件](14_Vue/插件.md)
- [Vue重要知识支持](14_Vue/Vue重要知识支持.md)
- [Vue 响应式原理示例](14_Vue/Vue_源码分析.md)

### 15. 附录：Vue 2 与 Vuex

- [Vue2.0](15/Vue2.0.md)
- [Vuex](15/Vuex.md)

## 原作者与许可

原作者为 zhangrenchuan。[查看 GitHub 原仓库](https://github.com/zhangrenchuan/chicken-soup-for-the-soul)。

本仓库附有 [原仓库许可文件](LICENSE.txt)。[原 README 的许可说明](https://github.com/zhangrenchuan/chicken-soup-for-the-soul/blob/e9783afdddbd3b86a9eb0cdf515a3194b4285b45/README.md) 可供查阅。
