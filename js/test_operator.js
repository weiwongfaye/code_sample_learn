var obj = {
	valueOf: function () {return 1000;}
};
var total = 3000 -obj;
console.log(total)

var total = 300 - NaN
console.log(total)
var total = 1.1 * 1.1
console.log(total)
console.log(total.toFixed(2))
var total = 20 * undefined
console.log(total)
var total = 20 * null
console.log(total)
var total = 4 * Infinity
console.log(total)
var total = 4 * "XYZ"
console.log(total)
var total = 9/0
console.log(total)
var total = -9/0
console.log(total)
var total = 9/"3"
console.log(total)
var total = 9 % 4;
console.log(total)
var total = 9 % "   4  ";
console.log(total)
var  level = 5;
++level;
console.log(level);
var value =-42;
value = -value
console.log(value)
var num1 = parseInt('1010',2);
var num2 = parseInt('0110',2);
var total = num1 & num2;
console.log(total.toString(2));
var total = num1 | num2;
console.log(total.toString(2));
var total = num1 ^ num2;
console.log(total.toString(2));
var total = num1 << 2
console.log(total.toString(2));

