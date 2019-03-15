def p006(n):
    return int(n**4/4 + n**3/6 - n**2/4 - n/6)

if __name__ == '__main__':
    for LIMIT in [10, 100]:
        print("")
        print("limit = {}".format(LIMIT))
        print("Sum square difference: {}".format(p006(LIMIT)))
