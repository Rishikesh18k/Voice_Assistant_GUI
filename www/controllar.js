$(document).ready(function () {
    //Display speak message...
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate('start');
    }
    eel.expose(ShowIndex)
    function ShowIndex(message) {
        $("#Oval").attr("hidden", true);
        $("#ClickBtn").attr("hidden", false);
        $("#name").attr("hidden",true);
    }
});
