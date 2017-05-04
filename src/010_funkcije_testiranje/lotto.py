import random

__author__ = 'mpolensek'
# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.


def generate_lotto_nums():
    """Generates lotto numbers
    Generates 7 pseudo-random numbers in range 1 - 39 (both limits included)
    plus an extra number
 
    :return: tuple [lotto_nums, extra_num]
    """
    lotto_nums = []
    while True:
        selected_num = random.randint(1, 39)  # Select random number
        if selected_num not in lotto_nums:    # Check if it was already selected
            if len(lotto_nums) != 7:
                lotto_nums.append(selected_num)
            else:
                extra_num = selected_num
                break
    return sorted(lotto_nums), extra_num  # Return both, sorted lotto nums and extra num

if __name__ == '__main__':
    print generate_lotto_nums()

