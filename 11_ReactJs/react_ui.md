### React-UI 
[material-ui](http://www.material-ui.com/#/) **国外常用**

[ANT DESIGN](https://ant.design/docs/react/getting-started-cn) **国内常用**

##### 使用create-react-app搭建react开发环境

1. 全局安装脚手架并创建项目
    - `npm install create-react-app -g`
    - `create-react-app antd-demo`
2. 搭建ant-design
    1. `npm install antd --save`
    2. 把对应插件引入就可使用(详见官网)
        - `import { Button ,DatePicker} from 'antd';`
3. 按需加载插件
    1. `npm run eject`
    2. `npm install babel-plugin-import --save-dev`
    3. 新增config/webpack.config.dev.js的配置
            
            query: {
               plugins: [
                 ['import', 
				 [{ libraryName: "antd", style: 'css' }]],
              ],

    4. src/App.css
        - `@import '~antd/dist/antd.css'`
        
---

### key={index}的问题
- 当虚拟DOM发生变化时,通过key的值找到发生变化的元素进行对比
- 哪里变化了就更新哪里. 没有变化的地方不会更新. 
- 如果key值找不到对应的旧元素,则直接"绘制"新的元素
- 所以在表单input里的内容没发生变化时,虚拟DOM是不会去改变的. 