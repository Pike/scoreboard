/* global $, diff_match_patch, scorecard */
$(".items .entity").click(function () {
    switchToEntity(this);
});

function switchToEntity(listitem) {
    $(".items .hovered").removeClass('hovered');
    $(listitem).addClass('hovered');
    $("#original").text(listitem.dataset.original);
    var dmp = new diff_match_patch();
    var diffs = dmp.diff_main(listitem.dataset.before, listitem.dataset.after);
    dmp.diff_cleanupSemantic(diffs);
    var eq = 0, add = 0;
    diffs.forEach(function(d) {
        if (d[0] === 0) {
            // equal
            eq += d[1].length;
        }
        else if (d[0] === 1) {
            // addition
            add += d[1].length;
        }
    });
    if (2*add > eq) {
        $("#before").text(listitem.dataset.before);
        $("#after").text(listitem.dataset.after);
    }
    else {
        $("#before").empty();
        $("#after").empty();
        diffs.forEach(function(d) {
            switch (d[0]) {
                case -1:
                    $("<span>").addClass('modified').text(d[1]).appendTo("#before");
                    break;
                case 0:
                    $("<span>").addClass('unchanged').text(d[1]).appendTo("#before");
                    $("<span>").addClass('unchanged').text(d[1]).appendTo("#after");
                    break;
                case 1:
                    $("<span>").addClass('modified').text(d[1]).appendTo("#after");
                    break;
            }
        });
    }
    if (scorecard) {
        scorecard.reset(listitem.dataset);
    }
}
function rows(textarea) {
}

$(document).ready(function() {
    switchToEntity(document.querySelector(".items .entity"));
});
