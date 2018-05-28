var canvas = juego.getElementById('mapa1');
var context = canvas.getContext('2d');

make_base();

function make_base():
{
	base_image = new Image();
	base_image.src = 'map1';
	base_image.onload = function(){
		context.drawImage(base_image, 0, 0)
	}
}