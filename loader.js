console.log(name);

// Photo Count
var river = 3;
var tuoi_tuoi = 3;
var nam_dinh = 3;
var paradise = 3;


// If you want to add more labels just let me know
// It should take less than a day to get that operationa;

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


$('.ImageContainer').on("click", function (e) {
      e.preventDefault();
      $("#imageDisplay").attr("src", load_next_image());
 });
