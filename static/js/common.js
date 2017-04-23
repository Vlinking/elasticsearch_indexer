$(document).ready(function() {
   $('#search_button').click(function() {
       $.get('/search/query/'+ $('#search_query').val() + '/', {}, function(data) {
           $('#search_result').html(data);
       });
    });
});