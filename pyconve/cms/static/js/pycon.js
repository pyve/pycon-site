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


var PYCON = {
    init: function () {
        $('[rel=popover]').popover()

        var _countError = function(){
            var cantErrors = 0;
            var cantDivError = $("#register").find('.alert-error:visible').length;
            if ($('#id_first_name').val().length < 1) cantErrors ++;
            if ($('#id_last_name').val().length < 1) cantErrors ++;
            if ($('#id_email').val().length < 1) cantErrors ++;
            if ($('#id_password').val().length < 1) cantErrors ++;
            if ($('#id_confirm_password').val().length < 1) cantErrors ++;
            if ($('#id_country option:selected').val() == "" ) cantErrors ++;
            if (cantErrors > 0 || cantDivError > 0) {
                $('.form-actions > button').addClass('disabled');
                $('.form-actions > button').attr('disabled','disabled');
            }
            else {
                $('.form-actions > button').removeClass('disabled');
                $('.form-actions > button').removeAttr('disabled');
            }
            console.log(cantErrors);
        }
        var _checkComboBox = function(idComboBox){
            $(idComboBox).on("change", (function(){
                var idComboBoxSelected = idComboBox + " option:selected";
                if ($(idComboBoxSelected).val() == "") {
                    $(idComboBoxSelected).parent().parent().parent().find('.message').hide();
                    $(idComboBoxSelected).parent().parent().parent().find('.message').html('<p class="alert alert-error"> Campo obligatorio </p>');
                    $(idComboBoxSelected).parent().parent().parent().find('.message').show();
                }
                else {
                    $(idComboBoxSelected).parent().parent().parent().find('.message').hide();
                }
                _countError();
                
            }));
            $(idComboBox).on("change", (function(){
                var idComboBoxSelected = idComboBox + " option:selected";
                if ($(idComboBoxSelected).val() == "19") {
                    $('#register > div:eq(6)').css("display", "block");
                }
                else {
                    $('#register > div:eq(6)').css("display", "none");
                }
            }));
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
        var _checkInputTextEqual = function(idInputText1, idInputText2){
            $(idInputText2).delayKeyup(function () {
                if ($(idInputText1).val().length > 0) {
                    if ($(idInputText2).val() != $(idInputText1).val()) {
                        //$(idInputText2).parent().parent().parent().find('.message').hide();
                        if ($(idInputText2).parent().parent().parent().find('.message').is (':visible')) { var o =0; }
                        else {
                            $(idInputText2).parent().parent().parent().find('.message').html('<p class="alert alert-error">Las contraseñas no coinciden</p>');
                            $(idInputText2).parent().parent().parent().find('.message').show();
                        }
                    }
                    else {
                        $(idInputText2).parent().parent().parent().find('.message').hide();
                        $(idInputText1).parent().parent().parent().find('.message').hide();
                    }
                    _countError();
                }
            },400);
            $(idInputText1).on("keyup", (function(){
                if ($(idInputText2).val().length > 0) {
                    if ($(idInputText2).val() != $(idInputText1).val()) {
                        if ($(idInputText2).parent().parent().parent().find('.message').is (':visible')) { var o =0; }
                        else {
                            $(idInputText2).parent().parent().parent().find('.message').html('<p class="alert alert-error">Las contraseñas no coinciden</p>');
                            $(idInputText2).parent().parent().parent().find('.message').show();
                        }
                    }
                    else {
                        $(idInputText2).parent().parent().parent().find('.message').hide();
                        $(idInputText1).parent().parent().parent().find('.message').hide();
                    }
                }
            }));
        }
        var idInputTextsAttenders = [
            "#id_first_name",
            "#id_last_name",
            "#id_email",
            "#id_password",
            "#id_confirm_password"
            ];
        for (var i = 0; i < idInputTextsAttenders.length ; i++) {
            _checkInputText(idInputTextsAttenders[i]);
        };
        
        _checkInputTextEqual('#id_password', '#id_confirm_password');
        _checkComboBox('#id_country');

        $('#register > div:eq(6)').hide();
        $('.form-actions > button').addClass('disabled');
        $('.form-actions > button').attr('disabled','disabled');

        $('header ul a').bind('click',function(event){
            var $anchor = $(this);
     
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top
            }, 500,'easeInOutExpo');
            event.preventDefault();
        });
        
        $("#form").keypress(function(e) {
            if (e.which == 13) {
            return false;
            }
        });

        $('#ra').roundabout({
            autoplay: true,
            autoplayDuration: 5000,
            autoplayPauseOnHover: true,
            enableDrag: true
        });

        $('#slider').s3Slider({
            timeOut: 5000
        });
    }
}

$(document).ready(function () {PYCON.init();});
