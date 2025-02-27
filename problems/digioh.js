/**
 * f(x) takes in integer X and returns an array of 5 integers that, 
 * when added, equal the integer X. None of the 5 integers can be repeated.
 */

function noChange(x) {
    check = {};
    nums = [];
    total = 0;
    while(nums.length < 4) {
        positiveOrNegative = Math.floor(Math.random() * 2)
        num = Math.floor(Math.random() * 1000);

        if (!positiveOrNegative) {
            num *= -1
        }

        if(!(num in check)) {
            nums.push(num)
            total += num;
            check[num] = true
        }
    }

    last = x - total;

    if (!(last in check)){
        nums.push(last);
    }
    
    console.log(nums)
    return nums
}

