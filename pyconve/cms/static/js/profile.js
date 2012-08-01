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


var PROFILE = {
    init: function () {
        var _this = this;

        $(document).on("click", "[data-action]", function () {
            var action = $(this).data().action;
            _this[action]($(this));
        });

        $("#id_duration").keydown(function(event){
            if( event.keyCode != 08 && event.keyCode != 127 ) { 
                if( event.keyCode < 48 || event.keyCode > 57 ){
                    return false;
                }
            }
        });

        var _countError = function(){
            var cantErrors = 0;
            var cantDivError = $(".container").find('.alert-error:visible').length;

            if ($('#id_name').val().length < 1) cantErrors ++;
            if ($('#id_description').val().length < 1) cantErrors ++;
            if ($('#id_duration').val().length < 1) cantErrors ++;
            if ($('#id_requirements').val().length < 1) cantErrors ++;

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
                    $(idInputText).parent().parent().parent().find('.message').hide();
                    $(idInputText).parent().parent().parent().find('.message').html('<p class="alert alert-error"> Campo obligatorio </p>');
                    $(idInputText).parent().parent().parent().find('.message').show();
                }
                if ((idInputText) == '#id_email'){
                    if ($(idInputText).val().indexOf('@', 0) == -1 || $(idInputText).val().indexOf('.', 0) == -1) {
                        $(idInputText).parent().parent().parent().find('.message').hide();
                        $(idInputText).parent().parent().parent().find('.message').html('<p class="alert alert-error"> No es un correo </p>');
                        $(idInputText).parent().parent().parent().find('.message').show();
                        
                    }
                }
                _countError();
            }));
            $(idInputText).on("keydown", (function(){
                if ($(idInputText).val().length > 0) {
                   $(idInputText).parent().parent().parent().find('.message').hide();
                }
            }));
        }     

        var idInputTextsSpeakers = [
            "#id_name",
            "#id_description",
            "#id_duration",
            "#id_requirements"
            ];

        for (var i = 0; i < idInputTextsSpeakers.length ; i++) {
            _checkInputText(idInputTextsSpeakers[i]);
        };
        
        $('.form-actions > button').addClass('disabled');
        $('.form-actions > button').attr('disabled','disabled');    
        
        $("#form").keypress(function(e) {
            if (e.which == 13) {
            return false;
            }
        });

        if ($('.alert-success').is (':visible')){
            setTimeout("$('.alert-success').fadeOut('fast');",1000) ;
        };
    },

    editPresentation: function (presentation){
        $('#formulario').load(presentation.data().url);
    },

    deletePresentation: function (presentation){
        presentation.parent().remove();
    }
}

$(document).ready(function () {PROFILE.init();});
