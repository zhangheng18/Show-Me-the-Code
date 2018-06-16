$(document).ready(function () {
    // edit item
    $(".edit-btn").on('click', function () {
        var itemId = this.id;
        $("#item" + itemId).hide();
        $("#form" + itemId).show();
        $(".cancel-btn").click(function () {
            $("#form" + itemId).hide();
            $("#item" + itemId).show();
        });
    });

    //$('.items').sortable({ handle: '.move' });
    $('select').material_select();
    $(".button-collapse").sideNav();

    // add new item
    $("#new-item").click(function () {
        if ($("#item-input").val() == '') {
            Materialize.toast('你的todo是空的！', 4000)
        } else {
            Materialize.toast('todo添加成功！', 3000, 'rounded');
            document.getElementById('add-item-form').submit()
        }
    });



    $(".item-done").click(function () {
        $(this).parent().slideUp();
        Materialize.toast('Well Done +1', 3000, 'rounded')
    });


    $(".confirm-btn").click(function () {
        Materialize.toast('修改成功~', 3000, 'rounded')
    });

    $(".delete-item").click(function () {
        $(this).parent().slideUp();
        Materialize.toast('删除成功~', 3000, 'rounded')
    });



})








