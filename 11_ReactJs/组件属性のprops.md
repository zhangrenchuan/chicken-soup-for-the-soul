## 组件三大属性 -- props
1. 每个组件实例对象都会有props属性(properties的简写)
2. 组件标签的所有 标签属性 都保存在props中
3. 作用: 通过标签属性从**组件外部向组件内部传递只读数据**(不可修改props属性)

##### props操作内部读取某个属性值:     
- **this.props.属性名**

	      class Person extends React.Component{
	        render(){
	          return (
	              <ul>
	                <li>姓名: {this.props.name}</li>
	                <li>年龄: {this.props.age}</li>
	                <li>性别: {this.props.sex}</li>
	              </ul>
	          )
	        }
	      }
     
##### 定义组件的默认props属性
- **组件实例.defaultProps = {}**
    
          Person.defaultProps = {
            age: 18,
            sex: '男'
          };   

##### 规定组件props属性的数据类型和必要性
- **组件实例.propTypes = {}**
- isRequired表示该项必填
    
	      Person.propTypes = {
	        name: React.PropTypes.string.isRequired,
	        age: React.PropTypes.number.isRequired
	      }

##### 扩展属性:定义对象的所有属性通过props传递
- 利用三点运算符把定义的对象全部属性传入虚拟dom标签里
- <组件实例对象 {...定义对象}/>
- <Person {...person}/>

	      let person1 = {name:'dirk',age:41,sex:'男'};
	          
	      ReactDOM.render(
	        <Person  {...person1}/>,
	        document.getElementById('example2')
	      )
      
##### 组件类的构造函数

    constructor (props) {
      super(props);
      console.log(props); // 查看所有属性
    }

---
###### 拆分组件

      //定义Welcom组件
      function Welcome(props) {
      	  return <h2>Welcome {props.name}</h2>
      }
    
      //定义app组件 外层
      class App extends React.Component{
        render(){
          return (
            <div>
             {
                this.props.names.map((item,index)=>{
                return <Welcome key={index} name={item}/>
             })
                }
            </div>
          )
        }
      }
    
      let names = ['tom','jason','bob'];
      //渲染组件
      ReactDOM.render(
          <App names= {names}/>,
          document.getElementById('example')
      )