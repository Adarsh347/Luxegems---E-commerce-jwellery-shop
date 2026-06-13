$(document).ready( function () {
    $('.increment-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value < 10) {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.decrement-btn').click(function (e) {
        e.preventDefault();

        var inc_value = $(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value, 10);
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });

    $('.addtowishlist').click(function (e) {
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': product_id,
                'csrfmiddlewaretoken': token
            },
            success: function(response) {
                console.log(response);
                if (window.alertify) {
                    alertify.success(response.status);
                } else {
                    alert(response.status);
                }
            }
        });
    });

    $('.AddToCartBtn').click(function (e) {
        e.preventDefault();

        var product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'product_id': product_id,
                'product_qty': product_qty,
                'csrfmiddlewaretoken': token
            },
            success: function(response) {
                console.log(response);
                if (window.alertify) {
                    alertify.success(response.status);
                } else {
                    alert(response.status);
                }
            }
        });
    });

    // CART PAGE: qty +/- buttons in cart rows
    $('.qty-btn').click(function(e){
        e.preventDefault();
        var $row = $(this).closest('tr');
        var $input = $row.find('.qty-input');
        var val = parseInt($input.val(),10) || 1;
        var txt = $(this).text().trim();
        if(txt === '+') val++;
        else if(txt === '-') val = Math.max(1, val-1);
        $input.val(val);
    });

    // Delete cart item
    $(document).on('click', '.icon', function(e){
        var $td = $(this);
        var $row = $td.closest('tr');
        var cart_id = $row.data('id');
        if(!cart_id) return;
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: 'POST',
            url: '/delete-cart-item',
            data: {'cart_id': cart_id, 'csrfmiddlewaretoken': token},
            success: function(response){
                if(window.alertify){ alertify.success(response.status); }
                else { alert(response.status); }
                if(response.status){ location.reload(); }
            }
        });
    });

    // Update cart quantities
    $('.update').click(function(e){
        e.preventDefault();
        var cart_ids = [];
        var qtys = [];
        $('table tr.items').each(function(){
            var cid = $(this).data('id');
            if(!cid) return;
            var q = $(this).find('.qty-input').val() || 1;
            cart_ids.push(cid);
            qtys.push(q);
        });
        if(cart_ids.length === 0) return;
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: 'POST',
            url: '/update-cart',
            traditional: true,
            data: {'cart_id[]': cart_ids, 'qty[]': qtys, 'csrfmiddlewaretoken': token},
            success: function(response){
                if(window.alertify){ alertify.success(response.status); }
                else { alert(response.status); }
                if(response.status){ location.reload(); }
            }
        });
    });
});

$(document).on('click', '.delete-wishlist-item', function () {

    var wishlist_id = $(this).data('wishlist-id');
    var token = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        method: "POST",
        url: "/delete-wishlist-item",
        data: {
            wishlist_id: wishlist_id,
            csrfmiddlewaretoken: token
        },
        success: function (response) {
            location.reload();
        }
    });
});



