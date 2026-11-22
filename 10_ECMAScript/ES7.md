# ES7

## 先弄懂这件事

`2 ** 3` 表示 2 的三次方。`[1, 2, 3].includes(2)` 用来检查数组里有没有 2。

## 笔记与示例

## ECMAScript 7
#### 指数运算符 (幂运算符)  
- 语法: **
- ````console.log(3 ** 3); //27````

#### Array.prototype.includes(value)
- 判断数组中是否包含指定的value值
- 带有prototype是给实例对象用的 ````var xxx = new Xxx()````

		  let arr = [1,2,3,'abc']
		  console.log(arr.includes(2));//true
		  console.log(arr.includes(5));//false
