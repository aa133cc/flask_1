var ec_right2 = echarts.init(document.getElementById('r2'), "dark");


// var mydata = [{'name': '上海', 'value': 318}, {'name': '云南', 'value': 162}]

var ec_right2_option = {
    title: {
        text: '今日新增确诊病例城市汇总',
        textStyle : {
	        color : 'rgb(95,158,160)',
	    },
        subtext: '',
        x: 'left'
    },
    tooltip: {
        trigger: 'item'
    },
    legend: {
        top: '15%',
        left: 'center'
    },
    //配置属性
    series: [
        {
            top:'30%',
            name: '城市疫情信息',
            type: 'pie',
            radius: ['40%', '80%'],
            avoidLabelOverlap: false,
            label: {
                show: false,
                position: 'center'
            },
            emphasis: {
                label: {
                    show: true,
                    fontSize: '20',
                    fontWeight: 'bold'
                }
            },
            labelLine: {
                show: false
            },
            data: []
        }
    ]


};
ec_right2.setOption(ec_right2_option)