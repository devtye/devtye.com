function myFunction(){
	
	var detail_child = document.getElementsByClassName('wrapper')[0].children;
	var delay = 0;
	
	for (var i = 0, len = detail_child.length; i < len ; i++) {

		detail_child[i].style.transitionDelay = delay + "s";
		detail_child[i].style.opacity = "1";
		console.log(delay);
		delay += 0.20;
	};
	
}

document.addEventListener('DOMContentLoaded', myFunction, false);