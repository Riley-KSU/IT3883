# Program 3

### What is the problem with the program?
### The program will keep checking divisors even after proving the number is not prime. This is why it’s so slow.
### What solution did you implement?
### I changed the code so when it finds a divisor it will return false and go to the next one. If it finishes without finding one it returns true. This is so it does not do an checks for noon prime numbers.
### Does your solution have any drawbacks or limitations? Explain why or why not.
### This solution has the downside of being slow on larger numbers as still has to test 2 thought the number – 1. Although this method has the benefit in performance for numbers that have a divisor.