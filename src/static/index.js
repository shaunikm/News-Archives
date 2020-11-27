function search(){
    document.write('loading..');
    var state = document.getElementById('day').value;
    window.location.replace('/day/' + state);
}