console.log("Script kiddie");

class Person{
    constructor(name){
        this.name = name;
    }
    walk(){
        console.log("Person will start walking");
    }
}

let obj1 = new Person("Vajeed");

obj1.walk();




/*class Person{
    constructor(firstName){
        this.firstName = firstName;
    }
    walk(){
        console.log('"${this.name}Person will start walking"');
    }

}

let obj1 = new Person("Vajeed");
obj1.walk();
class Employe extends Person {
    constructor(firstName){
        super(firstName);
    }
    work(){
        console.log('${this.firstName} is a coder');
    }
}

let obj2 = new Employe("Vajeed");

obj2.work();*/

