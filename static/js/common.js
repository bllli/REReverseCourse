/*
* js中的常用函数    
*/

// 将伪数组对象转换成真数组
function s(selector) {
    var arr = [];
    document.querySelectorAll(selector).forEach(function (item) {
        arr.push(item);
    })
    return arr;
}
// 求取[min,max]之间的平均数
function getRandom(min,max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}
// 复制对象中的属性
function extend(parent,child) {
    for(var key in parent) {
        if (child[key]) {
            continue;
        }
        child[key] = parent[key];
    }
}