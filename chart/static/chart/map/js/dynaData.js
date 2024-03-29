
function dynamicData(Chart){
	$.get('getData').done(function (data){
	var dataSour = $.parseJSON(data);
	Chart.setOption(function(){
		dataset: [
			{source: dataSour.source},
		] 
	},1000);
	});
}
$(function(){
var names=[];    //类别数组（实际用来盛放X轴坐标值）
var nums=[];    //销量数组（实际用来盛放Y坐标值）

$.ajax({
type : "post",
async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
url : "TestServlet",    //请求发送到TestServlet处
data : {},
dataType : "json",        //返回数据形式为json
success : function(result) {
	//请求成功时执行该函数内容，result即为服务器返回的json对象
	if (result) {
		   for(var i=0;i<result.length;i++){       
			  names.push(result[i].name);    //挨个取出类别并填入类别数组
			}
		   for(var i=0;i<result.length;i++){       
			   nums.push(result[i].num);    //挨个取出销量并填入销量数组
			 }
		   myChart.hideLoading();    //隐藏加载动画
		   myChart.setOption({        //加载数据图表
			   xAxis: {
				   data: names
			   },
			   series: [{
				   // 根据名字对应到相应的系列
				   name: '销量',
				   data: nums
			   }]
		   });
		   
	}

},
error : function(errorMsg) {
	//请求失败时执行该函数
alert("图表请求数据失败!");
myChart.hideLoading();
}
})
});