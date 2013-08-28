import random 

def check_overflow(i,j):
    '''
    Checks if addition of two numbers will cause overflow
    if overflow occurs
    sign of k will be opposite to sign of i and j.

    '''
    k = (i + j)
    if ((i ^ k) & (j ^ k)) < 0:
        return True
    else:
        return False

def string_to_long(inp_str):
    '''
    Takes in input string that represents a floating point number
    and returns a valid floating point number.

    If invalid input is given, then this function raises and Exception
    '''
    s = inp_str
    length = len(s)
    # Check for negative number
    if s[0] == '-':
        negative = True
        s = s[1:]
    else:
        negative = False

    # Check if still a valid input
    if not len(s):
        raise Exception("Invalid input %s" % inp_str)

    #Check for ending with L
    if s[-1] == 'L':
        s = s[:-1]

    #Check if still a valid input
    if not len(s):
        raise InputError("Invalid input %s" % inp_str)

    number = 0 
    digitctr = -1
    for i, digit in enumerate(s[::-1]):

        # If ',' skip digit
        if digit == ',':
            continue
        digitctr+=1
        num = ord(digit) - ord('0')
        if num > 9 or num < 0:
            raise InputError("Invalid digit %s found in input %s" % 
                (digit, inp_str))

        # Check for overflow before you add, although this is python and 
        # this limit should never be hit on a real number
        
        if not check_overflow(number, num*(10**digitctr)):
            number = number + num * (10**digitctr)
        else:
            raise OverflowError("Input %s causing overflow, "
             "cannot be decoded" % inp_str)
    
    if negative:
        number = number * -1
    
    return number


def test_string_to_long():
    # Test at edge cases
    test_cases = {
    '-1': -1,
    '-200L': -200,
    '123': 123,
    '9,223,372,036,854,775,807': 9223372036854775807,
    '-9,223,372,036,854,775,808': -9223372036854775808,
    }
    for s, exepected_value in test_cases.items():
        actual_value = string_to_long(s)
        if actual_value != exepected_value:
            raise Exception(
                "Test case failed\n\tActual value:  %s \n\t" 
                "Expected Value: %s \n"
                 %(actual_value, exepected_value))
    # Test case 2; generate random values and test in the middle
    low = 2**63*-1
    high = 2**63 -1
    for i in xrange(10000):
        item = random.randint(low,high)
        data = string_to_long(str(item))
        if data!= item:
            raise Exception("Test case failed\n\tExpected value  %d\n\t"
                "Actual Value  %d" % (item,data))

if __name__ == "__main__":
    test_string_to_long()



