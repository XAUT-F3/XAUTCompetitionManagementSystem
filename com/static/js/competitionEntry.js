$('#selected').bind('click', function () {
    let temp = document.getElementById('competition-name');
    $.getJSON('race_message/', {'id': temp.value}, function (data) {
        // $.getJSON("{% URL 'applyMessages' %}", {'id': temp.value}, function (data) {
        let obj = document.getElementById('radio-data');
        obj.innerHTML = '';
        for (let i = 0; i < data.length; i++) {
            obj.innerHTML += '<div class="radio">\n' +
                '<label>\n' +
                '<input type="radio" name="T_message" value=' +
                data.messages[i].id + '>\n' +
                '<span>' +
                data.messages[i].m_name +
                '</span>' +
                '</label>\n' +
                '</div>';
        }
    })
})

$('#select-message').bind('click', function () {
    $('#competition-message').val($("input[name='T_message']:checked").next("span").text());
    $('#myModal').modal('hide');
})

let head = document.querySelectorAll('#mar li');
let body = document.querySelectorAll('.body');
let remove = (start, end) => {
    body[start].classList.remove('active');
    head[start].classList.remove('active');
    body[end].classList.add('active');
    head[end].classList.add('active');
}
$('#next-one').bind('click', function () {
    remove(0, 1);
})
$('#next-two').bind('click', function () {
    remove(1, 2);
})
$('#next-three').bind('click', function () {
    let data = {
        's_name': $('input[name=s_name]').val(),
        'birthday': $('input[name=s_birthday]').val(),
        'college': $('input[name=s_college]').val(),
        'grade': $('input[name=s_grade]').val(),
        's_class': $('input[name=s_class]').val(),
        'number': $('input[name=s_number]').val(),
        'mail': $('input[name=s_mail]').val(),
        's_phone': $('input[name=s_phone]').val(),
        'T_message': $('input[name=T_message]:checked').val(),
        'T_name': $('input[name=T_name]').val(),
        'T_slogan': $('input[name=T_slogan]')["0"].value,
        'T_intro': $('#introduce')["0"].value,
        'T_leader': $('input[name=s_name]').val(),
        'T_phone': $('input[name=s_phone]').val(),
        'T_remark': $('#remark')["0"].value
    };
    // 调用Ajax上传数据
    $.post('team/', data, (args) => {
        if (args.code === 1) {
            layer.msg('报名成功');
            remove(2, 3);
            document.getElementById('captain').setAttribute('value', $('#student-name').val());
        } else {
            layer.msg(args.msgs);
        }
    })
})
$('#invite-student').bind('click', () => {
    $('#submit-invite').bind('click', () => {
        let tel = $('#invite-tel').val();
        let name = $('#invite-name').val();
        if (tel.length === 0 || name.length === 0) {
            alert('信息不能为空！');
        } else if (1) {

        } else {
            $.getJSON('addMatchStudent/', {
                'phone': tel,
                'name': name,
                'message_id': $('input[name=T_message]').val()
            }, (data) => {
                layer.msg(data.msgs);
                if (data.code === 1) {
                    $('#invite-table').modal('hide');  // 关闭窗口
                    let len = $('#student-table tbody tr')  // 数行数
                    $('#student-table tbody').innerHTML += '<tr>\n' +
                        '<td>' + len + 1 + '</td>\n' +
                        '<td>' + name + '</td>\n' +
                        '<td>' + '待接受' + '</td>\n' +
                        '<td>' + '<a href="{% url \'qry\' 1 %}" class="delete-message">移除</a>' + '</td>\n' +
                        '</tr>'
                }
            })
        }
    })
})
$('.delete-message').bind('click', () => {

})



