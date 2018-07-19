def get_digits(n):
    """get digits of a number. Return as list"""
    digits = []
    while True:
        n, digit = divmod(n, 10)
        digits.append(digit)
        if n == 0:
            break

    return digits

def is_palindrome(n):
    """Check if a number is a palindrome"""
    digits = get_digits(n)
    ln = len(digits)
    for i in range(ln//2):
        if digits[i] != digits[ln-1-i]:
            return False
    return True

def p004(ndigit):
    ulimit = 10**ndigit - 1 # upper limit
    llimit = 10**(ndigit-1) - 1 # lower limit

    mx = 0 # biggest palindrome found so far

    # iterate backwards to encounter largest palindrome sooner
    for n1 in range(ulimit, llimit, -1):
        for n2 in range(ulimit, n1-1, -1):

            # if n1*n2 is smaller than largest palindrome it will continue to
            # be so becaue n2 is decreasing
            if n1*n2 <= mx:
                break

            if is_palindrome(n1*n2):
                mx = n1*n2

    return mx

if __name__ == '__main__':

    for ndigit in range(2, 5):
        print("Largest palindrome for {} digits = {}".format(ndigit, p004(ndigit)))
