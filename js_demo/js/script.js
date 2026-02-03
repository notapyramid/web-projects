function askName() {
    var nameReturn = document.getElementById('ask-name');
    var name = prompt('enter ur name');
    if (name == ''){
        alert('eh')
    } else {
        nameReturn.innerHTML='Hello ' + name + '! Nice to meet you'
    }
}

function askQ () {
    var p=prompt('How much wood can a woodchuck chuck');
    if (p != null) {
        document.getElementById('q').innerHTML = 'Wow! ' + p + " is a lot of wood!";
        
    }
}

//its a commit