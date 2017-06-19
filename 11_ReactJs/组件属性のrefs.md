## 组件的3大属性之二: refs属性
1. 组件内的标签都可以定义ref属性来标识自己
2. 在组件中可以通过this.refs.ref属性名得到对应的真实DOM对象
3. 作用: 用于操作指定的ref属性的dom元素对象(表单标签居多)
    - ````<input ref='username'>````
    - ````this.refs.username````
    

##### 事件处理
- 通过onXxx属性指定组件的事件处理函数(注意大小写)
- React使用的是自定义(合成)事件, 而不是使用的DOM事件
- React中的事件是通过委托方式处理的(委托给组件最外层的元素)
- 必须通过this把事件绑定给组件的实例对象(不需要调用)
- 通过event.target得到发生事件的DOM元素对象

##### this的注意事项
- 组件内置的方法中的this为组件对象
- **自定义的function(方法)都指向null**
    - 使用类的继承控制器对象修改this
	
			constructor(props){
			   super(props)
			   this.xxx = this.xxx.bind(this)
		    }

---

###### 自定义组件实现弹框提示

    //创建组件
    class App extends React.Component{
      constructor(props){
        super(props);

        //修改this(this指向肯定是组件类的实例对象)
        this.handleClick = this.handleClick.bind(this)
      }


      //定义点击事件的方法
      handleClick(){
        let value = this.refs.msg.value;
        alert(value)
      }
      //定义失去焦点的方法
      handleBlur(event){
        let value = event.target.value;
        alert(value)
      }
      render(){
        return (
            <div>
              <input type="text" ref="msg"/>
              <button onClick={this.handleClick}>提示输入数据</button>
              <input onBlur={this.handleBlur} type="text" placeholder="失去焦点显示数据"/>
            </div>
        )
      }
    }
    
    //渲染
    ReactDOM.render(
        <App/>,
        document.getElementById('example')
    )