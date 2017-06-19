## JS数据类型
- String 字符串
- Number 数值
- Boolean 布尔值
- Null 空值
- Undefined 未定义
- Object 对象

**String、Number、Boolean、Null、undefined属于基本数据类型**

**Object属于引用数据类型**     

#### typeof 
- 通过 typeof 可以检查一个变量类型
- 返回值是一个字符串. 用来描述数据类型
- 使用typeof检查一个字符串时，会返回string
- 使用typeof检查一个数值时，会返回number
- 使用typeof检查一个布尔值时，会返回boolean
- **使用typef检查一个Null（空值）时，会返回Object**
- 使用typeof检查一个未定义值时，会返回Undefined
- **加引号是字符串. 不加引号是变量**

----------

### String 字符串
- 在JS中字符串需要使用引号引起来. 单引号双引号都可以
- 引号不可以被嵌套
- 当需要打印一些特殊字符时, 可以使用 \ 来作为转义字符

	     \" --> 表示“ ”
	     \‘ --> 表示‘ ’
	     \\ --> 表示 \
	     \t --> 表示制表符 （tab键）
	     \n --> 表示换行
	     \uxxxx --> 表示一个unicode编码. xxxx代表编码数值

### Number 数值
- 在JS中所有的数字都是Number类型
- 包括整数和浮点数
- 在JS中尽量不要做对精确度要求很高的计算. 计算浮点数会出现不可预期的结果

		- Number.MAX_VALUE来获取最大值
	      1.7976931348623157e+308
	
	    - Number.MIN_VALUE 0以上的最小值：
	      5e-324
   
- infinity 数据类型也是Number
- NaN (Not a Number) 表示非法数字. 数据类型也是Number
- 进制数字
	- 十六进制 0x数字
		- var c=0x10;//十六进制10
	- 八进制 0数字
		- c=010;//八进制10
	- 二进制 0b数字
		- c=0b10;//二进制10
	
### Boolean 布尔值
- 使用布尔值进行逻辑判断
- 布尔值只有两个 true和false
- true 表示逻辑为真
- false 表示逻辑为假


### Null 和 Undefined
- Null 空值
	- Null类型只有一个值 Null
	- 专门用来表示为空的对象
	- typeof返回为Object数据类型
- undefined 未定义
	- 表示一个声明但没有赋值的变量
	- 数据类型是undefined


## JS数据类型转换
#### 强制类型转换为String
- 调用 toString() 方法
	- null和undefined不能使用
- 调用 String() 函数
	- null转换成 "null"
	- undefined转换成 "undefined"
- **任意值 = 任意值 + ""**

#### 强制类型转换为Number
- 使用 Number() 函数
	- 如果字符串是合法的数字则转换成对应数字
	- 如果字符串不是合法数字则转换成NaN
	- 如果字符串是空串或者是空格则转换为0
	- true 转换为 1 
	- false 转换为 0
	- null 转换为 0 
	- undefined 转换为 NaN
- 使用 parseInt（）或 parseFloat（）
	- parseInt（） 将字符串转换成整数
	- parseFloat（） 将字符串转换为小数
	- 如果在这两个函数中传递一个非字符串作为参数会变成NaN
- **任意值 = +任意值** 
	- 进行任何计算也可转换
	- 任意类型 * 1 
	- 任意类型 - 0
	- 任意类型 / 1

#### 强制类型转换为Boolean
- 使用 Boolean() 函数
	- 对于字符串除了空串是false 其余都是true
	- 对于数字除了0和NaN是false 其余都是true
	- 对于Null 转换成false
	- 对于undefined 转换成false
	- 任何对象默认都是true
- **任意值 = !!任意值**