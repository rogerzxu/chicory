$(document).ready(function(){
    //$(".game").addClass("highlight");
    var str = $(".game").text()
    $(".game").empty()
    var row = -1
    var column = 0
    for (var i = 0, len = str.length; i < len; i++) {
        if(str[i] == "0" || str[i] == "X"){
            var position = "<form action=\"../server.py\" method=\"POST\">" +
            "<button type=\"submit\" name=\"turn\" value=\""+ row.toString() + column.toString() + "\">" + str[i] + "</button>" +
            "</form>"
            $(".game").append(position)
            column+=1
        }
        else if(str[i] == "\n"){
            $(".game").append("<br />")
            row+=1
            column = 0
        }
    }
});