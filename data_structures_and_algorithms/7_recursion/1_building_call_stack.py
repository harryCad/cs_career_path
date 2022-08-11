"""
Building Our Own Call Stack
The best way to understand recursion is with lots of practice! At first, this method of solving a problem can seem unfamiliar but by the end of this lesson, we’ll have implemented a variety of algorithms using a recursive approach.

Before we dive into recursion, let’s replicate what’s happening in the call stack with an iterative function.

The call stack is abstracted away from us in Python, but we can recreate it to understand how recursive calls build up and resolve.

Let’s write a function that sums every number from 1 to the given input.

sum_to_one(4)
# 10
sum_to_one(11)
# 66
To depict the steps of a recursive function, we’ll use a call stack and execution contexts for each function call.

The call stack stores each function (with its internal variables) until those functions resolve in a last in, first out order.

call_stack = []
recursive_func()
call_stack = [recursive_func_1]

# within the body of recursive_func, another call to recursive_func()
call_stack = [recursive_func_1, recursive_func_2]
# the body of the second call to recursive_func resolves...
call_stack = [recursive_func_1]
# the body of the original call to recursive_func resolves...
call_stack = []
Execution contexts are a mapping between variable names and their values within the function during execution. We can use a list for our call stack and a dictionary for each execution context.

Let’s get started!

Instructions
1.
Define a sum_to_one() function that has n as the sole parameter.

Inside the function body:

declare the variable result and set it to 1.
declare the variable call_stack and set it to an empty list.
Use multiple return to return both of these values: result, call_stack

Checkpoint 2 Passed

Stuck? Get a hint
2.
Fill in the sum_to_one() function body by writing a while loop after the variable call_stack.

This loop represents the recursive calls which lead to a base case.

We’ll want to loop until the input n reaches 1.

Inside the loop, create a variable execution_context and assign it to a dictionary with the key of "n_value" pointing to n.

Use a list method to add execution_context to the end of call_stack.

This is our way of simulating the recursive function calls being “pushed” onto the system’s call stack.

Decrement n after its value has been stored.

End the loop by printing call_stack.

Checkpoint 3 Passed

Stuck? Get a hint
3.
After the while loop concludes, we’ve reached our “base case”, where n == 1.

At this point we haven’t summed any values, but we have all the information we’ll need stored in our call_stack.

In the next exercise, we’ll handle the summation of values from the execution contexts captured in call_stack.

For now, print out “BASE CASE REACHED” outside of the loop block before our multiple return statement.
"""

# define your sum_to_one() function above the function call
def sum_to_one(n):
    result = 1
    call_stack = []

    while n != 1:
        execution_context = {'n_value':n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print('BASE CASE REACHED')
    return result, call_stack

sum_to_one(4)