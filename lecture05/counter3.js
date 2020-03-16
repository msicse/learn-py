let counter = 0;

document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('button').onclick = count;
});

function count(){
    counter++;
    document.querySelector("#counter").innerHTML = counter;

    if(counter % 10 === 0){
        alert(`Counter is ${counter}`);
    }

}