## meta标签
	<meta name="viewport" content="" />
		width=device-width 布局视口等于理想视口等于可视视口
		initial-scale 初始缩放比例 (根据理想视口)
		user-scalable 是否允许缩放 （no||yes）,默认允许
		minimum-scale 允许缩放的最小比例
		maximum-scale 允许缩放的最大比例 

- `<meta name="viewport" content="width=device-width" />`
- 缺点: 太大的元素浏览器的布局视口会尽量的包裹住元素
#### meta标签完美视口
	<meta name="viewport" 
	content="width=device-width,
			 initial-scale=1.0",
			 user-scalable=no />`
- 布局视口 = 视觉视口 = 理想视口
- 实际是包含的css像素一样多

#### with和inital-scale的冲突
- 布局视口在width与inital-scale产生分歧时会选择他们中比较大的那一个
- width=device-width,initial-scale=2.0 (375 width)
- width=device-width,initial-scale=1.0 (375 width)
- width=device-width,initial-scale=0.5 (750 initial-scale)
