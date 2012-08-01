(function ($) {
    $.fn.delayKeyup = function(callback, ms){
        var timer = 0;
        $(this).keyup(function(){                   
            clearTimeout (timer);
            timer = setTimeout(callback, ms);
        });
        return $(this);
    };
})(jQuery);


var LOGIN = {
    init: function () {

        var _countError = function(){

            var cantErrors = 0;
            var cantDivError = $("#register").find('.alert-error:visible').length;

            if ($('#id_username').val().length < 1) cantErrors ++;
            if ($('#id_password').val().length < 1) cantErrors ++;

            if (cantErrors > 0 || cantDivError > 0) {
                $('.form-actions > button').addClass('disabled');
                $('.form-actions > button').attr('disabled','disabled');
            }
            else {
                $('.form-actions > button').removeClass('disabled');
                $('.form-actions > button').removeAttr('disabled');
            }            
        }

        var _checkInputText = function (idInputText){
            $(idInputText).on("keyup", (function(){
                if ($(idInputText).val() == "") {
                    $(idInputText).parent().find('.help-inline').hide();
                    $(idInputText).parent().find('.help-inline').html('<div class="alert alert-error"> Campo obligatorio </div>');
                    $(idInputText).parent().find('.help-inline').show();
                }
                if ((idInputText) == '#id_email'){
                    if ($(idInputText).val().indexOf('@', 0) == -1 || $(idInputText).val().indexOf('.', 0) == -1) {
                        $(idInputText).parent().find('.help-inline').hide();
                        $(idInputText).parent().find('.help-inline').html('<div class="alert alert-error"> Este campo debe corresponder a un correo electrónico </div>');
                        $(idInputText).parent().find('.help-inline').show();
                    }
                }
                _countError();
            }));
            $(idInputText).on("keydown", (function(){
                if ($(idInputText).val().length > 0) {
                   $(idInputText).parent().find('.help-inline').hide();
                }
                _countError();
            }));
            
        }

        var idInputTextsAttenders = [
            "#id_username",
            "#id_password"
            ];

        for (var i = 0; i < idInputTextsAttenders.length ; i++) {
            _checkInputText(idInputTextsAttenders[i]);
        };
        
        $('.form-actions > button').addClass('disabled');
        $('.form-actions > button').attr('disabled','disabled');

        $("#form").keypress(function(e) {
            if (e.which == 13) {
            return false;
            }
        });
    }
}

$(document).ready(function () {LOGIN.init();});
