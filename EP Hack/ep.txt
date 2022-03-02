var p = prompt("is there two info at start?")
    var e = setInterval(function () {
        try {
            document.getElementById("sections-list").children.item(go()).click();
            var n = Math.floor(Math.random() * angular.element(".title-number.ng-binding").length);
            angular.element(".title-number.ng-binding").get(n).parentElement.click();
            if (n == angular.element(".title-number.ng-binding").length) angular.element(".continue").get(1).children.item(0).click();
            start()
        } catch { }
    }, 1);
var things = [];
var start = function () {
    things = [];
    var len = document.getElementById("sections-list").children.length;
    for (let i = 0; i < len - 2; i++) {
        if (check(i) == true) { things.push(document.getElementById("sections-list").children.item(i)) };
    }
    things[Math.floor(Math.random() * things.length)].click()
}
var check = function (i) {
    if (document.getElementById("sections-list").children.item(i).children.item(0).children.item(1).children.item(1).children.item(0).attributes.getNamedItem("style").value != 'width: 100%;') return true;
    return false;
}

function go() {
    if (p == 'yes') return 1;
    if (p == 'no') return 0;
}