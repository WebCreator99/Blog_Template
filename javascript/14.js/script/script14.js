let mainDiv = document.getElementById("main");
console.log(mainDiv.childElementCount);
console.log(mainDiv.children);
let listUI = document.getElementById("list");
let childs = mainDiv.childNodes;

let emptyDiv = document.getElementById("empty");
let child = mainDiv.childNodes;

/*
childs.forEach(element => {
    console.log(element.textContent);
    
});
*/

//console.log(mainDiv.firstChild);
//console.log(mainDiv.lastChild);

//console.log(listUI.parentNode);
/*
let itemLi= document.getElementById("secondItem");
console.log(itemLi.previousElementSibling);
console.log(itemLi.nextElementSibling);
*/

let ulElement = document.createElement("ol");

ulElement.setAttribute("class","myClass");
ulElement.setAttribute("id","myId");

for(let i=0; i<5; i++){
    ulElement.innerHTML += `<li>Item ${i+1}</li>`;

}
mainDiv.appendChild(ulElement);
mainDiv.removeChild(listUI);

alert("you have been hacked");

let b = confirm("This website need your location");
let a =prompt("What is your name?");
console.log(a);
console.log(b);

