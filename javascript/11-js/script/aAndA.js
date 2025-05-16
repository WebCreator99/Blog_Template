console.log("script kiddie");

function one(n){
    return n+1;
}

function two(num1,one){
    return num1+one(num1);
}

async function getValues(two,one){
    let promise = new Promise(
        (success,failure)=>{
            //let response_code = 200;
            let response_code = 200;
            if(response_code == 200){
                    //success("Everything is okay");
                    //success(two(5,one));
                    setTimeout(()=>{
                        let sum =two(5,one);
                    success(sum);
                    },2000);
                
            }else{
                setTimeout(()=>{
                    failure("Something wen wrong");
                },3000);
            }
            
        }
    )
    return await promise;
    
}


getValues(two,one).then(
    (success)=>{
    console.log(success);
    },
    (failure)=>{
        console.log(failure);
    }

)

console.log("I am last");


