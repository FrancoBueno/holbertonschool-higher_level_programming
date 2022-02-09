$(function () {
    $.get("https://swapi-api.hbtn.io/api/films/?format=json", function (json_get, textStatus) { 
        if (textStatus == 'success') {
            let movies = json_get.results;
            for (let x in movies) {
                $('#list_movies').append('<li>' + movies[x].title + '</li>');
        }
    }})
});