$(function(){
    var bmapChart = echarts.init(document.getElementById('map-wrap'));

    var data = [
        {name: '某某山公园', value: 100},
        {name: 'b街道', value: 200},
        {name: 'c街道', value: 150},
        {name: 'd街道', value: 70},
        {name: 'e街道', value: 114},
        {name: 'f街道', value: 175},
        {name: '赤峰', value: 16},
        {name: '青岛', value: 18},
        {name: '乳山', value: 18},
        {name: '金昌', value: 19},
        {name: '泉州', value: 21},
        {name: '莱西', value: 21},
        {name: '日照', value: 21},
        {name: '胶南', value: 22},
        {name: '南通', value: 23},
        {name: '拉萨', value: 24},
        {name: '云浮', value: 24},
        {name: '梅州', value: 25},
        {name: '文登', value: 25},
        {name: '上海', value: 25},
        {name: '攀枝花', value: 25},
        {name: '威海', value: 25},
        {name: '承德', value: 25},
        {name: '厦门', value: 26},
        {name: '汕尾', value: 26},
        {name: '潮州', value: 26},
        {name: '丹东', value: 27},
        {name: '太仓', value: 27},
        {name: '曲靖', value: 27},
        {name: '烟台', value: 28},
        {name: '福州', value: 29},
        {name: '瓦房店', value: 30},
        {name: '即墨', value: 30},
        {name: '抚顺', value: 31},
        {name: '玉溪', value: 31},
        {name: '张家口', value: 31},
        {name: '阳泉', value: 31},
        {name: '莱州', value: 32},
        {name: '湖州', value: 32},
        {name: '汕头', value: 32},
        {name: '昆山', value: 33},
        {name: '宁波', value: 33},
        {name: '湛江', value: 33},
        {name: '揭阳', value: 34},
        {name: '荣成', value: 34},
        {name: '连云港', value: 35},
        {name: '葫芦岛', value: 35},
        {name: '常熟', value: 36},
        {name: '东莞', value: 36},
        {name: '河源', value: 36},
        {name: '淮安', value: 36},
        {name: '泰州', value: 36},
        {name: '南宁', value: 37},
        {name: '营口', value: 37},
        {name: '惠州', value: 37},
        {name: '江阴', value: 37},
        {name: '蓬莱', value: 37},
        {name: '韶关', value: 38},
        {name: '嘉峪关', value: 38},
        {name: '广州', value: 38},
        {name: '延安', value: 38},
        {name: '太原', value: 39},
        {name: '清远', value: 39},
        {name: '中山', value: 39},
        {name: '昆明', value: 39},
        {name: '寿光', value: 40},
        {name: '盘锦', value: 40},
        {name: '长治', value: 41},
        {name: '深圳', value: 41},
        {name: '珠海', value: 42},
        {name: '宿迁', value: 43},
        {name: '咸阳', value: 43},
        {name: '铜川', value: 44},
        {name: '平度', value: 44},
        {name: '佛山', value: 44},
        {name: '海口', value: 44},
        {name: '江门', value: 45},
        {name: '章丘', value: 45},
        {name: '肇庆', value: 46},
        {name: '大连', value: 47},
        {name: '临汾', value: 47},
        {name: '吴江', value: 47},
        {name: '石嘴山', value: 49},
        {name: '沈阳', value: 50},
        {name: '苏州', value: 50},
        {name: '茂名', value: 50},
        {name: '嘉兴', value: 51},
        {name: '长春', value: 51},
        {name: '胶州', value: 52},
        {name: '银川', value: 52},
        {name: '张家港', value: 52},
        {name: '三门峡', value: 53},
        {name: '锦州', value: 54},
        {name: '南昌', value: 54},
        {name: '柳州', value: 54},
        {name: '三亚', value: 54},
        {name: '自贡', value: 56},
        {name: '吉林', value: 56},
        {name: '阳江', value: 57},
        {name: '泸州', value: 57},
        {name: '西宁', value: 57},
        {name: '宜宾', value: 58},
        {name: '呼和浩特', value: 58},
        {name: '成都', value: 58},
        {name: '大同', value: 58},
        {name: '镇江', value: 59},
        {name: '桂林', value: 59}
    ];
    
    var geoCoordMap = {
        '某某山公园':[114.363403,22.7061325],
        'b街道':[114.36,22.70],
        'c街道':[114.369,22.707],
        'd街道':[114.3610,22.711],
        'e街道':[114.3622,22.699],
        'f街道':[114.3655,22.69],
        '赤峰':[114.369,99],
        '青岛':[120.33,36.07],
        '乳山':[121.52,36.89],
        '金昌':[102.188043,38.520089],
        '泉州':[118.58,24.93],
        '莱西':[120.53,36.86],
        '日照':[119.46,35.42],
        '胶南':[119.97,35.88],
        '南通':[121.05,32.08],
        '拉萨':[91.11,29.97],
        '云浮':[112.02,22.93],
        '梅州':[116.1,24.55],
        '文登':[122.05,37.2],
        '上海':[121.48,31.22],
        '攀枝花':[101.718637,26.582347],
        '威海':[122.1,37.5],
        '承德':[117.93,40.97],
        '厦门':[118.1,24.46],
        '汕尾':[115.375279,22.786211],
        '潮州':[116.63,23.68],
        '丹东':[124.37,40.13],
        '太仓':[121.1,31.45],
        '曲靖':[103.79,25.51],
        '烟台':[121.39,37.52],
        '福州':[119.3,26.08],
        '瓦房店':[121.979603,39.627114],
        '即墨':[120.45,36.38],
        '抚顺':[123.97,41.97],
        '玉溪':[102.52,24.35],
        '张家口':[114.87,40.82],
        '阳泉':[113.57,37.85],
        '莱州':[119.942327,37.177017],
        '湖州':[120.1,30.86],
        '汕头':[116.69,23.39],
        '昆山':[120.95,31.39],
        '宁波':[121.56,29.86],
        '湛江':[110.359377,21.270708],
        '揭阳':[116.35,23.55],
        '荣成':[122.41,37.16],
        '连云港':[119.16,34.59],
        '葫芦岛':[120.836932,40.711052],
        '常熟':[120.74,31.64],
        '东莞':[113.75,23.04],
        '河源':[114.68,23.73],
        '淮安':[119.15,33.5],
        '泰州':[119.9,32.49],
        '南宁':[108.33,22.84],
        '营口':[122.18,40.65],
        '惠州':[114.4,23.09],
        '江阴':[120.26,31.91],
        '蓬莱':[120.75,37.8],
        '韶关':[113.62,24.84],
        '嘉峪关':[98.289152,39.77313],
        '广州':[113.23,23.16],
        '延安':[109.47,36.6],
        '太原':[112.53,37.87],
        '清远':[113.01,23.7],
        '中山':[113.38,22.52],
        '昆明':[102.73,25.04],
        '寿光':[118.73,36.86],
        '盘锦':[122.070714,41.119997],
        '长治':[113.08,36.18],
        '深圳':[114.07,22.62],
        '珠海':[113.52,22.3],
        '宿迁':[118.3,33.96],
        '咸阳':[108.72,34.36],
        '铜川':[109.11,35.09],
        '平度':[119.97,36.77],
        '佛山':[113.11,23.05],
        '海口':[110.35,20.02],
        '江门':[113.06,22.61],
        '章丘':[117.53,36.72],
        '肇庆':[112.44,23.05],
        '大连':[121.62,38.92],
        '临汾':[111.5,36.08],
        '吴江':[120.63,31.16],
        '石嘴山':[106.39,39.04],
        '沈阳':[123.38,41.8],
        '苏州':[120.62,31.32],
        '茂名':[110.88,21.68],
        '嘉兴':[120.76,30.77],
        '长春':[125.35,43.88],
        '胶州':[120.03336,36.264622],
        '银川':[106.27,38.47],
        '张家港':[120.555821,31.875428],
        '三门峡':[111.19,34.76],
        '锦州':[121.15,41.13],
        '南昌':[115.89,28.68],
        '柳州':[109.4,24.33],
        '三亚':[109.511909,18.252847],
        '自贡':[104.778442,29.33903],
        '吉林':[126.57,43.87],
        '阳江':[111.95,21.85],
        '泸州':[105.39,28.91],
        '西宁':[101.74,36.56],
        '宜宾':[104.56,29.77],
        '呼和浩特':[111.65,40.82],
        '成都':[104.06,30.67],
        '大同':[113.3,40.12],
        '镇江':[119.44,32.2],
        '桂林':[110.28,25.29]
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
    
    function renderItem(params, api) {
        var coords = [
            [116.7,39.53],
            [103.73,36.03],
            [112.91,27.87],
            [120.65,28.01],
            [119.57,39.95]
        ];
        var points = [];
        for (var i = 0; i < coords.length; i++) {
            points.push(api.coord(coords[i]));
        }
        var color = api.visual('color');
    
        return {
            type: 'polygon',
            shape: {
                points: echarts.graphic.clipPointsByRect(points, {
                    x: params.coordSys.x,
                    y: params.coordSys.y,
                    width: params.coordSys.width,
                    height: params.coordSys.height
                })
            },
            style: api.style({
                fill: color,
                stroke: echarts.color.lift(color)
            })
        };
    }
    
    option = {
        backgroundColor: 'transparent',
        title: {
            text: '深圳市坪山区地区事件热度',
            subtext: 'data from MySql',
            sublink: 'http://www.baidu.com',
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
                        if(myseries[i].name=="Top 5")  
                          res="Top 5" + '</br>' + res;  
                        if(myseries[i].name=="事件数量")
                          res+=myseries[i].name +' : '+myseries[i].data[j].value[2]+'</br>';
                      }
                  }
              }
              return res;
          }
        },
        bmap: {
            center: [114.363403,22.7061325],
               zoom: 14,

               roam: false, // 允许缩放

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
                      return val[2] / 10;
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
                          color: '#ddb926'
                      }
                  }
              },
              {
                  name: 'Top 5',
                  type: 'effectScatter',
                  coordinateSystem: 'bmap',
                  data: convertData(data.sort(function (a, b) {
                      return b.value - a.value;
                  }).slice(0, 5)),
                  symbolSize: function (val) {
                      return val[2] / 10;
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

bmapChart.setOption(option);
});
