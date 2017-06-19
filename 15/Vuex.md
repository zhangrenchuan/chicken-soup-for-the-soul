## Vuex
- Github: [https://github.com/vuejs/vuex](https://github.com/vuejs/vuex)
- 文档: vuex.vuejs.org
- 安装: npm install vuex --save

### vuex 概念
- Vuex是一个专为Vue.js应用程序开发的状态管理模式
- 它采用集中式存储管理应用的所有组件的状态，并以相应的规则保证状态以一种可预测的方式发生变化

### 状态自管理应用
- state，驱动应用的数据源, 相当于data；
- view，以声明方式将state映射到视图；
- actions，响应在view上的用户输入导致的状态变化。

![](http://i.imgur.com/LBYfMzX.png)

> 问题: 当我们的应用遇到多个组件共享状态时，单向数据流的简洁性很容易被破坏
> 
> 1. 多个视图依赖于同一状态。
> 2. 来自不同视图的行为需要变更同一状态。
> 3. 以前的解决办法: 
	- 将数据以及操作数据的行为定义在父组件
	- 将数据以及操作数据的行为传递给需要的各个子组件(可能多层传递)

----------

#### Vuex核心 -- State
- 单一状态树(唯一数据源). 用一个对象就包含了全部的应用层级状态. 
- 每个应用将仅仅包含一个 store 实例
- 单一状态树让我们能够直接地定位任一特定的状态片段，在调试的过程中也能轻易地取得整个当前应用状态的快照
- Vuex 通过 store 选项，提供了一种机制将状态从根组件『注入』到每一个子组件中（需调用 Vue.use(Vuex)）
- 通过在根实例中注册 store 选项，该 store 实例会注入到根组件下的所有子组件中，且子组件能通过 this.$store 访问到

		const state = {
			xxx: initValue
		}

#### Vuex核心 -- Mutations
- 包含多个更新state的方法(回调函数)的对象. 
- 由action中的commit方法来触发

		const mutations = {
			yyy (state) {
			// 更新state某个属性	
		  }
		}

#### Vuex核心 -- Actions
- Action 提交的是 mutation，而不是直接变更状态. 
- 通过执行commit()来触发mutation的调用.间接更新state
- 由组件中的 $store.dispatch('action名称')触发
- 可包含多个任意异步操作
	- 定时器
	- ajax

			const actions = {
				zzz ({commit, state}, data) {
				 commit('yyy') //事件名
			  }
			}

#### Vuex核心 -- Getters
- 包含多个计算属性 (get) 对象
- Getters 会暴露为 store.getters 对象
- 由 $store.getters.xxx 来读取
- store 中定义『getters』（可以认为是 store 的计算属性）。Getters 接受 state 作为其第一个参数

		const getters = {
			mmm (state) {
			 return
		  }
		}

#### Vuex核心 -- Modules
Vuex 允许将 store 分割成模块, 每个模块拥有自己的 state、mutation、action、getter、甚至是嵌套子模块——从上至下进行同样方式的分割

##### 向外暴露store对象

	export default new Vuex.store({
		state,
		mutations,
		actions,
		getters
	})

##### 组件中映射

	import {mapGetters, mapActions} from 'vuex'
	export default ({
		computer: mapGetters(['mmm'])
		methods: mapActions(['zzz'])
	})

	{{mmm}} @click="zzz(data)"

##### 映射store

	import store from './store'
	new Vue({
		store
	})

#### 将vuex引到项目中
* 下载: npm install vuex --save
* 使用vuex:

		store.js
			import Vuex from 'vuex'
			export default new Vuex.Store({
				state,
				mutations,
				actions,
				getters,
				modules
			})
		main.js
			import store from './store.js'
			new Vue({
				store
			})

![](http://i.imgur.com/oL4GZt7.png)