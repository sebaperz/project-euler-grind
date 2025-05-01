# Longest Collatz sequence
# https://projecteuler.net/problem=14

def number_of_steps_collatz(num):
    steps = 1
    save = num
    while num != 1:
        if num % 2 == 0:
            num /= 2
        else:
            num = 3 * num + 1
        steps += 1
    return [steps,save]

max_steps = [0, 0]
for i in range(1, 1000000):
    steps = number_of_steps_collatz(i)
    if steps[0] > max_steps[0]:
        max_steps = steps
print(max_steps)
