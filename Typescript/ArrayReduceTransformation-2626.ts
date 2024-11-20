/**
 * Reduces an array to a single value using a provided reducer function.
 *
 * @param {number[]} nums - The array of numbers to be reduced.
 * @param {Fn} fn - The reducer function. It takes the accumulator and the current element as arguments and returns the updated accumulator.
 * @param {number} init - The initial value for the accumulator.
 * @returns {number} The final reduced value.
 */
function reduce(nums: number[], fn: CallableFunction, init: number): number {
    // Initialize the accumulator with the initial value
    let val = init;

    // Iterate through the array and apply the reducer function
    for (let i = 0; i < nums.length; i++) {
        // Update the accumulator with the function result
        val = fn(val, nums[i]);
    }

    // Return the final result
    return val;
}