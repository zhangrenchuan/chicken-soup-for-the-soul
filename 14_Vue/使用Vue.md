## 使用VUE
- 引入 vue.js 
- 创建vue实例对象 `new Vue({})`
- 页面模版使用vue指令
    - 使用v-model实现双向数据绑定
    - 显示数据
	    - 使用 `{{}}`  相当于innerText
    	- 使用 `{{{}}}` 相当于innerHTML

### Vue实例
- 每个 Vue.js 应用的起步都是通过构造函数 Vue 创建一个 Vue 的根实例
- 一个 Vue 实例其实正是一个 MVVM 模式中所描述的 ViewModel

		var vm = new Vue({
		  // 选项
		})

#### Vue对象配置选项
- el: 指定dom标签容器的选择器
    - 指定后管理其对应标签及其子标签
- data: 指定初始化状态属性数据的对象
    - vm代理了data中所有的属性的操作 (读写)
    - 可以指定对象或函数 (返回一个对象)
    - Vue.js 会递归地将它全部属性转为 getter/setter来响应数据变化
- methods: 包含多个实例方法的对象. 供页面中的事件指令来绑定回调
	- this自动绑定到实例对象
    - 回调函数默认有event参数, 但也可以指定自己的参数
    - 所有的方法由vue对象来调用, 访问data中的属性直接使用
- computed: 实例计算属性. 对状态属性进行计算返回一个新的数据, 供页面获取显示
	- getter 和 setter 的 this 自动地绑定到实例
    - 一般情况下相当于是一个只读属性
    - 利用set/get方法来实现属性数据的计算读取. 同时监视属性数据的变化
	- xxx : {
		get(){},
		set(value){}
	  }
- watch: 包含多个属性监视的对象. 
	- Vue.$watch(propertyName,function(val){})
		- propertyName 要监视的属性名
		- 回调中形参是最新更新的数据
    - 分为一般监视和深度监视
    	- handler:function(val,oldVal){}
    	- deep:true

----------

### Vue页面指令
- v-text/v-html: 指定标签体
    - v-text: 当作纯文本; 相当于{{}}
    - v-html: 将value作为html标签来解析; 相当于{{{}}}
    - 可以防止显示时闪屏
- v-el: 为某个元素注册一个唯一标识, vue对象通过$els属性访问这个元素对象
	- v-el:xxx
	- 读取得到标签对象: this.$els.xxx
	- HTML `<span v-el:msg>baidu</span>`
	- vm `this.$els.msg;`
- v-ref: 标识组件
- v-model: 在表单控件上创建双向绑定
	- 只限于 `input` / `select` / `textarea`
	- 表单项新特性指令
		- lazy  表单失去焦点时同步
		- number 将输入内容转换成number类型
		- debounce 设置一个最小的延时.在输入后延时同步
- v-if / v-else / v-show
    - v-if: 如果vlaue为true, 当前标签会输出在页面中
	- v-else: 与v-if一起使用, 如果value为false, 将当前标签输出到页面中
	- v-show: 根据表达式值的真假切换元素的 `display` CSS属性
	- template模版标签 不会出现在页面上
	- 如果需要频繁切换 v-show 较好，如果在运行时条件不大可能改变 v-if 较好
- v-for: 遍历
    - 遍历数组: `v-for="person in persons"` 
    - $index 当前数组元素的索引
    - 扩展数组方法: 对数组的常用方法进行了包装(用于数据绑定)
		- $remove(item) : 删除数组中对应的元素 (存在过滤索引会出错)
		- $set(index, ele) : 给数组中指定下标指定对应的元素 
	- 遍历对象: `v-for="value in person"`  
	- $key 当前对象的属性名
- v-on: 绑定事件监听
    - 格式: `v-on:事件名`
    - 简写: `@事件名`
    - 可指定参数也可不指定参数
    - 按键修饰符
	    - @keyup.keyCode   
	    - @keyup.enter
    - 事件修饰符
	    - @click.stop   阻止事件冒泡行为
	    - @click.prevent 阻止事件默认行为
    - 隐含对象: $event
- v-bind: 强制数据绑定
	- `<img v-bind:src="imgSrc" alt="">`
    - 简写: 可直接省略v-bind只写冒号 `<img :src="imgSrc" alt="">`
    - 强制绑定不写冒号传的是字符串. 写了冒号传的是变量 (动态的)
- v-cloak: 使用它防止闪现表达式, 与css配合
	- CSS: `[v-cloak] {display: none}`
	- HTML: `<p v-cloak>{{msg}}</p>`
	

####  自定义Vue指令
- 注册全局指令 `Vue.directive`
- 第一个参数: 自定义指令名 (去掉前缀 v-)
- 第二个参数: 指令的回调 形参value

	      Vue.directive('my-directive', function(value){
	        this.el.innerHTML = value.toUpperCase();
	      })
- 注册局部指令; 在对象配置选项中
- 属性名: 自定义指令名 (去掉前缀 v- 并加引号)
- 属性值: 函数 形参value
      
	      directives : {
	        'my-directive' : function(value) {
	          this.el.innerHTML = value.toLowerCase();
	        }
	      }
- 使用指令: `v-upper-zrc='xxx'`
- 在标签中使用:  `<p v-upper-zrc="msg"></p>`
	- 必须 `v-` 开头
	- 全部都为小写. 可以用 `-`作为分割
- 获取指令所在dom对象: this.el

----------

### Vue内置过滤器
- capitalize : 首字母大写
- uppercase : 全部大写
- lowercase : 全部小写
- currency : 货币化 (空格之后添加货币符号)
- pluralize : 单数/复数处理
- json : json格式化
- limitBy : 限定数组的部分元素(下标)
	- 第一个参数: 从下标第N个起
	- 第二个参数: 偏移数值
	- limitBy 2 1 从下标第二个起偏移1个
- filterBy : 限定数组的部分元素(值)
	- 第一个参数可以是字符串或函数
	- in分割
	- 第二个参数为根据某属性筛选
	- 格式: 'a' in 'name' name属性中有a的
- orderBy : 对数组进行排序 (默认升序)
	- 可指定具体属性来排序
	- -1为降序

#### 自定义Vue过滤器
- 全局过滤器 `Vue.filter`
- 第一个参数: 自定义过滤器名 
- 第二个参数: 过滤器回调. 可传参数;回调内必须return出结果

		<!--过滤器reverse: 对指定值进行倒序显示-->
		<p>{{msg | reverse}}</p>

	    Vue.filter('reverse', function(value) {
	      //处理逻辑
	      return  value.split('').reverse().join('');
	    })

- 局部过滤器; 在对象配置选项中
- 属性名: 过滤器名
- 属性值: 函数 

	  <!--过滤器wrap: 在指定值的左侧和右侧添加指定的文本-->
	  <p>{{msg | wrap '左边的文本' '右边的文本'}}</p>

	    new Vue({
	      filters : {
	        'wrap' : function(value, left, right) {
	            //处理逻辑
	            return left + ' ' + value + ' ' + right;
	        }
	      }
	    })