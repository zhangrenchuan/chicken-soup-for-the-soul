## React Ajax
##### 集成axios
- npm 
    - `npm install axios --save`
- BootCDN
    - `https://cdn.bootcss.com/axios/0.16.1/axios.js`
- [axios](https://github.com/mzabriskie/axios)

		//GET
		axios.get('/user?ID=12345')
		  .then(function (response) {
		    console.log(response);
		  })
		  .catch(function (error) {
		    console.log(error);
		  });

		//POST
		axios.post('/user', {
		    firstName: 'Fred',
		    lastName: 'Flintstone'
		  })
		  .then(function (response) {
		    console.log(response);
		  })
		  .catch(function (error) {
		    console.log(error);
		  });


##### 集成fetch
- BootCDN
    - `https://cdn.bootcss.com/fetch/2.0.1/fetch.min.js`
- [fetch](https://segmentfault.com/a/1190000003810652)

		fetch(url).then(function(response) {
		  return response.json();
		}).then(function(data) {
		  console.log(data);
		}).catch(function(e) {
		  console.log("Oops, error");
		});

		
		//ES6 箭头函数
		fetch(url).then(response => response.json())
		  .then(data => console.log(data))
		  .catch(e => console.log("Oops, error", e))