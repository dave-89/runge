$(document).ready(function() {

    $('#reloadButton').click(function() {

        var functionDefault = '-x';
        var bDefault = '1.0';

        var x0Default = '1.0';
        var p0Default = '0.0';

        var t0Default = '0.0';
        var t1Default = '5.0';
        var dtDefault = '0.01';

        var func = $('#functionField').val();
        var x0 = $('#x0Field').val();
        var p0 = $('#p0Field').val();

        var t0 = $('#t0Field').val();
        var t1 = $('#t1Field').val();
        var dt = $('#dtField').val();

        if (func == '') {
            $('#functionField').val(functionDefault);
            func = functionDefault;
        }

        if (x0 == '') {
            $('#x0Field').val(x0Default);
            x0 = x0Default;
        }

        if (p0 == '') {
            $('#p0Field').val(p0Default);
            p0 = p0Default;
        }

        if (t0 == '') {
            $('#t0Field').val(t0Default);
            t0 = t0Default;
        }

        if (t1 == '') {
            $('#t1Field').val(t1Default);
            t1 = t1Default;
        }

        if (dt == '') {
            $('#dtField').val(dtDefault);
            dt = dtDefault;	
        }

	if((parseFloat(t1)-parseFloat(t0))/parseFloat(dt)>5000) {
		dt = (t1-t0)/5000.0;
		$('#dtField').val(dt);			
	}



        var params = {
            functionVal: func,
            x0Val: x0,
            p0Val: p0,
            t0Val: t0,
            t1Val: t1,
            dtVal: dt
        };

        params = JSON.stringify(params);



        var req = $.ajax({
            url: '/plot',
            type: 'POST',
            contentType: 'application/json',
            data: params,
            success: function(result) {
                $('.image').html('<img src="data:image/png;base64,' + result + '" />');
            },
            error: function(xhr, ajaxOptions, thrownError) {
                console.log(xhr.status);
                console.log(thrownError);
            }
        });
    });
});
