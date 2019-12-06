
$(function(){
    if(!myChart2){
        var myChart2 = echarts.init(document.getElementById('mychart2'));
    }
    myChart2.showLoading({
        text: 'loading'
    })
    var d = new Date()
    var day = d.getDate()
    var month = d.getMonth() + 1
    var year = d.getFullYear()
    var name_1 = year + '-' + month + '-' + day + '-民生事件性质统计'
option = {
    title : {
        text: '民生事件性质分析',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        x : 'center',
        y : 'bottom',
        data:['投诉','咨询','建议','感谢','求决','其他']
    },
    toolbox: {
        show : true,
        feature: {
            myTool2: {
                show: true,
                title: '日期选择',
                icon: 'image://static/chart/mychart/img/timeset.jpg',
                onclick: function () {
                    if (document.getElementById('testchart').style.display == 'none') {
                        document.getElementById('testchart').style.display = 'block';
                    }
                    else {
                        document.getElementById('testchart').style.display = 'none';
                    }
                }
            },
            mark : {show: true},
            dataView : {show: true, readOnly: false},
            magicType : {
                show: true,
                type: ['pie', 'funnel']
            },
            restore : {show: true},
            saveAsImage: {
                show: true,
                name: name_1
            }
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
                {value:10, name:'投诉'},
                {value:5, name:'咨询'},
                {value:15, name:'建议'},
                {value:25, name:'感谢'},
                {value:20, name:'求决'},
                {value:35, name:'其他'}
            ]
        },
        {
            name:'面积模式',
            type:'pie',
            radius : [30, 110],
            center : ['75%', '50%'],
            roseType : 'area',
            data:[
                {value:10, name:'投诉'},
                {value:5, name:'咨询'},
                {value:15, name:'建议'},
                {value:25, name:'感谢'},
                {value:20, name:'求决'},
                {value:35, name:'其他'}
            ]
        }
    ]
};

    var deversion
    $(function () {
        var srcData = [];

        $.ajax({
            type: "get",
            async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
            url: "mychart2",    //请求发送到TestServlet处
            data: {},
            dataType: "json",        //返回数据形式为json
            success: function (result) {
                //请求成功时执行该函数内容，result即为服务器返回的json对象
                if (result) {
                    var version = result[0].version
                    for (var i = 1; i < result.length; i++) {
                        srcData.push({
                            value: result[i].value,
                            name: result[i].name
                        });
                    }
                    option.series[0].data = srcData;
                    option.series[1].data = srcData;
                    myChart2.hideLoading();
                    myChart2.clear();
                    myChart2.setOption(option, true);
                }
                deversion = version
            },
        })
    });

    setInterval(function () {
        var srcData = [];

        $.ajax({
            type: "get",
            async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
            url: "mychart2",    //请求发送到TestServlet处
            data: {},
            dataType: "json",        //返回数据形式为json
            success: function (result) {
                //请求成功时执行该函数内容，result即为服务器返回的json对象

                if (result) {
                    version = result[0].version

                    if (version != deversion || result[0].time_request==1) {
                        deversion = version
                        for (var i = 1; i < result.length; i++) {
                            srcData.push({
                                value: result[i].value,
                                name: result[i].name
                            });
                        }
                        option.series[0].data = srcData;
                        option.series[1].data = srcData;
                        myChart2.hideLoading();
                        myChart2.clear();
                        myChart2.setOption(option, true);
                    }
                }

            },
        })
    }, 10000);
});
