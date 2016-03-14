/* global scorecard */
$(".items .entity").click(function () {
    switchToEntity(this);
});

function switchToEntity(listitem) {
    $(".items .hovered").removeClass('hovered');
    $(listitem).addClass('hovered');
    $("#original").text(listitem.dataset.original);
    rows($("#before").text(listitem.dataset.before));
    rows($("#after").text(listitem.dataset.after));
    if (scorecard) {
        scorecard.reset(listitem.dataset);
    }
}
function rows(textarea) {
}

$(document).ready(function() {
    switchToEntity(document.querySelector(".items .entity"));
});
