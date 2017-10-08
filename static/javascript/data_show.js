/**
 * Created by yys-tt on 2017/9/3.
 */
var group_transform = {
    1 : "大一",
    2 : "大二",
    3 : "大三",
    4 : "大四"
};

$(document).ready(function(){
    //登录验证
    login_check();
    // 渲染数据
    data_show();
});

//登录验证
function login_check() {
    if ($.cookie('login_status') && $.cookie('login_status') == "on" ) {
        //登录成功
        return;
    } else {
        // 没有登录
        alert("你还没有登录呢，亲");
        window.location.href = "/login";
    }
}

//渲染数据
function data_show() {
    // 从cookie拿数据
    var username = $.cookie('username');
    var password = $.cookie('password');
    var obj = {
        email : username,
        password : password
    };
    //AJAX
    $.ajax({
        type:"post",
        url: "https://www.jnugeek.cn/api/checkApply ",
        data: obj,
        dataTpye: "json",
        success: function(result,status,xhr) {
            result = JSON.stringify(result);
            var data = result;
            if (!data) {
                return;
            }
            data = JSON.parse(data);
            // var data = [
            //     {
            //         created_at: "2017-09-01 14:13:43",
            //         major : "cst",
            //         introduction : "略",
            //         grade : "1",
            //         name : "patrick",
            //         phone : "18674020841",
            //         email : "chengtiyanyang@qq.com",
            //         department : "technology",
            //         student : "2015051654"
            //     },
            //     {
            //         created_at: "2017-09-01 14:13:43",
            //         major : "cst",
            //         introduction : "略",
            //         grade : "1",
            //         name : "aada",
            //         phone : "18674020841",
            //         email : "chengtiyanyang@qq.com",
            //         department : "technology",
            //         student : "2015051654"
            //     }
            // ];
            // 遍历数据
            var all_html = "";
            for (var i=0;i<data.length;i++) {
                var html = "";
                html += "<td>" + data[i]["name"] +  "</td>";
                html += "<td>" + data[i]["email"] +  "</td>";
                html += "<td>" + data[i]["phone"] +  "</td>";
                html += "<td>" + data[i]["student_id"] +  "</td>";
                html += "<td>" + group_transform[data[i]["grade"]] +  "</td>";
                html += "<td>" + data[i]["department"] +  "</td>";
                html += "<td>" + data[i]["major"] +  "</td>";
                html += "<td>" + data[i]["created_at"] +  "</td>";
                html += "<td>" + data[i]["introduction"] +  "</td>";
                html = "<tr>" + html + "<tr/>";
                all_html += html;
            }
            // 渲染
            $("table tbody").html(all_html);
        }
    });
}