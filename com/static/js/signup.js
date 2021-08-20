let green = document.querySelectorAll('.brod-green');
let greenFont = document.querySelectorAll('.font-green');
let student = document.getElementById('student');
let greenIcon = document.getElementById('green-icon')
student.onmouseover = function () {
    for (let i = 0; i < green.length; i++) {
        green[i].style.backgroundColor = '#5CB85C';
    }
    for (let i = 0; i < greenFont.length; i++) {
        green[i].style.color = '#ffffff';
        greenIcon.style.color = '#ffffff'
    }
}
student.onmouseout = function () {
    for (let i = 0; i < green.length; i++) {
        green[i].style.backgroundColor = '#f2fffa';
    }
    for (let i = 0; i < greenFont.length; i++) {
        green[i].style.color = '#5CB85C';
        greenIcon.style.color = '#5CB85C'
    }
}
let blue = document.querySelectorAll('.brod-blue');
let blueFont = document.querySelectorAll('.font-blue');
let teacher = document.getElementById('teacher');
let blueIcon = document.getElementById('blue-icon')
teacher.onmouseover = function () {
    for (let i = 0; i < blue.length; i++) {
        blue[i].style.backgroundColor = '#337AB7';
    }
    for (let i = 0; i < blueFont.length; i++) {
        blue[i].style.color = '#ffffff';
        blueIcon.style.color = '#ffffff'
    }
}
teacher.onmouseout = function () {
    for (let i = 0; i < blue.length; i++) {
        blue[i].style.backgroundColor = '#F1FBFF';
    }
    for (let i = 0; i < blueFont.length; i++) {
        blue[i].style.color = '#337AB7';
        blueIcon.style.color = '#337AB7'
    }
}
let type = document.getElementsByName('type');
// let phone = 0;
let head = document.querySelectorAll('.all-head');
let body = document.querySelectorAll('.tab-pane');
$(function () {
    $('#student').click(
        function () {
            layer.confirm('&nbsp&nbsp&nbsp&nbsp您选择的身份为【参赛队员】，注册成功后，身' +
                '份<br>将无法更改，是否继续？', {
                btn: ['确认', '取消'] //按钮
            }, function () {
                layer.msg('选择成功！', {icon: 1});
                body[0].classList.remove('active');
                body[1].classList.add('active');
                head[1].classList.add('active');
                head[0].classList.remove('active');
                type[0].checked = true;
                type[1].checked = false;
            }, function () {
                layer.msg('请重新选择', {icon: 2});
            });
        }
    )
})
$(function () {
    $('#teacher').click(
        function () {
            layer.confirm('&nbsp&nbsp&nbsp&nbsp您选择的身份为【指导教师】，注册成功后，身' +
                '份<br>将无法更改，是否继续？', {
                btn: ['确认', '取消'] //按钮
            }, function () {
                layer.msg('选择成功！', {icon: 1});
                body[0].classList.remove('active');
                body[2].classList.add('active');
                head[1].classList.add('active');
                head[0].classList.remove('active');
                type[0].checked = false;
                type[1].checked = true;
            }, function () {
                layer.msg('请重新选择', {icon: 2});
            });
        }
    )
})


$('#student-date,#date').datetimepicker({
    forceParse: 0,//设置为0，时间不会跳转1899，会显示当前时间。
    language: 'zh-CN',//显示中文
    format: 'yyyy-mm-dd',//显示格式
    minView: "day",//设置只显示到月份
    initialDate: new Date(),//初始化当前日期
    autoclose: true,//选中自动关闭
    startView: 3,
})


$('input[name=picture], input[name=s_picture]').change(function () {
    let file = this.files[0]
    if (!/image\/\w+/.test(file.type)) {
        return 0;
    }
    let reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function (e) {
        $('.reading').attr('src', this.result)
    }
})

$("#submit").bind('click', function () {
    let password = $("#password");
    let password_again = $("#passwordagain");
    if (password.val().length < 8 || password.val().length > 16) {
        layer.alert('请输入8-16位数字,字母,字符的组合', {
            icon: 2,
            skin: 'layer-ext-demo' //见：扩展说明
        })
        return 0;
    } else {
        if (password.val() !== password_again.val()) {
            layer.alert('请两次输入一样的密码!', {
                icon: 2,
                skin: 'layer-ext-demo' //见：扩展说明
            })
            return 0;
        }
    }
})
let PHONE = 0
$("#stu-btn").bind('click', function () {
    let sex_obj = document.getElementsByName('s_sex');
    if (sex_obj[0].checked !== true && sex_obj[1].checked !== true) {
        layer.alert('选择性别!', {
            icon: 2,
            skin: 'layer-ext-demo'
        })
        return;
    }
    let element = document.querySelectorAll('.stu .form-group input');
    for (let i = 0; i < element.length; i++) {
        if (element[7].value === '') {
            layer.alert('请上传照片', {
                icon: 2,
                skin: 'layer-ext-demo'
            })
            return;
        }
        if (element[i].value === '') {
            layer.alert('请填写完整信息!', {
                icon: 2,
                skin: 'layer-ext-demo'
            })
            return;
        }
    }
    body[1].classList.remove('active');
    body[3].classList.add('active');
    head[2].classList.add('active');
    head[1].classList.remove('active');
    $("#username").val(element[6].value);
})
let FLAG = 0;  // 学生注册标记 如果是学生则进入学生信息界面
$('#tea-btn').bind('click', function () {
    let sex_tea = document.getElementsByName('t_sex');
    if (sex_tea[0].checked !== true && sex_tea[1].checked !== true) {
        layer.alert('选择性别!', {
            icon: 2,
            skin: 'layer-ext-demo'
        })
        return;
    }
    let teacher_data = document.querySelectorAll('.tea .form-group input');
    for (let i = 0; i < teacher_data.length; i++) {
        if (teacher_data[7].value === '') {
            layer.alert('请上传照片', {
                icon: 2,
                skin: 'layer-ext-demo'
            })
            return;
        }
        if (teacher_data[i].value === '') {
            layer.alert('请填写完整信息!', {
                icon: 2,
                skin: 'layer-ext-demo'
            })
            return;
        }
    }
    body[2].classList.remove('active');
    body[3].classList.add('active');
    head[2].classList.add('active');
    head[1].classList.remove('active');
    FLAG = 1;
    $("#username").val(teacher_data[6].value);
})

$('.fir').bind('click', function () {
    body[2].classList.remove('active');
    body[1].classList.remove('active');
    body[0].classList.add('active');
    head[1].classList.remove('active');
    head[0].classList.add('active');
})
$('.sec').bind('click', function () {
    head[2].classList.remove('active');
    head[1].classList.add('active');
    body[3].classList.remove('active');
    if (FLAG === 0) {
        body[1].classList.add('active');
    } else {
        body[2].classList.add('active');
    }
})
// 取消第三个a标签的使用
document.getElementById("must1").href = "javascript:void(0)";
document.getElementById("must2").href = "javascript:void(0)";


