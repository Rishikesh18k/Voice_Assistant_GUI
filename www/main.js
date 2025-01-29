// siri wave...
$(document).ready(function () {
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 670,
        height: 180,
        style: "ios9",
        amplitude: "1",
        speed: "0.17",
        autostart: true
    });

    // siri message animation...
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect:  "fadeInUp",
            sync: true,
        },
        out: {
            effect:  "fadeOutUp",
            sync: true
        },
    });
    $("#micbtn").click(function () { 
        $("#Oval").attr("hidden", false);
        $("#ClickBtn").attr("hidden", true);
        $("#name").attr("hidden", false);
        // eel.takeCommand()()
        eel.AllCommand()()
    });
});