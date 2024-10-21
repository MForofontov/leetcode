type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

/**
 * Creates a counter object with increment, decrement, and reset methods.
 *
 * @param {number} init - The initial value of the counter.
 * @return {Counter} An object with methods to increment, decrement, and reset the counter.
 */
function createCounter2(init: number): Counter {
    // Initialize the current value of the counter
    let currentValue = init;

    return {
        /**
         * Increments the counter by 1.
         *
         * @returns {number} The new value of the counter after incrementing.
         */
        increment: (): number => {
            currentValue += 1;
            return currentValue;
        },

        /**
         * Decrements the counter by 1.
         *
         * @returns {number} The new value of the counter after decrementing.
         */
        decrement: (): number => {
            currentValue -= 1;
            return currentValue;
        },

        /**
         * Resets the counter to its initial value.
         *
         * @returns {number} The value of the counter after resetting.
         */
        reset: (): number => {
            currentValue = init;
            return currentValue;
        }
    };
}