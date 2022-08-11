"""
Sum to One with Recursion
Now that we’ve built a mental model for how recursion is handled by Python, let’s implement the same function and make it truly recursive.

To recap: We want a function that takes an integer as an input and returns the sum of all numbers from the input down to 1.

sum_to_one(4)
# 4 + 3 + 2 + 1
# 10
Here’s how this function would look if we were to write it iteratively:

def sum_to_one(n):
  result = 0
  for num in range(n, 0, -1):
    result += num
  return result

sum_to_one(4)
# num is set to 4, 3, 2, and 1
# 10
We can think of each recursive call as an iteration of the loop above. In other words, we want a recursive function that will produce the following function calls:

recursive_sum_to_one(4)
recursive_sum_to_one(3)
recursive_sum_to_one(2)
recursive_sum_to_one(1)
Every recursive function needs a base case when the function does not recurse, and a recursive step, when the recursing function moves towards the base case.

Base case:

The integer given as input is 1.
Recursive step:

The recursive function call is passed an argument 1 less than the last function call.
Instructions
1.
Define the sum_to_one() function.

It takes n as the sole parameter.

We’ll start by setting up our base case.

This function should NOT recurse if the given input, n is 1.

In the base case, we return n.

2.
Now, we’ll consider the recursive step.

We want our return value to be the current input added to the return value of sum_to_one().

We also need to invoke sum_to_one() with an argument that will get us closer to the base case.

# return {recursive call} + {current input}

Stuck? Get a hint
3.
Each recursive call is responsible for adding one of those integers to the ultimate total.

To help us visualize the different function calls, add a print statement before the recursive call that tells us the current value of n.

Use the following string for the print statement: print("Recursing with input: {0}".format(n))

Let’s test out our function. Call sum_to_one() with 7 as input and print out the result. Nice work!
"""

# Define sum_to_one() below...
def sum_to_one(n):
    if n == 1:
        return n
    print(f"Recursing with input: {n}")
    return n + sum_to_one(n-1)
# uncomment when you're ready to test
print(sum_to_one(7))