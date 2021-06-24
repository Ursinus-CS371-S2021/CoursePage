let canvas = new Canvas2D();
let finalStack = [];
let label = document.getElementById("animationlabel");
let slider = document.getElementById("myRange");
let animating = false;

function animate(i) {
    if (animating) {
        slider.value = "" + i;
        redraw();
        if (i < finalStack.length-1 && animating) {
            setTimeout(function() {
                animate(i+1);
            }, 1000);
            
        }
    }
}


function startAnimation() {
    computeHull();
    animating = true;
    slider.value = 0;
    slider.max = finalStack.length-1;
    animate(0);
}


function redraw() {
    canvas.clearLines();
    let output = parseInt(slider.value);
    label.innerHTML = "Step " + (output+1) + " of " + finalStack.length;
    let stack = finalStack[output];
    for (let i = 0; i < stack.length-1; i++) {
        canvas.drawLine(stack[i][0], stack[i][1], stack[i+1][0], stack[i+1][1], [200, 0, 0]);
    }
}

function computeHull() {
    animating = false;
    let stackArr = [];
    stackArr = CCW()
    let temp = CW();
    
    finalStack = stackArr.concat(temp);
    temp[temp.length-1].reverse();
    let finaltemp = [stackArr[stackArr.length-1].concat(temp[temp.length-1])];
    finalStack = finalStack.concat(finaltemp);

    
    let output = slider.value;
    output.innerHTML = slider.value;
    slider.oninput = function() {
        output.innerHTML = this.value;
        slider.max = finalStack.length-1;
        redraw();
    }
    slider.onchange= function() {
        output.innerHTML = this.value;
        slider.max = finalStack.length-1;
        redraw();
    }
    slider.value = 0;
    redraw();
}    





let i = this.ii;
    let span = document.querySelector('span'); // find the <span> element in the DOM
    let increment = document.getElementById('increment'); // find the element with the ID 'getNext'
    let decrement = document.getElementById('decrement'); // find the element with the ID 'getPrev'

    increment.addEventListener('click', function () {
    // this function is executed whenever the user clicks the increment button
    span.textContent = i++;
   
    });

    decrement.addEventListener('click', function () {
    // this function is executed whenever the user clicks the decrement button
    span.textContent = i--;
    
    });




function sortPoints(){
    let P = canvas.getPoints();
    let arr = P.sort(function (x, y) {
        return x[0] - y[0];
    });
    return arr;
}

function CCW(){
    let P = canvas.getPoints();
    let sortedArr = sortPoints();
    let stack = [sortedArr[0]];
    let moreStacks = [];
    let A;
    let B;
    for (let i = 1; i < P.length; i++){
        A = stack[stack.length - 2];
        B = stack[stack.length - 1];
        while (stack.length > 1 && determinant(A, B, sortedArr[i]) < 0){
            stack.pop();
            stackArr = [...stack];
            moreStacks.push(stackArr);
            A = stack[stack.length - 2];
            B = stack[stack.length - 1];
        }
        stack.push(sortedArr[i]);
        stackArr = [...stack];
        moreStacks.push(stackArr);
    }
    return moreStacks;
}

function CW(){
    let P = canvas.getPoints();
    let sortedArr = sortPoints();
    let stack = [sortedArr[0]];
    let A;
    let B;
    let moreStacks = [];
    for (let i = 1; i < P.length; i++){
        A = stack[stack.length - 2];
        B = stack[stack.length - 1];
        while (stack.length > 1 && determinant(A, B, sortedArr[i]) > 0){
            stack.pop();
            stackArr = [...stack];
            moreStacks.push(stackArr);
            A = stack[stack.length - 2];
            B = stack[stack.length - 1];
        }
        stack.push(sortedArr[i]);
        stackArr = [...stack];
        moreStacks.push(stackArr);
    }
    return moreStacks;
}


function determinant(A, B, C){
    let x1 = A[0];
    let x2 = B[0];
    let x3 = C[0];
    let y1 = A[1];
    let y2 = B[1];
    let y3 = C[1];
    let val = x2*y3-x3*y2-x1*y3+x3*y1+x1*y2-x2*y1;
    return val; 
}







function clearEdges() {
    canvas.clearLines();
}

function clearPoints() {
    canvas.clearPoints();
}
