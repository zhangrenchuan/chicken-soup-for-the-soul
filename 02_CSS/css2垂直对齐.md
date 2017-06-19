## CSS2 vertical-align 垂直对齐

	- baseline   默认值.基于基线对齐
	- middle     位于同一行的非衬线字体小写字母的 1/2 处.不要为父元素设置高度和行高      
	- top           位于父元素一行的顶部
	- bottom    位于父元素一行的底部
	- text-top   位于同一行的文本的顶部
	- text-bottom 位于同一行的文本的底部
	- super       位于同一行的sub元素文本的基线对齐 <sup>上角标</sup>
	- sub          位于同一行的sub元素文本的基线对齐 <sub>下角标</sub> 
	
- 使用 vertical-align 在一行内，行内元素在垂直方向的对齐位置。
- vertical-align: 只能设置行内元素（inline inline-block)

#### 垂直居中对齐

	vertical-align: middle;
	text-align: center;

#### vertical-align 使用场景1： 一行内的垂直方向对齐
![](http://i.imgur.com/gqvFjtp.jpg)

####  vertical-align 使用场景2： 多行内的垂直方向对齐 
1. 为要垂直居中的子元素设置 ````vertical-align:middle````样式
2. 为该元素的父元素设置````display: table-cell````,并设置固定的高度
3. 然后再设置 ````vertical-align:middle````和水平对齐````text-align: center````
4. 当其元素设置为 ````display: table-cell````.并且宽度清零时，需要为父元素添加display: table;，并设置宽度100%

**可以把元素的所有内容（文本，子元素-inline, inline-block）都在垂直方向居中**

**在局部布局中使用display:table-cell;以减少对整体布局的影响**

	    <style type="text/css">
	        /*指定块元素图片垂直居中*/
	        .box-table{
	            display: table;
	            width:100%;
	        }
	        .box {
	            background-color: orange;

	            height: 200px;
	            display: table-cell;
	            vertical-align: middle;
	            text-align: center;
	        }
	        img{
	            width: 100px;
	        }
	    </style>
	
	    <script type="text/javascript"></script>
		</head>
		<body>
	
		<div class="box-table">
		    <div class="box">
		        <img src="img/bg.jpg" alt="">
		    </div>
		</div>
		</body>
