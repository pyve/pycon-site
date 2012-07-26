var PYCON = {
    init: function () {
        console.log("hello world!")

        $(".show-form-speakers").click(function() {
        	$(".form-attendees").fadeOut(500, function(){
        		$(".form-speakers").fadeIn(1000);
        	});
			
        	//$(".form-attendees").animate({ height: "hide"}, 1000, "swing");
			//$(".form-speakers").animate({ height: "show"}, 1000, "swing");
			$("#f-speakers").addClass("active");
			$("#f-attendees").removeClass("active");
		});

		$(".show-form-attendees").click(function() {
			$(".form-speakers").fadeOut(500, function(){
				$(".form-attendees").fadeIn(1000);
			});
        	//$(".form-speakers").animate({ height: "hide"}, 1000, "swing");
			//$(".form-attendees").animate({ height: "show"}, 1000, "swing");
			$("#f-speakers").removeClass("active");
			$("#f-attendees").addClass("active");
		});
    }
}

$(document).on("ready", function () {
   PYCON.init();
});