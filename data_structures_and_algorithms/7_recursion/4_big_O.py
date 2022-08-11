"""
Recursion and Big O
Excellent job writing your first recursive function. Our next task may seem familiar so there won’t be as much guidance.

We’d like a function factorial that, given a positive integer as input, returns the product of every integer from 1 up to the input. If the input is less than 2, return 1.

For example:

factorial(4)
# 4 * 3 * 2 * 1
# 24
Since this function is similar to the previous problem, we’ll add an additional wrinkle. You’ll need to evaluate the big O runtime of the function.

Note that if this is the first time you’re seeing Big O notation, this might be a bit confusing. You can learn much more about this topic in the Asymptotic Notation section of the Computer Science path. That being said, it is also fine to just continue working through this course and learn more about Big O later!

With an iterative function, we would consider how the number of iterations grows in relation to the size of the input.

For example you may ask yourself, are we looping once more for each new element in the list?

That’s linear or O(N).

Are we looping an additional number of elements in the list for each new element in the list?

That’s quadratic or O(N^2).

With recursive functions, the thought process is similar but we’re replacing loop iterations with recursive function calls.

In other words, are we recursing once more for each new element in the list?

That’s linear or O(N).

Let’s analyze our previous function, sum_to_one().

sum_to_one(4)
# recursive call to sum_to_one(3)
# recursive call to sum_to_one(2)
# recursive call to sum_to_one(1)

# Let's increase the input...

sum_to_one(5)
# recursive call to sum_to_one(4)
# recursive call to sum_to_one(3)
# recursive call to sum_to_one(2)
# recursive call to sum_to_one(1)
What do you think? We added one to the input, how many more recursive calls were necessary?

Talk through a few more inputs and then start coding when you’re ready to move on.

Instructions
1.
Define the factorial function with one parameter: n.

Set up a base case.

Think about the input(s) that wouldn’t need a recursive call for your function.

Return the appropriate value.


Stuck? Get a hint
2.
Now let’s consider the recursive step for factorial().

If we’re in the recursive step that means factorial() has been invoked with an integer of at least 2.

We need to return the current input value multiplied by the return value of the recursive call.

Structure the recursive call so it invokes factorial() with an argument one less than the current input.


Stuck? Get a hint
3.
Nice work, test out your function by printing the result of calling factorial() with 12 as an input.

Now, change the input to a really large number, think big, and run the code.

If you chose an input large enough, you should see a RecursionError.
"""

# Define factorial() below:
def factorial(n):
    if n < 2:
        return n
    return n * factorial(n-1)

print(factorial(12))
print(factorial(992305923509813412))