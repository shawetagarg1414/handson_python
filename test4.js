var config = require('./test3.json');
// console.log(config.firstName + ' ' + config.lastName);

// const objc = JSON.parse('{"name":"John", "age":30, "city":"New York"}');
// console.log(objc);

// const objcc = '{"name":"John", "age":"30", "city":"New York"}';
// console.log(objcc);
// const objcc = JSON.parse(text);
// var objcc = JSON.parse(text);
// console.log(objcc)

// const textt = '{"name":"John", "age":"function () {return 30;}", "city":"New York"}';
// const obj = JSON.parse(textt);
// console.log(obj)

var obj = '{"list":[{"name":"John", "age":"30", "city":"New York"}]}';
var objc = JSON.parse(jsonStr);
objc['list'].push({"name":"4","sage":"pending","date":"pending"});
console.log(objc);

// var jsonStr = '{"theTeam":[{"teamId":"1","status":"pending"},{"teamId":"2","status":"member"},{"teamId":"3","status":"member"}]}';
// var obj = JSON.parse(jsonStr);
// obj['theTeam'].push({"teamId":"4","status":"pending"});
// jsonStr = JSON.stringify(obj);