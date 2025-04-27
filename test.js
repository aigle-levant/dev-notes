console.log("With setTimeout");
// for (var i=0; i<3; i++) {
//     setTimeout(() => {
//         console.log('var i:', i);
//     }, 1000);
// }

setTimeout(() => {
    for (var i=0; i<3; i++) {
        console.log('var i:', i);
    }
}, 1000);

// console.log("With setTimeout");
// for (var i=0; i<3; i++) {
//     console.log('var i:', i);
// }