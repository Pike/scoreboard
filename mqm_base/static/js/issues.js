/* global scorecard */
$("#entitylist .entity").click(function () {
    switchToEntity(this);
});

function switchToEntity(listitem) {
    $("#entitylist .hovered").removeClass('hovered');
    $(listitem).addClass('hovered');
    $("#original").text(listitem.dataset.original);
    rows($("#before").text(listitem.dataset.before));
    rows($("#after").text(listitem.dataset.after));
    if (scorecard) {
        scorecard.reset(listitem.dataset);
    }
}
function rows(textarea) {
    textarea = textarea[0];  // de-jQuery
    textarea.rows = 1;
    while (textarea.clientHeight < textarea.scrollHeight) {
        textarea.rows++;
    }
}

$(document).ready(function() {
    switchToEntity(document.querySelector("#entitylist .entity"));
});
