console.log("Javascript - 11");


function one(n){
    return n+1;
}

function two(num1,one){
    return num1+one(num1);
}

let sum = two(5,one);

console.log(sum);

function output(value) {
    let sum = two(value,one);

    console.log(sum);
}

setTimeout(() => {
    output(5);
    //console.log("I am setTimeout");
},3000);

console.log("I am last");