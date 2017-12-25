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
