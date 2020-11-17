// client-side js
// run by the browser each time your view template is loaded

// by default, you've got jQuery,
// add other scripts at the bottom of index.html

$(function() {
  console.log("hello world :o");

  $.get("/stats", function(playlist) {
        $("ul#dreams").empty();
    playlist.forEach(function(stuff) {
      $("<li></li>")
        .text(stuff)
        .appendTo("ul#dreams");
    });
  });

  $("form").submit(function(event) {
    event.preventDefault();
    console.log("form submitted");
    var playlistUri = document.getElementById('playlist').value
    console.log(playlistUri);
    $.post('/stats?' + $.param({'playlist': playlistUri}), function() {
      // $("<li></li>")
      //   .text(playlistUri)
      //   .appendTo("ul#dreams");
      // console.log($("<li></li>").text(playlistUri));
      // $("input").val("");
      // $("input").focus();
      $.get("/stats", function(playlist) {
        $("ul#dreams").empty();
    playlist.forEach(function(stuff) {
      $("<li></li>")
        .text(stuff)
        .appendTo("ul#dreams");
    });
  });
    });
  });
});
