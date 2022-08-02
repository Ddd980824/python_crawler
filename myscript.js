function tableCreate() {
    var mydiv = document.getElementById('mydiv');
    var tbl = document.createElement('table');
    tbl.style.width = '100px';
    tbl.style.border = '1px solid black';

    for (var i = 0; i < 5; i++) {
        var tr = tbl.insertRow();
        for (var j = 0; j < 4; j++) {
            var td = tr.insertCell();
            td.appendChild(document.createTextNode('food' + i + ',' + j));
            td.style.border = '1px solid black';
        }
    }
    mydiv.appendChild(tbl);
}