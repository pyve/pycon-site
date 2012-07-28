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
    }
}

$(document).on("ready", function () {
	$(".btn-register-attenders").on("click",(function () {
    	alert("hola");
    	return false;
    }));

   	PYCON.init();
});