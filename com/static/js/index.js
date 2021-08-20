// 轮播图播放时间
let x = $('.carousel').carousel({
    interval: 2500
})

// 限制显示字数
let title = document.querySelectorAll('.title span')
for (let i = 0; i < title.length; i++) {
    if (title[i].innerHTML.length > 50) {
        title[i].innerHTML = title[i].innerHTML.slice(0, 45) + '...';
    }
}
let font = document.querySelectorAll('.font span')
for (let i = 0; i < font.length; i++) {
    if (font[i].innerHTML.length > 50) {
        font[i].innerHTML = font[i].innerHTML.slice(0, 100) + '...';
    }
}

// 改变聚焦颜色
let hover = document.querySelectorAll('.comp-son');
let mort = document.querySelectorAll('.title');
for (let i = 0; i < hover.length; i++) {
    hover[i].onmouseover = function () {
        mort[i].style.color = '#4C96FF';
        font[i].style.color = '#999999';
    }
    hover[i].onmouseout = function () {
        mort[i].style.color = '#0F0F0F';
        font[i].style.color = '#6e6e6e';
    }
}

// 弹出框的js
$(function () {
    $('#layer-login').on('click', function () {
        layer.open({
            type: 2,
            title: '用户登录',
            // maxmin: true,
            skin: 'layui-layer-lan',
            shadeClose: true, //点击遮罩关闭层
            area: ['440px', '300px'],
            content: 'login.html'  //弹框显示的url
        });
    });
})



