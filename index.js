function setSizes() {
   var container_width = $(".body").width();
   $(".Content").width(Math.max(container_width - 330, 400));

   var container_height = $(".body").height();
   $(".Content").height = (Math.max(container_height, 500));
   $(".Sidebar").height = (Math.max(container_height, 500));
}

$(window).resize(function() { setSizes(); });
