/* global $, issues */
var scorecard = {
    current: null,
    reset: function(ctx) {
        this.select(issues.getElementById('good'));
        $(".current > .save").one("click", scorecard.save);
    },
    select: function(issue) {
        this.current = issue;
        this.render();
    },
    save: function(ev) {
        console.log(ev);
    },
    render: function() {
        var breadcrumbs = $("#tree-card-breadcrumbs");
        breadcrumbs.children("div").remove();
        var container = $("#tree-card-issues");
        container.empty();
        if (!this.current) return;
        var parent = this.current;
        var self = this;
        while (parent && parent.id) {
            $("<div>").addClass("select").append(
                $('<div>').text(parent.getAttribute('name'))
                    .addClass('button').addClass('breadcrumbs')
                    .click((function(issue) {
                        return function() {
                            self.select(issue);
                        };
                    })(parent))
            ).prependTo(breadcrumbs);
            parent = parent.parentNode;
        }
        var selector = this.current.parentNode.id ? 
            '#' + this.current.parentNode.id:
            this.current.parentNode.nodeName;
        selector += ' > issue[core], ';
        selector += '#' + this.current.id + ' > issue[core]';
        var selected = issues.querySelectorAll(selector);
        container.append($.map(selected, function(issue, index) {
            var li = $('<li>').text(issue.getAttribute('name'));
            li.attr('data-id', issue.id);
            if (issue === self.current) {
                li.addClass('hovered');
            }
            if (issue.depth > self.current.depth) {
                li.css('margin-left', (issue.depth - self.current.depth) + 'em');
            }
            li.click(function() {
                self.select(issue);
            });
            return li;
        }));
    }
};
