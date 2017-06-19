## Vue2.0
- Vue升级工具: [https://github.com/vuejs/vue-migration-helper](https://github.com/vuejs/vue-migration-helper)
- vue从1.x升级到2.x, 几乎 90% 的 API 和核心概念都没有变

### Vue2.0 API变化
- vue-router变化
	- v-link ->  <router-link>
	- keep-alive ===> <keep-alive>
- v-for 指令
	- 移除$index
	- v-for="(item, index) in items"
- v-el与v-ref指令
	- ref指令 ref='xxx'
	- this.refs.xxx
- 组件的模板
	- 只允许有一个根标签
- 组件间通信
	- $dispatch()/$broadcast()被移除, 只留下$emit
	- events选项被移除, 通过v-on指令绑定监听
	- 不能直接在子组件中修改父组件传入的prop
- 过渡
	- <transition>
	- transitions选项被移除
	- 过滤css
	
		     .fade-enter: 进入的开始状态(不可见), 在此指定进入显示前不可见的样式
		       .fade-leave-active: 离开的结束状态(不可见), 在此指定离开后不可见的样式
		       .fade-enter-active: 进入的结束状态(可见), 在此指定显示的transition
		       .fade-leave-active: 离开的结束状态(不可见),在此指定隐藏的transition
	- JS动画
	
		     <transition name="drop"
		            @before-enter="beforeDrop"
		            @enter="dropping"
		            @after-enter="afterDrop"
		            v-bind:css="false">
- 虚拟DOM/组件的生命周期
	- 生命周期回调函数有增减
	- 移除: ready()
	- 增加: mounted() / beforeUpdate() / afterUpdate()