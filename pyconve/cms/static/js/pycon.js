var PYCON = {
    init: function () {
        //console.log("hello world!")
        //
        $('[rel=popover]').popover()
        
        $(".show-form-speakers").click(function() {
        	$(".form-attendees").fadeOut(200, function(){
        		$(".form-speakers").fadeIn(500);
        	});
			
        	//$(".form-attendees").animate({ height: "hide"}, 1000, "swing");
			//$(".form-speakers").animate({ height: "show"}, 1000, "swing");
			$("#f-speakers").addClass("active");
			$("#f-attendees").removeClass("active");
		});

		$(".show-form-attendees").click(function() {
			$(".form-speakers").fadeOut(200, function(){
				$(".form-attendees").fadeIn(500);
			});
        	//$(".form-speakers").animate({ height: "hide"}, 1000, "swing");
			//$(".form-attendees").animate({ height: "show"}, 1000, "swing");
			$("#f-speakers").removeClass("active");
			$("#f-attendees").addClass("active");
		});

        

        var _checkInputText = function (idInputText){
            $(idInputText).on("blur", (function(){
                if ($(idInputText).val() == "") {
                    $(idInputText).parent().parent().parent().find('.span5').hide();
                    $(idInputText).parent().parent().after('<div class="span5 alert alert-error"> Este campo es obligatorio </div>');
                }
                if ((idInputText) == '#id_email'){
                    if ($(idInputText).val().indexOf('@', 0) == -1 || $(idInputText).val().indexOf('.', 0) == -1) {
                        $(idInputText).parent().parent().parent().find('.span5').hide();
                        $(idInputText).parent().parent().after('<div class="span5 alert alert-error"> Este campo debe corresponder a un correo electrónico </div>');
                    }
                }
            }));
            $(idInputText).on("keydown", (function(){
                if ($(idInputText).val().length > 0) {
                   $(idInputText).parent().parent().parent().find('.span5').hide();
                }
            }));

            
        }

        var _checkInputTextEqual = function(idInputText1, idInputText2){

            $(idInputText2).on("blur", (function(){
                if ($(idInputText2).val() != $(idInputText1).val()) {
                    //$(idInputText2).parent().parent().parent().find('.span5').hide();
                    $(idInputText2).parent().parent().after('<div class="span5 alert alert-error">Las contraseñas no coinciden</div>');
                }
            }));
            $(idInputText2).on("keydown", (function(){
                $(idInputText2).bind("blur");
                if ($(idInputText2).val().length > 0) {
                    $(idInputText2).parent().parent().parent().find('.span5').hide();

                }
            }));
        }
        
        var idInputTexts = ["#id_first_name","#id_last_name","#id_email","#id_password","#id_confirm_password"];
        
        for (var i = 0; i < idInputTexts.length ; i++) {
            _checkInputText(idInputTexts[i]);
        };
        
        _checkInputTextEqual('#id_password', '#id_confirm_password');

        
    }
}

$(document).ready(function () {

    //$(".form-horizontal .control-group").addClass('span6');

 //    $('#id_first_name').on("blur", (function(){
 //        if ($('#id_first_name').val() == "") {
 //            $('#id_first_name').parent().parent().after('<div class="span5 alert alert-error"> Debes ingresar tu nombre </div>');
 //            $('#id_first_name').unbind("blur");
 //            //return false;
 //        }
 //    }))

	// $(".form-actions").find('.btn').on("click",(function () {
 //        var nombre = $('#id_first_name').value;
 //        alert(nombre);
 //        if ($('#id_first_name').value == "") {
 //            $('#id_first_name').after('<p>Debes ingresar tu nombre</p>');
 //        }
            // $.ajax({
            //     type: "GET",
            //     url:"vef.php",
            //     data:"nick="+document.nickval.nick.value,
            //     success:function(msg){
            //         $("#final").html(msg);
            //     }
            // })
    // }));

   	PYCON.init();
});