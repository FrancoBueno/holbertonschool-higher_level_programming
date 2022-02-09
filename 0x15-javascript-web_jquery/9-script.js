$(function () {
    $.get("https://fourtonfish.com/hellosalut/?lang=fr", function (json_get) { 
                $('#hello').text(json_get.hello)
});
    });