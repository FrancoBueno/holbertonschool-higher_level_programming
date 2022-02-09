$.get("https://swapi-api.hbtn.io/api/people/5/?", function (json_get) { 
    $('DIV#character').text(json_get.name);
});