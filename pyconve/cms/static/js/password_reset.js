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


var PWDRESET = {
    init: function () {

        var _countError = function(){

            var cantErrors = 0;
            var cantDivError = $("#pwdreset").find('.alert-error:visible').length;

            if ($('#id_new_password').val().length < 1) cantErrors ++;
            if ($('#id_new_password_confirm').val().length < 1) cantErrors ++;

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
            $(idInputText).on("blur", (function(){
                if ($(idInputText).val() == "") {
                    $(idInputText).parent().find('.help-inline').hide();
                    $(idInputText).parent().find('.help-inline').html('<div class="alert alert-error"> Campo obligatorio </div>');
                    $(idInputText).parent().find('.help-inline').show();
                }
                else {
                    $(idInputText).parent().find('.help-inline').hide(); 
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
            "#id_new_password",
            "#id_new_password_confirm"
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

$(document).ready(function () {PWDRESET.init();});
