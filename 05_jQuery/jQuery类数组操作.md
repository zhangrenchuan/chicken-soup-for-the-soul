## jQuery类数组操作

类数组对象就是结构上类似于数组的对象，该对象具备数组的一些特性属性或方法，同时具有自己独特的一些属性或方法。

**数组与类数组对象的区别**

*   数组的类型是Array
*   类数组对象的类型是Object

**类数组的操作：**

*   length属性：获取指定元素的个数。
*   eq(index)：将下标等于index的DOM对象取出来。
*   get(index)：返回一个DOM对象组成的数组。
*   index（obj）：返回DOM或jQuery对象在类数组中的下标。
*   遍历方法：
    *   $(selector).each(callback)
        *   callback：回调函数，function(index,domEle){}
            *   index：遍历过程中的索引值
            *   domEle：遍历后得到的DOM对象

					$.each($("input"),function(index,domEle){
					    console.log(domEle.value);
					    console.log($(domEle).val());
					    console.log(this.value);
					    console.log($(this).val());
					});

- $.makeArray(obj) 将类数组对象转换为数组对象

- $.inArray(value, array)  查找元素在数组中的位置
确定第一个参数在数组中的位置，从0开始(如果没有找到则返回 -1 )

- $.toArray() 把jQuery集合中所有DOM元素恢复成一个数组。
