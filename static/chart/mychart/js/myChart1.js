
$(function () {
    if (!myChart1) {
        var myChart1 = echarts.init(document.getElementById('mychart1'));
    }
    myChart1.showLoading({
        text: '数据查询中,请勿刷新'
    })
    var d = new Date()
    var day = d.getDate()
    var month = d.getMonth() + 1
    var year = d.getFullYear()
    var name_1 = year + '-' + month + '-' + day +'-街道民生事件情况'
    option = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            data: ['市容城管', '禽畜养殖污染', '市政、公共设施设置及维护', '商业经营噪声', '城乡规划', '房屋征收', '宣传广告违法行为', '工业噪声', '教育行政管理', '占道经营', '垃圾问题', '绿化养护', '公用部件', '交通设施', '废弃物堆放', '道路交通安全', '车辆乱停放', '社会生活噪声', '道路保洁', '医患纠纷', '人力资源', '行政效能', '医政监管', '道路设施', '水污染', '招生中的违法行为', '教育体制', '城市建设和市政管理', '其他市容违法行为或影响市容事件', '劳动就业', '劳动社保', '住宅区（园区）或建筑物内安全、环卫问题', '渣土问题', '公共交通管理', '建筑施工噪声', '违法建筑与用地行为', '供、排水及水质问题', '道路规划建设', '扬尘污染', '环卫设施设置及维护', '住房保障和房地产', '集体土地上房屋拆迁与补偿', '营业性文化娱乐噪声', '工业、住宅废气扰民', '经济纠纷', '建设工程质量', '城市公共资源管理', '服务行业废气扰民', '人口房屋', '综合事件采集', '社会治安', '土地资源管理', '教育收费', '违反计生政策', '工商经济联络', '交通运输噪声', '其他公共安全隐患', '消防设施安全', '建筑市场', '建筑消防安全', '危险化学品安全', '医疗机构违规经营', '教学违规', '环保标志管理', '双拥优抚', '环保管理', '物业服务管理监督', '宣传舆论', '互联网与通讯', '户籍证件', '警务督察', '经济管理', '线路消防安全', '社区公共管理', '医疗机构违规收费', '药品（医疗器械）监管', '面源污染隐患', '党的建设', '表达情感', '福利慈善', '刑案侦破', '公共设施保洁', '消费维权', '地质安全', '野生资源管理', '社会组织', '军转安置', '生态破坏', '劳动保护', '安全生产', '社区建设', '无证无照经营', '文化', '危险废物、化学品污染', '质监检验检疫', '燃气安全', '社会救助', '公共卫生', '商标管理', '国有土地上房屋征收与补偿', '固体废物', '经济违法行为举报', '教师队伍和待遇', '出入境检验检疫', '价格监管', '普法教育', '食品安全', '小散乱污', '建筑设计', '义工联', '复退安置', '核安全', '人口计生', '体育', '校园安全', '民间纠纷', '招录辞退', '食药监问题', '征转地审批', '旅游市场管理', '工作纪律', '跨河桥、河堤、河道破损', '卫生问题', '科学技术', '编制职务', '宣传教育', '建筑安装', '信息化建设', '网约车管理', '知识产权', '更改房屋结构', '市场垄断', '文化市场违法行为']
            , show: true,
            type: 'scroll',
            orient: 'vertical',
            right: 0
        },
        toolbox: {
            show: true,
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
                mark: { show: true },
                dataView: { show: true, readOnly: false },
                magicType: {
                    show: true,
                    type: ['pie', 'funnel']
                },
                restore: { show: true },
                saveAsImage: {
                    show: true ,
                    name: name_1
                }
            }
        },
        grid: {
            left: '3%',
            right: '20%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: [
            {
                type: 'category',
                data: ['龙田街道', '坪山街道', '碧岭街道', '坑梓街道', '马峦街道', '石井街道']
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
        ]

    }




    var deversion1
    $(function () {
        var series = []

        $.ajax({
            type: "get",
            async: true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
            url: "mychart1",    //请求发送到TestServlet处
            data: {},
            dataType: "json",        //返回数据形式为json
            success: function (result) {
                //请求成功时执行该函数内容，result即为服务器返回的json对象
                if (result) {
                    var version = result[0].version
                    for (var i = 1; i < result.length; i++) {
                        series.push({
                            name: result[i].name,
                            type: result[i].type,
                            stack: result[i].stack,
                            data: result[i].data
                        });

                    }
                    option.series = series
                    myChart1.hideLoading();
                    myChart1.clear();
                    myChart1.setOption(option, true);
                }
                deversion1 = version
            },
        })
    });


    setTimeout(
        setInterval(function () {
            var series = []
            $.ajax({
                type: "get",
                async: true,            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
                url: "mychart1",    //请求发送到TestServlet处
                data: {},
                dataType: "json",        //返回数据形式为json
                success: function (result) {
                    //请求成功时执行该函数内容，result即为服务器返回的json对象
                    if (result) {
                        version = result[0].version

                        if (version != deversion1 || result[0].time_request == 1) {
                            deversion1 = version
                            for (var i = 1; i < result.length; i++) {
                                series.push({
                                    name: result[i].name,
                                    type: result[i].type,
                                    stack: result[i].stack,
                                    data: result[i].data
                                });

                            }
                            option.series = series
                            myChart1.hideLoading();
                            myChart1.clear();
                            myChart1.setOption(option, true);
                        }
                    }

                },
            })
        }, 60000), 60000);


});


