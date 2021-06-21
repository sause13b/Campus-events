window.onload = function () {
    var link = document.getElementsByClassName('navigation_bottom');
    link[0].classList.add('active');
    for (let i = 0; i < link.length; i++) {
        link[i].addEventListener('click', function () {
            localStorage.setItem('link', this);
        })
    }

    for (let i = 0; i < link.length; i++) {
        if (link[i] == localStorage.getItem('link')) {
            link[0].classList.remove('active');
            link[i].classList.add('active');
        }
    }
    var back_link = document.getElementsByClassName('back_to_main_bottom');
    back_link[0].addEventListener('click', function(){
        localStorage.clear();
    })
}