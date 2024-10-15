/**
 * Type definition for the object returned by the `expect` function.
 */
type ToBeOrNotToBe_implementation = {
    toBe: (expected: any) => boolean;
    notToBe: (expected: any) => boolean;
};

/**
 * Creates an expectation object for the given value, providing methods to assert equality or inequality.
 *
 * @param val - The value to be tested.
 * @returns An object with `toBe` and `notToBe` methods for assertions.
 */
function expect_question(val: any): ToBeOrNotToBe_implementation {
    return {
        /**
         * Asserts that the given value is equal to the expected value.
         *
         * @param expected - The value to compare against.
         * @returns True if the values are equal.
         * @throws Error if the values are not equal.
         */
        toBe: (expected: any): boolean => {
            if (val === expected) {
                return true;
            } else {
                throw new Error("Not Equal");
            }
        },
        /**
         * Asserts that the given value is not equal to the expected value.
         *
         * @param expected - The value to compare against.
         * @returns True if the values are not equal.
         * @throws Error if the values are equal.
         */
        notToBe: (expected: any): boolean => {
            if (val !== expected) {
                return true;
            } else {
                throw new Error("Equal");
            }
        }
    };
}