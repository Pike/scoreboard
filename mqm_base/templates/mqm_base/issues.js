/* global DOMParser */
var issues;
(function(){
    var parser = new DOMParser();
    issues = parser.parseFromString("{{ issues_xml|escapejs }}", 'text/xml');
    var moz_doc = parser.parseFromString("{{ moz_issues_xml|escapejs }}", 'text/xml');
    Array.from(moz_doc.querySelectorAll('issue')).forEach(function(moz_issue) {
        var mqm_issue = issues.getElementById(moz_issue.id);
        if (!mqm_issue) {
            var new_issue = issues.importNode(moz_issue, true);
            // TODO find parent if wanted
            var parent = issues.documentElement;
            parent.appendChild(new_issue);
            return;
        }
        for (var i=0, ii=moz_issue.attributes.length; i<ii; ++i) {
            var attr = moz_issue.attributes[i];
            if (attr.name !== 'id') {
                if (attr.value !== 'no') {
                    mqm_issue.setAttribute(attr.name, attr.value);
                }
                else {
                    mqm_issue.removeAttribute(attr.name);
                }
            }
        }
    });
    Array.prototype.forEach.call(issues.querySelectorAll('issue'),
        function(issue) {
            issue.depth = issue.parentElement.nodeName === 'issue' ?
                issue.parentElement.depth + 1 : 0;
        }
    );
})();