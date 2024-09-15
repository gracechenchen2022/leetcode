/**
 * @return {Function}
 */
var createHelloWorld = function() {
    // 返回一个匿名函数
    return function(...args) {
        return "Hello World";
    }
};


/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */


 