// const text = '{"name":"John", "age":"function a() {return 30;}", "city":"New York"}';
// var obj = JSON.parse(text);
// console.log(obj)


    // function a() 
    // {
    //     return 30;
    // }
    // // a()
    // console.log(a());


    // const fruits = ["Banana", "Orange", "Apple", "Mango"];
    // fruits.push("Kiwi");
    // console.log(fruits)


var jsonStr = '{"theTeam":[{"teamId":"1","status":"pending"},{"teamId":"2","status":"member"},{"teamId":"3","status":"member"}]}';

var obj = JSON.parse(jsonStr);
obj['theTeam'].push({"teamId":"4","status":"pending"});
console.log(obj)
// jsonStr = JSON.stringify(obj);