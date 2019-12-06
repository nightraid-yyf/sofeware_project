$(function(){
    if(!myChart3){
        var myChart3 = echarts.init(document.getElementById('mychart3'));
    }
    myChart3.showLoading({
        text: 'loading'
    })
    var d = new Date()
    var day = d.getDate()
    var month = d.getMonth() + 1
    var year = d.getFullYear()
    var name_1 = year + '-' + month + '-' + day + '-民生事件结办分析'
option = {
    tooltip: {
        trigger: 'item',
        formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        x: 'left',
        data:['市容环卫','环保水务','市政设施','规土城建','教育卫生','安全隐患','组织人事','党纪政纪','劳动社保','社区管理','交通运输','治安维稳','专业事件采集','统一战线','民政服务','文体旅游','食药市监','党建群团','处置中','超期结办','按期结办']
    },
    toolbox: {
        show: true,
        left: '90%',
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
            saveAsImage: {
                show: true,
                name: name_1
            }
        }
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
                {value:335, name:'超期结办', selected:true},
                {value:679, name:'处置中'},
                {value:1548, name:'按期结办'}
            ]
        },
        {
            name:'事件类型',
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
                {value:335, name:'市容环卫'},
                {value:310, name:'环保水务'},
                {value:234, name:'市政设施'},
                {value:135, name:'规土城建'},
                {value:1048, name:'教育卫生'},
                {value:251, name:'安全隐患'},
                {value:147, name:'组织人事'},
                {value:102, name:'党纪政纪'},
                {value:102, name:'劳动社保'},
                {value:102, name:'社区管理'},
                {value:102, name:'交通运输'},
                {value:102, name:'治安维稳'},
                {value:102, name:'专业事件采集'},
                {value:102, name:'统一战线'},
                {value:102, name:'民政服务'},
                {value:102, name:'文体旅游'},
                {value:102, name:'食药市监'},
                {value:102, name:'党建群团'}
            ]
        }
    ]
};

    var deversion
    $(function () {
        var srcData_1 = [];
        var srcData_2 = [];

        $.ajax({
            type: "get",
            async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
            url: "mychart3",    //请求发送到TestServlet处
            data: {},
            dataType: "json",        //返回数据形式为json
            success: function (result) {
                //请求成功时执行该函数内容，result即为服务器返回的json对象
                if (result) {
                    var version = result[0].version
                    for (var i = 1; i <= result[0].length1; i++) {
                        srcData_1.push({
                            value: result[i].value,
                            name: result[i].name
                        });
                    }
                    for (var i = 1; i <= result[0].length2; i++) {
                        srcData_2.push({
                            value: result[i + result[0].length1].value,
                            name: result[i + result[0].length1].name
                        });
                    }
                    option.series[0].data = srcData_1;
                    option.series[1].data = srcData_2;
                    myChart3.hideLoading();
                    myChart3.clear();
                    myChart3.setOption(option, true);
                }
                deversion = version
            },
        })
    });

    setInterval(function () {
        var srcData_1 = [];
        var srcData_2 = [];
        $.ajax({
            type: "get",
            async : true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
            url: "mychart3",    //请求发送到TestServlet处
            data: {},
            dataType: "json",        //返回数据形式为json
            success: function (result) {
                //请求成功时执行该函数内容，result即为服务器返回的json对象

                if (result) {
                    version = result[0].version

                    if (version != deversion || result[0].time_request == 1) {
                        deversion = version
                        for (var i = 1; i <= result[0].length1; i++) {
                            srcData_1.push({
                                value: result[i].value,
                                name: result[i].name
                            });
                        }
                        for (var i = 1; i <= result[0].length2; i++) {
                            srcData_2.push({
                                value: result[i + result[0].length1].value,
                                name: result[i + result[0].length1].name
                            });
                        }
                        option.series[0].data = srcData_1;
                        option.series[1].data = srcData_2;
                        myChart3.hideLoading();
                        myChart3.clear();
                        myChart3.setOption(option, true);
                    }
                }

            },
        })
    }, 10000);

});
