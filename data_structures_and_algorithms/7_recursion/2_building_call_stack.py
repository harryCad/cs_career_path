"""
Building Our Own Call Stack, Part II
In the previous exercise, we used an iterative function to implement how a call stack accumulates execution contexts during recursive function calls.

We’ll now address the conclusion of this function, where the separate values stored in the call stack are accumulated into a single return value.

Instructions
1.
This is the point in a recursive function when we would begin returning values as the function calls are “popped” off the call stack.

We’ll use another while loop to simulate this process. Write the while loop below the “Base Case Reached” print statement.

This loop will run as long as there are execution contexts stored in call_stack.

Inside this second loop:

declare the variable return_value
assign the last element in call_stack to return_value.
Remove that value from call_stack otherwise you’ll have an infinite loop!
Print call_stack to see how the execution contexts are removed from call_stack.


Stuck? Get a hint
2.
Print that you’re adding return_value["n_value"] to result and their respective values.

Finish the loop by retrieving "n_value" from return_value and add it to result.
"""

def sum_to_one(n):
    result = 1
    call_stack = []

    while n != 1:
        execution_context = {"n_value": n}
        call_stack.append(execution_context)
        n -= 1
        print(call_stack)
    print("BASE CASE REACHED")

    while call_stack:
        return_value = call_stack.pop()
        print(call_stack)
        #print(return_value["n_value"])
        print(f"adding {return_value['n_value']} to {result}")
        result += return_value["n_value"]

    return result, call_stack

sum_to_one(4)