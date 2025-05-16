console.log("Script kiddie");

/*let promise = new Promise(
    (success,failure)=>{
        success("Everything is okay");
        failure("Something wen wrong");
    }
)

promise.then(
    (success)=>{
    console.log(success);
    },
    (failure)=>{
        console.log(failure);
})
)*/



/*let promise = new Promise(
    (success,failure)=>{
        //let response_code = 200;
        let response_code = 100;
        if(response_code == 200){
            success("Everything is okay");
        }else{
            failure("Something wen wrong");
        }
        
    }    
)

promise.then(
    (success)=>{
    console.log(success);
    },
    (failure)=>{
        console.log(failure);
})*/

let promise = new Promise(
    (success,failure)=>{
        //let response_code = 200;
        let response_code = 100;
        if(response_code == 200){
            setTimeout(()=>{
                success("Everything is okay");
            },2000);
        }else{
            setTimeout(()=>{
                failure("Something wen wrong");
            },3000);
        }
        
    }    
)

promise.then(
    (success)=>{
    console.log(success);
    },
    (failure)=>{
        console.log(failure);
})


