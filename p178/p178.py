from functools import lru_cache

@lru_cache(maxsize=2**20)
def count_pandigital_step_numbers(start, length=10, seen_zero=False, seen_nine=False,):
    """`start` is starting digit. If None iterate over 1 to 9
    `length` is max number of digits
    `seen_zero` boolean to indicate that 0 is in the step number
    `seen_nine` boolean to indicate that 9 is in the step number
    """
    if start is None:
        return sum([count_pandigital_step_numbers(n,
                                                  length=length,
                                                  seen_zero=seen_zero,
                                                  seen_nine=seen_nine) 
                    for n in range(1, 10)])
    
    seen_zero = True if start == 0 else seen_zero
    seen_nine = True if start == 9 else seen_nine
    n_step = 1 if seen_zero and seen_nine else 0 # count iff step number if pandigital
    if length == 1: 
        return n_step
    if start > 0:
        n_step += count_pandigital_step_numbers(start-1, length-1, seen_zero, seen_nine)
    if start < 9:
        n_step += count_pandigital_step_numbers(start+1, length-1, seen_zero, seen_nine)
    return n_step

if __name__ == '__main__':
    print("Result: {}".format(count_pandigital_step_numbers(None, 40)))