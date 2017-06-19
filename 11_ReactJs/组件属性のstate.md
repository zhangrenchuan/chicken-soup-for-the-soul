##   组件3大属性之: state属性
- 组件被称为"状态机",通过更新组件的状态值来更新对应的页面显示(重新渲染)
- **this.state 初始化状态**

      constructor (props) {
        super(props);
        this.state = {
          stateProp1 : value1,
          stateProp2 : value2
        };
      }
- **读取某个状态值**
    - ````this.state.statePropertyName````
- **this.setState({}) 更新状态**

          this.setState({
            stateProp1 : value1,
            stateProp2 : value2
          })
         
        
---
###### 实时切换更新界面

    class App extends React.Component{
      constructor(props){
        super(props);
        
      this.state = {
        isGun:true //初始化状态
      };
      //修改this
      this.handleClick = this.handleClick.bind(this)
    }
    
    //定义点击方法
    handleClick()
      this.setState({
        isGun:!this.state.isGun //修改状态
      })
    };
    render(){
      let msg = this.state.isGun?'你给我滚':'我给你滚';
      return (
        <p onClick={this.handleClick}>
            {msg}
         </p>
      )
     }
    }
  
    //渲染组件
    ReactDOM.render(
      <App/>,
      document.getElementById('example')
    )
    

---


#### 扩展 -- 对象的关系
- 依赖 (完成某个功能需要依赖的对象)
	- 对象关系之间最弱的一种，通常表示一个对象里的某一个功能需要另外一个对象（依赖对象）才能实现
- 关联 (一个对象长期持有另一个对象的引用)
	- 关系比依赖稍微密切一点，但不是强制性的，这种关系随时可以拆开，一个对象里长期持有另一个对象的引用就是关联关系
- 聚合 
	- 关系比关联更加深刻， 它暗含着一种所属关系以及生命期关系。
- 组合 (整体与部分的关系)
	- 对象关系中最为亲密的，有着直接的声明周期关联性，就是整体与部分的关系
- trim() 去除字符串空格
- 事件委托的好处: 新添加的元素也可以享受到父元素绑定的事件


----------
#### 受控组件

    class TowWay extends React.Component{
      constructor(props){
        super(props);
      //初始化state状态
      this.state = {
        msg:'atguigu.com'
      };
      this.changeMsg = this.changeMsg.bind(this)
    }

    changeMsg(e){
      let msg = e.target.value;
      //修改state的状态
      this.setState({msg})
    }

    render(){
      let msg = this.state.msg;
      return (
          <div>
            <input onChange={this.changeMsg} value={msg} type="text"/>
            <p>{msg}</p>
          </div>
        )
      }
    }
  
    ReactDOM.render(
       <TowWay/>,
       document.getElementById('example')
    )
- React是一个单向数据流
- 但可以自定义双向数据流组件(受控组件)
- 效果: 初始化数据并且在输入数据时实时同步变化