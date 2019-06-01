from time import time

def search(ncorrect, correct, digits=None):
    digits = [] if digits is None else digits
    
    ld = len(digits)
    
    if (ncorrect == 0) or (ld == len(COLUMNS)):
        if ncorrect == 0:
            return digits
        else:
            return None

    for key, value in COLUMNS[ld]:
        if ld == 3:
            print(digits+[key], time()-T0)
        
        if (ncorrect-value) >= 0:
            _correct = correct[:]
            for i, row in enumerate(GUESSES):
                if row[ld] == key:
                    _correct[i] -= 1
            if (sum(_correct) == (ncorrect-value)) and min(_correct) >= 0:
                result = search(ncorrect-value, _correct, digits=digits+[key])
                if result is not None:
                    return result

if __name__ == '__main__':
    T0 = time()

#     GUESSES = ((9,0,3,4,2), 
#            (7,0,7,9,4), 
#            (3,9,4,5,8), 
#            (3,4,1,0,9), 
#            (5,1,5,4,5), 
#            (1,2,5,3,1),)

#     CORRECT = (2,0,2,1,2,1,)

    GUESSES = ((5,6,1,6,1,8,5,6,5,0,5,1,8,2,9,3),
               (3,8,4,7,4,3,9,6,4,7,2,9,3,0,4,7),
               (5,8,5,5,4,6,2,9,4,0,8,1,0,5,8,7),
               (9,7,4,2,8,5,5,5,0,7,0,6,8,3,5,3),
               (4,2,9,6,8,4,9,6,4,3,6,0,7,5,4,3),
               (3,1,7,4,2,4,8,4,3,9,4,6,5,8,5,8),
               (4,5,1,3,5,5,9,0,9,4,1,4,6,1,1,7),
               (7,8,9,0,9,7,1,5,4,8,9,0,8,0,6,7),
               (8,1,5,7,3,5,6,3,4,4,1,1,8,4,8,3),
               (2,6,1,5,2,5,0,7,4,4,3,8,6,8,9,9),
               (8,6,9,0,0,9,5,8,5,1,5,2,6,2,5,4),
               (6,3,7,5,7,1,1,9,1,5,0,7,7,0,5,0),
               (6,9,1,3,8,5,9,1,7,3,1,2,1,3,6,0),
               (6,4,4,2,8,8,9,0,5,5,0,4,2,7,6,8),
               (2,3,2,1,3,8,6,1,0,4,3,0,3,8,4,5),
               (2,3,2,6,5,0,9,4,7,1,2,7,1,4,4,8),
               (5,2,5,1,5,8,3,3,7,9,6,4,4,3,2,2),
               (1,7,4,8,2,7,0,4,7,6,7,5,8,2,7,6),
               (4,8,9,5,7,2,2,6,5,2,1,9,0,3,0,6),
               (3,0,4,1,6,3,1,1,1,7,2,2,4,6,3,5),
               (1,8,4,1,2,3,6,4,5,4,3,2,4,5,8,9),
               (2,6,5,9,8,6,2,6,3,7,3,1,6,8,6,7),)

    CORRECT = (2,1,3,3,3,1,2,3,1,2,3,1,1,2,0,2,2,3,1,3,3,2,)

    CORRECT, GUESSES = zip(*sorted(zip(CORRECT, GUESSES), key=lambda x: x[0]))

    COLUMNS = [{j:0 for j in range(10)} for i in range(len(GUESSES[0]))]
    for ROW in GUESSES:
        for D, VALUE in zip(COLUMNS, ROW):
            D[VALUE] += 1

    COLUMNS = [sorted(tuple(C.items()), key=lambda x: x[1], reverse=True) for C in COLUMNS]

    RESULT = search(sum(CORRECT), list(CORRECT))
    RESULT = ''.join(map(str, RESULT))

    SECONDS = time() - T0

    MINUTES, SECONDS = divmod(SECONDS, 60)
    HOURS, MINUTES = divmod(MINUTES, 60)

    print("Result: {}".format(RESULT))
    print("Time elapsed = {:.0f}h {:.0f}m {:f}s".format(HOURS, MINUTES, SECONDS))