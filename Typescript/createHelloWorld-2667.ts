/**
 * Creates a function that returns "Hello World".
 *
 * @return {() => string} A function that returns the string "Hello World".
 */
const createHelloWorld = (): () => string => {
    // Return a function that ignores its arguments and returns "Hello World"
    return (...args: any[]): string => {
        return "Hello World";
    };
};

/**
 * Example usage:
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */