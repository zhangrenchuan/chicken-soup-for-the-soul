## React-Router
##### 后端路由
- path（路由分发）针对不同的路由对应不同的回调函数处理(req, res, next)
	- req;获取请求参数
	- res：返回请求数据
	- next: 调用后续的回调函数
##### 前端路由
- 路由是根据不同的url去请求不同的页面内容
- 前端路由就是把不同路由对应不同的内容或页面的任务交给前端来做，之前是通过服务端根据url不同返回不同的页面来实现。
- 利用H5的history.pushState和history.replaceState，这两个history新增的api，为前端操控浏览器历史栈提供了可能性
- 这两个Api都会操作浏览器的历史栈，而不会引起页面的刷新。
- 不同的是，pushState会增加一条新的历史记录，而replaceState则会替换当前的历史记录。

##### 应用：单页面应用
##### 优点和缺点：
- 优点： 用户体验好，不需要每次向服务器发送请求请求页面数据，响应快
- 缺点：使用浏览器的前进，后退键的时候会重新发送请求，没有合理地利用缓存

### HASH值
- 将任意长度的二进制字符串通过一定的算法映射成一个固定长度的较小二进制字符串，这个字符串就是对应的hash值，主要特点就是唯一的，不可逆的。
- hash通常应用在spa单页面应用中。因为通过不同的hash值映射的url可以使浏览器添加一条不同的url历史记录
- window.location.hash 读取#值
    - 读取时，可以用来判断网页状态是否改变
    - 写入时，则会在不重载网页的前提下，创造一条访问历史记录
- window.onhashchange = fun 监听hash值的改变

### URL的#号
- #代表网页中的一个位置。其右面的字符，就是该位置的标识符
- #是用来指导浏览器动作的，对服务器端完全无用。所以，HTTP请求中不包括#
- 单单改变#后的部分，浏览器只会滚动到相应位置，不会重新加载网页
- 这对于ajax应用程序特别有用，可以用不同的#值，表示不同的访问状态，然后向用户给出可以访问某个状态的链接。
- window.location.hash读取#值

---

### React-router
- react-router库中的相关组件
    - Router: 路由器组件, 用来包含各个路由组件
    - Route: 路由组件, 注册路由 
    - IndexRoute: 默认路由组件
    - hashHistory:路由的切换由URL的hash变化决定，即URL的#部分发生变化
    - Link: 路由链接组件
- Router: 路由器组件
    - 属性: history={hashHistory}用来监听浏览器地址栏的变化
    - hashHistory是react-router提供的对象.保存所有hash的url
    - 并将URL解析成一个地址对象，供React Router匹配
    - 子组件: Route
- Route: 路由组件
    - 属性1: path="/xxx"   映射请求的路由路径
    - 属性2: component={Xxx} 请求的组件对象
    - 根路由组件: path="/". 通常对应的是主组件
    - 子路由组件: 子<Route>配置的组件
- IndexRoute: 默认路由
    - 当父路由被请求时, 默认就会请求此路由组件
- hashHistory
    - 用于Router组件的history属性
    - 作用: 为地址url生成?_k=hash,用于内部保存对应的state
- Link: 路由链接
    - a标签用Link标签代替. 从react里拿到{Link}
    - 属性1: to="/xxx"  要请求的路由路径
    - 属性2: activeClassName="active" 活动时触发的class名
    

##### 基于脚手架创建项目
- `create-react-app hello-react`
- `npm install react-router@3 --save`

1. **定义各个路由组件**
   - About.js

            import React from 'react'
              function About() {
                return <div>About组件内容</div>
            }
            export default About

    - Home.js
    
	          import React from 'react'
	          function Home() {
	            return <div>Home组件内容2</div>
	          }
	          export default Home
    
    - Repos.js
    
	          import React, {Component} from 'react'
	          export default class Repos extends Component {
	            render() {
	              return (
	                <div>Repos组件</div>
	              )
	            }
	          }

2. **定义应用主组件** --> App.js
    
        import React from 'react';
        import {Link} from 'react-router'
        
        class App extends React.Component{
            render(){
                return (
                  <div>
                    <h1>Hello. React Router!</h1>
        
                    <ul>
                      <li><Link to="/about">about</Link></li>
                      <li><Link to="/repos">repos</Link></li>
                    </ul>
        
                    {this.props.children}
                  </div>
                )
              }
            }
        export default App

3. 定义配置文件 --> index.js

	       import React from 'react';
	       import ReactDOM from 'react-dom';
	       import {Router,Route,hashHistory,IndexRoute} from 'react-router';
	        
	       import App from './components/App';
	       import About from './components/About';
	       import Repos from './components/Repos';
	       import Home from './components/Home';
	        
	       ReactDOM.render((
	          <Router history={hashHistory}>
	             <Route path="/" component={App}>
	                <IndexRoute component={Home}></IndexRoute>
	                <Route path="/about" component={About}></Route>
	                <Route path="/repos" component={Repos}></Route>
	             </Route>
	          </Router>
	        ),
	       document.getElementById('root'));

4. 配置单页应用链接 Repos.js

        import React, {Component} from 'react';
        import {Link} from 'react-router';
        
        export default class Repos extends Component {
          constructor(props){
            super(props);
            this.state = {
              repos:[
                {name:'facebook',repo:'yarn'},
                {name:'facebook',repo:'react'},
                {name:'google',repo:'angular'},
                {name:'antd',repo:'antd'}
              ]
        
            }
          }
        render() {
          return (
            <div>
                <h3>Repos组件</h3>
                <ul>
                {
                  this.state.repos.map((item,index)=>{
                  return (
                    <li key={index}>
                        <Link activeClassName="active"
                        to={`/repos/${item.name}/${item.repo}`}>
                              {item.repo}
                        </Link>
                   </li>
                 )
              })
           }
               </ul>
                  {this.props.children}
               </div>
            )
          }
        }

5. 显示 Repo.js

        import React from 'react';
        
        function Repo({params}) {
          return (
              <p>
                用户名:{params.name}
                仓库名:{params.repo}
              </p>
          )
        }
        
        export default Repo
        
6. index.js 补充

        import Repo from './components/Repo';
        <Route path="/repos/:name/:repo" component={Repo}></Route>


----------

### Restless (非rest风格)
- http://wangyi.butterfly.mopaasapp.com/detail/api?simpleId=8
- 请求地址里有包含行为的表现
- 请求方式不能决定请求行为

### Restful API  (json_server)
- 请求方式可以决定请求行为
    - 请求行为
        - 添加
        - 更新 
        - 获取
        - 删除
- GET 只能请求数据
- POST 只能提交数据
- PUT 只能更新数据
- DELETE 只能删除数据
- 这种方法各司其职. 

