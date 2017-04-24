$(document).ready(function() {
   $('#search_button').click(function() {
       $.get('/search/'+ $('#search_query').val() + '/', {}, function(data) {
           $('#search_result').html(data);
       });
    });
});