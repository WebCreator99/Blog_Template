let btn = document.getElementById('myBtn');

let div = document.getElementById('boxDiv');

btn.addEventListener('click', () => {
    btn.classList.toggle('click');
});

div.addEventListener("mousedown", () => {
    div.innerHTML = "Mouse clicked";
});

/*
div.addEventListener("mouseover", () => {
    div.innerHTML = "Mouse hover";
});

div.addEventListener("mouseout", () => {
    div.innerHTML = "Mouse out";
});
*/


/*
btn.addEventListener('click', () => {
    btn.setAttribute('class', 'click');
});
*/

let input = document.getElementById('myInput');
input.addEventListener("keypress", (key) => {
    div.innerHTML = `${key.key} is Key pressed `;
});

let list = document.getElementById('list');

list.addEventListener("click", (ele) => {
    if(ele.target.toggle = 'li'){
        let name = ele.target.getAttribute('name');
        switch(name){
            case 'home':
                div.innerHTML = "Home is clicked";
                break;
            case 'about':
                div.innerHTML = "About is clicked";
                break;
            case 'services':
                div.innerHTML = "Services is clicked";
                break;
            case 'contact':
                div.innerHTML = "Contact is clicked";
                break;
        }
    }
});