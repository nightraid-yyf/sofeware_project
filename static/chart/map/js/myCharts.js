
$(function(){
	// <script src="./echarts3.js"></script>
	// <script src="./jquery-1.7.2.js"></script>
	// <script src="./dynaData.js"></script>

		if(!myChart1){
			var myChart1 = echarts.init(document.getElementById('leftTop'));
		}
		if(!myChart2){
			var myChart2= echarts.init(document.getElementById('leftBottom'));
		}
		if(!myChart3){
			var myChart3= echarts.init(document.getElementById('rightTop'));
		}
		if(!myChart4){
			var myChart4= echarts.init(document.getElementById('rightBottom'));
		}
		
		
		
		
		function randomData() {
			now = new Date(+now + oneDay);
			value = value + Math.random() * 21 - 10;
			return {
				//name : now.toString(),
				value : [
						[ now.getFullYear(), now.getMonth() + 1, now.getDate() ]
								.join('/'), Math.round(value) ]
			}
		}

//		var data = [];
	//	var now = +new Date(1997, 9, 3);
		//var oneDay = 24 * 3600 * 1000;
		//var value = Math.random() * 1000;
		//for (var i = 0; i < 1000; i++) {
			//data.push(randomData());
		//}

		option = {
			tooltip : {
				trigger: 'axis',
				axisPointer : {            // 坐标轴指示器，坐标轴触发有效
					type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
				}
			},
			legend: {
				data:['直接访问','邮件营销','联盟广告','视频广告','搜索引擎','百度','谷歌','必应','其他']
			},
			grid: {
				left: '3%',
				right: '4%',
				bottom: '3%',
				containLabel: true
			},
			xAxis : [
				{
					type : 'category',
					data : ['周一','周二','周三','周四','周五','周六','周日']
				}
			],
			yAxis : [
				{
					type : 'value'
				}
			],
			series : [
				{
					name:'直接访问',
					type:'bar',
					data:[320, 332, 301, 334, 390, 330, 320]
				},
				{
					name:'邮件营销',
					type:'bar',
					stack: '广告',
					data:[120, 132, 101, 134, 90, 230, 210]
				},
				{
					name:'联盟广告',
					type:'bar',
					stack: '广告',
					data:[220, 182, 191, 234, 290, 330, 310]
				},
				{
					name:'视频广告',
					type:'bar',
					stack: '广告',
					data:[150, 232, 201, 154, 190, 330, 410]
				},
				{
					name:'搜索引擎',
					type:'bar',
					data:[862, 1018, 964, 1026, 1679, 1600, 1570],
				   // markLine : {
					 //   lineStyle: {
					   //     normal: {
						 //       type: 'dashed'
						   // }
						//},
						//data : [
						  //  [{type : 'min'}, {type : 'max'}]
						//]
					//}
				},
				{
					name:'百度',
					type:'bar',
					barWidth : 5,
					stack: '搜索引擎',
					data:[620, 732, 701, 734, 1090, 1130, 1120]
				},
				{
					name:'谷歌',
					type:'bar',
					stack: '搜索引擎',
					data:[120, 132, 101, 134, 290, 230, 220]
				},
				{
					name:'必应',
					type:'bar',
					stack: '搜索引擎',
					data:[60, 72, 71, 74, 190, 130, 110]
				},
				{
					name:'其他',
					type:'bar',
					stack: '搜索引擎',
					data:[62, 82, 91, 84, 109, 110, 120]
				}
			]
		};
		option2 = {
			title: {
				text: '漏斗图',
				subtext: '纯属虚构'
			},
			tooltip: {
				trigger: 'item',
				formatter: "{a} <br/>{b} : {c}%"
			},
			toolbox: {
				feature: {
					dataView: {readOnly: false},
					restore: {},
					saveAsImage: {}
				}
			},
			legend: {
				data: ['展现','点击','访问','咨询','订单']
			},
			calculable: true,
			series: [
				{
					name:'漏斗图',
					type:'funnel',
					left: '10%',
					top: 60,
					//x2: 80,
					bottom: 60,
					width: '80%',
					// height: {totalHeight} - y - y2,
					min: 0,
					max: 100,
					minSize: '0%',
					maxSize: '100%',
					sort: 'descending',
					gap: 2,
					label: {
						show: true,
						position: 'inside'
					},
					labelLine: {
						length: 10,
						lineStyle: {
							width: 1,
							type: 'solid'
						}
					},
					itemStyle: {
						borderColor: '#fff',
						borderWidth: 1
					},
					emphasis: {
						label: {
							fontSize: 20
						}
					},
					data: [
						{value: 60, name: '访问'},
						{value: 40, name: '咨询'},
						{value: 20, name: '订单'},
						{value: 80, name: '点击'},
						{value: 100, name: '展现'}
					]
				}
			]
		};

		option3 = {
			title : {
				text: '南丁格尔玫瑰图',
				subtext: '纯属虚构',
				x:'center'
			},
			tooltip : {
				trigger: 'item',
				formatter: "{a} <br/>{b} : {c} ({d}%)"
			},
			legend: {
				x : 'center',
				y : 'bottom',
				data:['rose1','rose2','rose3','rose4','rose5','rose6','rose7','rose8']
			},
			toolbox: {
				show : true,
				feature : {
					mark : {show: true},
					dataView : {show: true, readOnly: false},
					magicType : {
						show: true,
						type: ['pie', 'funnel']
					},
					restore : {show: true},
					saveAsImage : {show: true}
				}
			},
			calculable : true,
			series : [
				{
					name:'半径模式',
					type:'pie',
					radius : [20, 110],
					center : ['25%', '50%'],
					roseType : 'radius',
					label: {
						normal: {
							show: false
						},
						emphasis: {
							show: true
						}
					},
					lableLine: {
						normal: {
							show: false
						},
						emphasis: {
							show: true
						}
					},
					data:[
						{value:10, name:'rose1'},
						{value:5, name:'rose2'},
						{value:15, name:'rose3'},
						{value:25, name:'rose4'},
						{value:20, name:'rose5'},
						{value:35, name:'rose6'},
						{value:30, name:'rose7'},
						{value:40, name:'rose8'}
					]
				},
				{
					name:'面积模式',
					type:'pie',
					radius : [30, 110],
					center : ['75%', '50%'],
					roseType : 'area',
					data:[
						{value:10, name:'rose1'},
						{value:5, name:'rose2'},
						{value:15, name:'rose3'},
						{value:25, name:'rose4'},
						{value:20, name:'rose5'},
						{value:35, name:'rose6'},
						{value:30, name:'rose7'},
						{value:40, name:'rose8'}
					]
				}
			]
		};

		option4 = {
			tooltip: {
				trigger: 'item',
				formatter: "{a} <br/>{b}: {c} ({d}%)"
			},
			legend: {
				orient: 'vertical',
				x: 'left',
				data:['直达','营销广告','搜索引擎','邮件营销','联盟广告','视频广告','百度','谷歌','必应','其他']
			},
			series: [
				{
					name:'访问来源',
					type:'pie',
					selectedMode: 'single',
					radius: [0, '30%'],

					label: {
						normal: {
							position: 'inner'
						}
					},
					labelLine: {
						normal: {
							show: false
						}
					},
					data:[
						{value:335, name:'直达', selected:true},
						{value:679, name:'营销广告'},
						{value:1548, name:'搜索引擎'}
					]
				},
				{
					name:'访问来源',
					type:'pie',
					radius: ['40%', '55%'],
					label: {
						normal: {
							//formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
							formatter: '{a|{a}}{abg|}\n{hr|}\n  {b|{b}：}{c}  {per|{d}%}  ',
							backgroundColor: '#eee',
							borderColor: '#aaa',
							borderWidth: 1,
							borderRadius: 4,
							// shadowBlur:3,
							// shadowOffsetX: 2,
							// shadowOffsetY: 2,
							// shadowColor: '#999',
							// padding: [0, 7],
							rich: {
								a: {
									color: '#999',
									lineHeight: 22,
									align: 'center'
								},
								// abg: {
								//     backgroundColor: '#333',
								//     width: '100%',
								//     align: 'right',
								//     height: 22,
								//     borderRadius: [4, 4, 0, 0]
								// },
								hr: {
									borderColor: '#aaa',
									width: '100%',
									borderWidth: 0.5,
									height: 0
								},
								b: {
									fontSize: 16,
									lineHeight: 33
								},
								per: {
									color: '#eee',
									backgroundColor: '#334455',
									padding: [2, 4],
									borderRadius: 2
								}
							}
						}
					},
					data:[
						{value:335, name:'直达'},
						{value:310, name:'邮件营销'},
						{value:234, name:'联盟广告'},
						{value:135, name:'视频广告'},
						{value:1048, name:'百度'},
						{value:251, name:'谷歌'},
						{value:147, name:'必应'},
						{value:102, name:'其他'}
					]
				}
			]
		};

		myChart1.setOption(option,1);
		myChart2.setOption(option2,1);
		myChart3.setOption(option3,1);
		myChart4.setOption(option4,1);
		dynamic=dynamicData;
		dynamic(myChart1);
		dynamic(myChart2);
		dynamic(myChart3);
		dynamic(myChart4);
	//	test1=test;
	//	test1(myChart1);
	setInterval(function() {

		for (var i = 0; i < 5; i++) {
			data.shift();//删除数组第一个元素
			//data.push(randomData());//向数组中添加元素
		}

		myChart1.setOption({
			series : [ {
				data : data
			} ]
		});
	}, 1000);
});
