$('#xrm-search-name').keyup(function() {
    var input = $(this).val().toLowerCase();
    if (input) {
        $('.xrm-items tbody tr').each(function() {
            var check = $(this).find('.xrm-item-name').text().toLowerCase().indexOf(input) == -1;
            if (check) {
                $(this).hide();
            }
            else {
                $(this).show();
            }
        });
    }
    else {
        $('.xrm-items tbody tr').show();
    }
});

$('#xrm-search-number').keyup(function() {
    var input = $(this).val().toLowerCase();
    if (input) {
        $('.xrm-items tbody tr').each(function() {
            var check = $(this).find('.xrm-item-id').text().toLowerCase().indexOf(input) != 0;

            if (check) {
                $(this).hide();
            }
            else {
                $(this).show();
            }
        });
    }
    else {
        $('.xrm-items tbody tr').show();
    }
});