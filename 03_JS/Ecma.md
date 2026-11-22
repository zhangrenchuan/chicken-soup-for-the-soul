# ECMAScript 与 JavaScript

## 先弄懂这件事

ECMAScript 规定 JavaScript 语言的语法和行为。操作网页的 DOM 是浏览器提供的接口，学习时可以把语言和运行环境分开理解。

### 语言规范和运行环境

ECMAScript 是语言规范。我们写的 JavaScript 遵循这套规则。浏览器和 Node.js 还能提供不同的功能，例如浏览器提供 DOM，Node.js 提供文件读写接口。

ES5、ES2015（ES6）和 ES2016（ES7）是不同版本的规范。

### 把代码放在哪里

网页可以用 `<script>` 写代码，也可以用 `<script src="main.js"></script>` 加载外部文件。把代码放在独立文件中，页面结构和交互代码更容易各自维护。

- `//` 写单行注释，`/* ... */` 写多行注释。
- 用 `console.log()` 在控制台查看值。
- 用同一个标签调用 `console.time()` 和 `console.timeEnd()`，可以测量一段代码经过了多久。
