/**
 * Creates a counter function that increments and returns a number each time it is called.
 *
 * @param n - The initial number to start the counter from.
 * @returns A function that increments and returns the counter value.
 */
function createCounter(n: number): () => number {
    /**
     * Increments and returns the current counter value.
     *
     * @returns The current counter value before incrementing.
     */
    return function(): number {
        return n++;
    }
}