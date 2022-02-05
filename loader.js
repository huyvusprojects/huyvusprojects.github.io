
// Photo Count
var river = 3;
var tuoi_tuoi = 3;
var nam_dinh = 3;
var paradise = 3;


// If you want to add more labels just let me know
// It should take less than a day to get that operational

// DO NOT TOUCH BELOW OR I WILL FIND YOU... and probably give you fried chicken



// laced with poison, of course

var image_load_count = [nam_dinh, paradise, river, tuoi_tuoi];
var image_load_type = ["NamDinh", "Paradise", "ByTheRiver", "TuoiTuoi"];

var categories = 4;
var image_count;


for (var i = 0; i < categories; i++) {
  if (name == image_load_type[i]) {
    image_count = image_load_count[i];
    break;
  }
}


var current_image = 1; // 1.png

function load_next_image() {
  current_image += 1;
  if (current_image > image_count) {
    current_image = 1;
  }
  return "Photography/" + name + "/" + current_image.toString() + ".jpg";
}


function preload(image_array) {
  $(image_array).each(function(){
      (new Image()).src = this;
  });
}

function load_preload_array() {
  var load = [];
  for (var j = 1; j <= image_count; j++) {
    load.push("Photography/" + name + "/" + j.toString() + ".jpg");
  }
  console.log(load);
  return load
}

preload(load_preload_array());
/*
var image_preload_holder = [];

function preloadImage(counter)
{
  image_preload_holder.push(new Image().src = "Photography/" + name + "/" + counter.toString() + ".jpg");
}

for (var j = 1; j <= image_count; j++) {
  preloadImage(j);
}
*/


$('.ImageContainer').on("click", function (e) {
  e.preventDefault();
  $('.ImageContainer').fadeTo(200, 0.2);
  $('.ImageContainer').promise().done(function(){
  // will be called when all the animations on the queue finish
    $("#imageDisplay").attr("src", load_next_image());
    $('.ImageContainer').fadeTo(200, 1);
  });

});
