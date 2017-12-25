// let is similar to var but let has scope. let is only accessible in the block level it is defined.
if (true) {
  let a = 40;
  console.log(a); // 40
}
 // console.log(a);  undifined -> throw an error

// Const is used to assign a constant value to the variable. And the value cannot be changed. Its fixed.
 const a = 50;
 // a = 60 => throws error. You cannot change the value
 const LANGUAGES = ['js','py','kt','go'];
 // LANGUAGES = "javascript" => error
 LANGUAGES.push('cpp'); // works
 console.log(LANGUAGES);

/* ================== ARROW FUNCTIONS ================== */

// OLD FUNCTIONS

function oldOne() {
  console.log("Hello from oldies");
}

var newOne = () =>{
  console.log("Hello from news");
}

var newOneWithParams = (a,b = 15) =>{
  console.log(a+b);
}

oldOne();
newOne();
newOneWithParams(23);
newOneWithParams(23,788);


/** LOOPS  **/


let arr = [1,2,3,4,5,6]
for (let value of arr){
  console.log(value);
}

let word = "enzoftware"
for (let letter of word){
  console.log(letter);
}

/** SPREAD ATTRIBUTES **/

let sumElements = (...arr) =>{
  console.log(arr);
  var sum = 0;
  for (let elem of arr){
    sum += elem;
  }
  console.log(sum);
}

sumElements(1,2,6,4,5,8);
console.log(Math.max(1,2,3,5,6,52));


/**  MAPS  : Map holds key-value pairs.
It’s similar to an array but we can define our own index.
And indexes are unique in maps.**/

var newMap = new Map();
newMap.set('hello','world');
newMap.set('id', 2345796);
newMap.set('interest', ['js', 'ruby', 'python']);
newMap.get('name'); // John
newMap.get('id'); // 2345796
newMap.get('interest'); // ['js', 'ruby', 'python']
console.log(newMap.size);
console.log(newMap.keys());
console.log(newMap.values());

/** SETS **/
var sets = new Set([1,5,6,8,9]);
sets.size; // returns 5. Size of the size.
sets.has(1); // returns true.
sets.has(10); // returns false.

/** STATIC METHODS **/
class Example {
  static CallMe(){
    console.log("Static Method invoque");
  }
  constructor() {

  }
}
// NO INSTANCE , NO FUCTION CALL
Example.CallMe();

class Persona {
  constructor(name) {
    this.name = name;
  }

  get Name(){
    return this.name;
  }

  set Name(name){
    this.name = name;
  }
}

let person = new Persona("Enzo");
console.log(person.Name);
person.Name = "EnzoFrancesco";
console.log(person.Name);
