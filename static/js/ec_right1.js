var ec_right1 = echarts.init(document.getElementById('r1'),"dark");
var ec_right1_option = {
	//标题样式
	title : {
	    text : "今日新增确诊病例前五城市",
	    textStyle : {
	        color : 'rgb(95,158,160)',
	    },
	    left : 'left'
	},
	  color: ['#3398DB'],
	    tooltip: {
	        trigger: 'axis',
	        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
	            type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
	        }
	    },
    xAxis: {
        type: 'category',
        data: [    ]
    },
    yAxis: {
        type: 'value',
		max : 10,
		splitNumber : 5,

    },
    series: [{
        data: [],
        type: 'bar',
		barMaxWidth:"50%",

    }]
};
ec_right1.setOption(ec_right1_option)