function myFunction(){
	
	var thumbnails = document.getElementsByClassName('thumbnails');
	var delay = 0;

	for (var i = 0, len = thumbnails.length; i < len ; i++) {

		thumbnails[i].style.transitionDelay = delay + "s";
		thumbnails[i].style.opacity = "1";
		console.log(delay);
		delay += 0.30;
	};
	
}


document.addEventListener('DOMContentLoaded', myFunction);


