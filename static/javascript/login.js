/**
 * Created by yys-tt on 2017/9/1.
 */
$(document).ready(function(){
    //remove按钮事件
    remove_alert();
    //登录事件
    login();
});

//remove按钮事件
function remove_alert() {
    $("span.remove").click(function(){
        $("#alert").hide();
    })
}

//模态框通用函数
function alert_something(title,str) {
    if (typeof str == typeof "a") {
        $("#alert .message").text(str);
        $("#alert .title").text(title);
        $("#alert").show();
    }
}

//登录事件
function login() {
    $("#container input[type='submit']").click(function(e){
        // 取消默认行为
        e.preventDefault();
        // 禁用按钮
        $(this).attr("disabled",true);
        //获取数据
        var username = $("#container input[name='username']").val().trim().replace(/["'“”]/g,"");
        var password = $("#container input[name='password']").val().trim().replace(/["'“”]/g,"");
        // 表单验证
        if (!username || !password) {
            alert_something("输入错误","username和password不能为空");
            $(this).attr("disabled",false);
            return;
        }
        //数据整理
        var obj = {
            email : username,
            password : password
        };
        // ajax提交
        $.ajax({
            type:"post",
            url: "https://www.jnugeek.cn/api/checkApply ",
            data: obj,
            dataTpye: "json",
            success: function(result,status,xhr) {
                $.cookie('username',username,{path: '/'});
                $.cookie('password',password,{path: '/'});
                $.cookie('login_status',"on",{path: '/'});
                // 页面跳转
                window.location.href = "/data_show";
            },
            error: function(xhr,status,error) {
                if (error == "INTERNAL SERVER ERROR") {
                    alert_something("登录失败","用户名或密码不正确");
                    $("#container input[type='submit']").attr("disabled",false);
                    return;
                } else {
                    alert_something("登录失败","请检查你的网络。");
                    $("#container input[type='submit']").attr("disabled",false);
                    return;
                }
            }
        });
    })
}