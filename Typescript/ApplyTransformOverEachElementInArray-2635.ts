/**
 * Applies a given function to each element of an array and returns a new array with the results.
 *
 * @param {number[]} arr - The array of numbers to be mapped.
 * @param {(n: number, i: number) => number} fn - The function to apply to each element. It takes the element and its index as arguments and returns a new value.
 * @returns {number[]} A new array with the results of applying the function to each element of the input array.
 */
function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    // Initialize a new array to store the results
    let newArr: number[] = [];
    
    // Iterate over each element in the input array
    for (let i = 0; i < arr.length; i++) {
        // Apply the function to the current element and its index, then push the result to the new array
        newArr.push(fn(arr[i], i));
    }
    
    // Return the new array with the mapped values
    return newArr;
}
