type Fn = (n: number, i: number) => boolean;

/**
 * Filters an array based on a provided function.
 *
 * @param {number[]} arr - The array of numbers to be filtered.
 * @param {Fn} fn - The function to test each element. It takes the element and its index as arguments and returns a boolean indicating whether the element should be included in the new array.
 * @returns {number[]} A new array with the elements that pass the test implemented by the provided function.
 */
function filter(arr: number[], fn: Fn): number[] {
    // Initialize a new array to store the filtered results
    const filteredArr: number[] = [];
    
    // Iterate over each element in the input array
    for (let i = 0; i < arr.length; i++) {
        // Apply the function to the current element and its index
        // If the function returns true, push the element to the filtered array
        if (fn(arr[i], i)) {
            filteredArr.push(arr[i]);
        }
    }
    
    // Return the new array with the filtered values
    return filteredArr;
}