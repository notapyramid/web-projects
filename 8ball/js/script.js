

function m8() {
    var f = gf();
    sf(f);
}

function gf() {
    var f = ["yes", "no", "maybee", "6-7"];
    var r = ran(f.length);
    return f[r];
}

function ran(max){
    return Math.floor(Math.random()*max);
}

function sf(f) {
    document.getElementById("a").innerHTML = f;
}