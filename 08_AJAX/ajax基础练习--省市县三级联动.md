## 省市县三级联动

#### 需求:

   1. 自动填充省份
   2. 选择某个省, 填充该省的所有的市
   3. 选择某个市, 填充该市所有的区县

     1. 动态获取数据
         ajax

     2. 服务器必须响应请求


#### 前后端接口文档

       1. 获得省的数据
         发出去的数据
           - 方法: get
           - url文件路径: /province
           - 参数:
        收到的数据
           {
             province: []
           }


       2. 获得城市的数据
       发出去的数据
          - 方法: get
          - url文件路径: /city
          - 参数: provinceId
       收到的数据
          {
            city: []
          }

      3. 获得区县的数据
        发出去的数据
          - 方法: get
          - url文件路径: /county
          - 参数: cityId
        收到的数据
          {
            county: []
           }


----------

### 后台服务器设置


**1.引入国家省市县**

	var china_area = require('../china.json'); //require自动转换对象


**2.省的接口**

	router.get('/province',function (req,res,next) {
	  //根据接口文档规范编写
	  var obj = {
	    province : china_area.province
	  };
		  res.send(obj)
	});


**3.市的接口**

	router.get('/city',function (req,res,next) {
		//获取省的id
	  var provinceId = req.query.provinceId;
	  var cities = [];
		
		//遍历城市
	  china_area.city.forEach(function (ele,index) {
		//进行城市匹配省份判断 普通城市或直辖市
	    if(ele.parent === provinceId || ele.id === provinceId){ //普通城市或直辖市
	      cities.push(ele);
	    }
	  });
	
	  //根据接口文档规范编写
	  var obj = {
	    cities : cities
	  };
	  res.send(obj)
	});


**4.区县的接口**

	router.get('/county',function (req,res,next) {
		   //获取市的id
		  var cityId = req.query.cityId;
		  var countys = [];
	
	//遍历区和县
	china_area.county.forEach(function (ele,index) {
			//进行区县匹配城市的判断
    	  if(ele.parent === cityId){
          countys.push(ele)
	    }
	});
	
	    //根据接口文档规范编写
	    var obj = {
	      countys : countys
	    };
	    res.send(obj)
    });


----------

### 前端显示页面设置

	<select id="selProvince">
	  <option value="">--请选择省份--</option>
	</select>
	<select id="selCity">
	  <option value="">--请选择城市--</option>
	</select>
	<select id="selCounty">
	  <option value="">--请选择区/县--</option>
	</select>

	<script type="text/javascript" src="../js/jquery-1.11.1.js"></script>

----------


**1.获取多选框**

	$(function () {

	  var $province = $('#selProvince');
	  var $city = $('#selCity');
	  var $county = $('#selCounty');
	
**2.把省份的数据从服务器传送回来**

//forEach()遍历接收一个函数作为参数.

//该函数接收两个参数 1. 元素ele, 2. 下标index

	  $.getJSON('/province',function (data) {
	    //获取省份数据的数组
	    var provinceArr = data.province;

		//遍历省份数据
	    provinceArr.forEach(function (ele,index) {
	      //把获取到的数据显示到下拉列表中
	      var str = '<option value="'+ ele.id +'">'+ ele.province +'</option>';
	      $(str).appendTo($province)
	    });
	  });
	
	
	
**3.当选择某个省市,  出现对应的市**

	  $province.change(function () {
		  //得到用户选择的省的id
	  	  var provinceId = this.value; 

	      //清空市和区县下拉列表之前的数据
	      $city.children().not(':first').remove();
	      $county.children().not(':first').remove();
	
		  //如果不选择市的话不需要进行ajax请求
	      if(provinceId === ""){
	        return;
	      }
	
	      $.getJSON('/city',{provinceId:provinceId},function (data) {
	
			//城市数据遍历
	        data.cities.forEach(function (ele,index) {
	          var str = '<option value="'+ ele.id +'">'+ ele.city +'</option>';
	          $(str).appendTo($city);
	        })
	      });
	  });
	
	
**选择市之后, 出现对应的区 县**

	 $city.change(function () {
		//得到用户选择的市的id
	    var cityId = this.value; 

		//清除县或区之前的数据
	    $county.children().not(':first').remove();

		//如果不选择市的话不需要进行ajax请求
	    if(cityId === ""){
	      return;
	    }
	
	  $.getJSON('/county',{cityId:cityId},function (data) {
	
		//区和县数据遍历
	      data.countys.forEach(function (ele,index) {
	        var str = '<option value="'+ ele.id +'">'+ ele.county +'</option>';
	        $(str).appendTo($county);
	      })
	    });
	  });
	})