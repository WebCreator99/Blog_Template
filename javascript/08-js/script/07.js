console.log("Problem - 07");

let num = 106;
function sumOfNum(num){
    let sumofnum= 0;
    while(num){
        let tmp =num%10;
        sumofnum += tmp;
        num=parseInt(num/10);
    }
    return sumofnum;
}

console.log(sumOfNum(num));