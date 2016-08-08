$(function(){
    $.ajax({
        url:'/scholar/get_spider_data',
        type:'GET',
        success:function(callback){
            var obj = jQuery.parseJSON(callback);
			if(!obj.status){
				console.log(obj.message);
				alert("请求失败!"+obj.message);
			}else{
				console.log(obj.data);
				$.each(obj.data.total_list,function(k,v){
				    //console.log(k);
				    //console.log(v[1]);
				    var t = v[0];
				    v[0] = new Date(v[1]);
				    v[1] = t;
				    //console.log(v[0]);
				});
				$.each(obj.data.delta_list,function(k,v){
				    //console.log(k);
				    //console.log(v[0]);
				    v[0] = new Date(v[0]);
				    //console.log(v[0]);
				});
                //console.log(obj.data.total_list)
                //console.log(obj.data.delta_list)
				total_data = obj.data.total_list
				delta_data = obj.data.delta_list
				draw_plot("文章数目总量曲线",total_data,'total_graph');
				draw_plot("文章每小时增量曲线",delta_data,'delta_graph',line_fill=true);
                //handle day data
				$.each(obj.data.day_list,function(k,v){
                    $("#date_tr").append('<th>'+v[0]+'</th>');
                    $("#delta_tr").append('<th>'+v[1]+'</th>');
                    $("#total_tr").append('<th>'+v[2]+'</th>');
				});
			}
        }
    })
});


function draw_plot(label,data,div_id,line_fill=null){
    var data_set = [
        {label: label,data: data}
    ];
    var options = {
            series: {
                lines: {
                    show: true,
                    fill: line_fill
                },
                points: {
                    radius: 1,
                    show: true,
                }
            },
            xaxis: {
               mode: "time",
               timeformat: "%m/%d %H:00"
            }
        };
    $.plot(
        $("#"+div_id),
        data_set,
        options
    );
}