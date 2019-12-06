$(function(){
    var bmapChart = echarts.init(document.getElementById('map-wrap'));
    bmapChart.showLoading({
        text: '小地图迷路啦 正在找回'
    })
    var data = [
        {name: '坪山社区', value: 500}
    ];
    
    var geoCoordMap = {
        '南布社区':[114.375607,22.70534],
        '和平社区':[114.355204,22.697106],
        '坪山社区':[114.355432,22.694818],
        '汤坑社区':[114.331079,22.678805],
        '金沙社区':[114.406938,22.751133],
        '江岭社区':[114.362596,22.69202],
        '石井社区':[114.390978,22.697625],
        '六和社区':[114.3517,22.707447],
        '沙湖社区':[114.326552,22.67909],
        '老坑社区':[114.369312,22.734866],
        '竹坑社区':[114.395074,22.715773],
        '秀新社区':[114.381223,22.746873],
        '沙田社区':[114.404444,22.761764],
        '六联社区':[114.332971,22.795219],
        '坪环社区':[114.35474,22.688096],
        '龙田社区':[114.372841,22.753346],
        '坑梓社区':[114.390013,22.753031],
        '沙坣社区':[114.377888,22.690889],
        '田头社区':[114.410837,22.697197],
        '田心社区':[114.421943,22.700351],
        '碧岭社区':[114.295663,22.67342],
        '金龟社区':[114.406461,22.663744],
        '马峦社区':[114.338203,22.644538]
    };
    
    var convertData = function (data) {
        var res = [];
        for (var i = 0; i < data.length; i++) {
            var geoCoord = geoCoordMap[data[i].name];
            if (geoCoord) {
                res.push({
                    name: data[i].name,
                    value: geoCoord.concat(data[i].value)
                });
            }
        }
        return res;
    };
    
    
    var option = {
        backgroundColor: 'transparent',
        title: {
            text: '深圳市坪山区地区事件热度',
            subtext: 'data from MySql',
            left: 'center',
            textStyle: {
                color: '#fff'
            }
        },
        tooltip : {
            trigger: 'item',
            formatter: function(params) {
              var res = params.name+'<br/>';
              var myseries = option.series;
              for (var i = 0; i < myseries.length; i++) {
                  for(var j=0;j<myseries[i].data.length;j++){
                      if(myseries[i].data[j].name==params.name){
                        if(myseries[i].name=="Top 3")  
                          res="Top 3" + '</br>' + res;  
                        if(myseries[i].name=="事件数量")
                          res+=myseries[i].name +' : '+myseries[i].data[j].value[2]+'</br>';
                      }
                  }
              }
              return res;
          }
        },
        toolbox: {
        show : true,
        feature : {
            
            myTool2: {
                show: true,
                title: '日期选择',
                icon: 'image://static/chart/map/img/timeset.jpg',
                onclick: function (){
                    if(document.getElementById('testchart').style.display == 'none'){
                        document.getElementById('testchart').style.display = 'block';}
                    else{
                        document.getElementById('testchart').style.display = 'none';}
                }
            },
            restore:{show: true}
            
        }
        },
        bmap: {
            center: [114.360403,22.7301325],
               zoom: 13.7,

               roam: true, // 允许缩放

               mapStyle: {
                  'styleJson': [
                    {
                      'featureType': 'water',
                      'elementType': 'all',
                      'stylers': {
                        'color': '#031628'
                      }
                    },
                    {
                      'featureType': 'land',
                      'elementType': 'geometry',
                      'stylers': {
                        'color': '#000102'
                      }
                    },
                    {
                      'featureType': 'highway',
                      'elementType': 'all',
                      'stylers': {
                        'visibility': 'off'
                      }
                    },
                    {
                      'featureType': 'arterial',
                      'elementType': 'geometry.fill',
                      'stylers': {
                        'color': '#000000'
                      }
                    },
                    {
                      'featureType': 'arterial',
                      'elementType': 'geometry.stroke',
                      'stylers': {
                        'color': '#0b3d51'
                      }
                    },
                    {
                      'featureType': 'local',
                      'elementType': 'geometry',
                      'stylers': {
                        'color': '#000000'
                      }
                    },
                    {
                      'featureType': 'railway',
                      'elementType': 'geometry.fill',
                      'stylers': {
                        'color': '#000000'
                      }
                    },
                    {
                      'featureType': 'railway',
                      'elementType': 'geometry.stroke',
                      'stylers': {
                        'color': '#08304b'
                      }
                    },
                    {
                      'featureType': 'subway',
                      'elementType': 'geometry',
                      'stylers': {
                        'lightness': -70
                      }
                    },
                    {
                      'featureType': 'building',
                      'elementType': 'geometry.fill',
                      'stylers': {
                        'color': '#000000'
                      }
                    },
                    {
                      'featureType': 'all',
                      'elementType': 'labels.text.fill',
                      'stylers': {
                        'color': '#857f7f'
                      }
                    },
                    {
                      'featureType': 'all',
                      'elementType': 'labels.text.stroke',
                      'stylers': {
                        'color': '#000000'
                      }
                    },
                    {
                      'featureType': 'building',
                      'elementType': 'geometry',
                      'stylers': {
                        'color': '#022338'
                      }
                    },
                    {
                      'featureType': 'green',
                      'elementType': 'geometry',
                      'stylers': {
                        'color': '#062032'
                      }
                    },
                    {
                      'featureType': 'boundary',
                      'elementType': 'all',
                      'stylers': {
                        'color': '#465b6c'
                      }
                    },
                    {
                      'featureType': 'manmade',
                      'elementType': 'all',
                      'stylers': {
                        'color': '#022338'
                      }
                    },
                    {
                      'featureType': 'label',
                      'elementType': 'all',
                      'stylers': {
                        'visibility': 'off'
                      }
                    }
                  ]
                }
            },
            series : [
              {
                  name: '事件数量',
                  type: 'scatter',
                  coordinateSystem: 'bmap',
                  data: convertData(data),
                  symbolSize: function (val) {
                       var temp=(val[2]/20);
                       if(temp<10){
                         temp=10}
                      return temp;
                  },
                  label: {
                      normal: {
                          formatter: '{b}',
                          position: 'right',
                          show: false
                      },
                      emphasis: {
                          show: true
                      }
                  },
                  itemStyle: {
                      normal: {
                          color: '#Ff8c00'
                      }
                  }
              },
              {
                  name: 'Top 3',
                  type: 'effectScatter',
                  coordinateSystem: 'bmap',
                  data: convertData(data.sort(function (a, b) {
                      return b.value - a.value;
                  }).slice(0, 3)),
                  symbolSize: function (val) {
                      var temp=(val[2]/20);
                       if(temp<10){
                            temp=10;}
                      return temp;
                  },
                  showEffectOn: 'render',
                  rippleEffect: {
                      brushType: 'stroke'
                  },
                  hoverAnimation: true,
                  label: {
                      normal: {
                          formatter: '{b}',
                          position: 'right',
                          show: true
                      }
                  },
                  itemStyle: {
                      normal: {
                          color: 'orange',
                          shadowBlur: 10,
                          shadowColor: '#333'
                      }
                  },
                  zlevel: 1
              }
        ]
    };
var deversion
$(function(){
var srcData=[];     
  
  $.ajax({
  type : "get",
  async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
  url : "myMap",    //请求发送到TestServlet处
  data : {},
  dataType : "json",        //返回数据形式为json
  success : function(result) {
    //请求成功时执行该函数内容，result即为服务器返回的json对象
    if (result) {
        var version = result[0].version
         for(var i=1;i<result.length;i++){       
          srcData.push({
            name: result[i].name,
            value: result[i].value
        });
        }
         data=srcData;
         option.series[0].data=convertData(data);
         option.series[1].data=convertData(data.sort(function (a, b) {
                      return b.value - a.value;
                  }).slice(0, 3));
         bmapChart.hideLoading();  
         bmapChart.clear();
         bmapChart.setOption(option,true);
    }
    deversion = version
  },
  })
});

setInterval(function(){
  var srcData=[];     
  
  $.ajax({
  type : "get",
  async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
  url : "myMap",    //请求发送到TestServlet处
  data : {},
  dataType : "json",        //返回数据形式为json
  success : function(result) {
    //请求成功时执行该函数内容，result即为服务器返回的json对象
    if (result) {
         version = result[0].version
         for(var i=1;i<result.length;i++){       
          srcData.push({
            name: result[i].name,
            value: result[i].value
        });
        }
        if(version != deversion || result[0].time_request==1){
         deversion = version
         data=srcData;
         option.series[0].data=convertData(data);
         option.series[1].data=convertData(data.sort(function (a, b) {
                      return b.value - a.value;
                  }).slice(0, 5));
         bmapChart.hideLoading();  
         bmapChart.clear();
         bmapChart.setOption(option,true);}
    }
  
  },
  })
  },10000);










});



