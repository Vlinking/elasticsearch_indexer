$(document).ready(function() {
   $('#search_button').click(function(e) {
       e.preventDefault();
       var data = $('#search_form').serialize();
       $.post('/search/query/', data, function(result) {
           $('#search_result').html(result);
       });
    });
});