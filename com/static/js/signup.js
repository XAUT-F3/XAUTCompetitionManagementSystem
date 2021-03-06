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
                type[0].checked = true;   // 参赛队员0为真
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


layui.use('laydate', function () {
    let laydate = layui.laydate;
    //执行一个laydate实例
    laydate.render({
        elem: '#student-date', //指定元素
        // elem: '#date', //指定元素
    });
    laydate.render({
        elem: '#date', //指定元素
    });
});


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




