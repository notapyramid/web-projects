function askName() {
    var nameReturn = document.getElementById('ask-name');
    var name = prompt('enter ur name');
    if (name == ''){
        alert('eh')
    } else {
        nameReturn.innerHTML='Hello ' + name + '! Nice to meet you'
    }
}