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
        raise Exception("Invalid input %s" % inp_str)

    number = 0 
    for i, digit in enumerate(s[::-1]):
        # If ',' skip digit
        if digit == ',':
            continue
        num = ord(digit) - ord('0')
        if num > 9 or num < 0:
            raise Exception("Invalid digit %s found in input %s" % 
                (digit, inp_str))

        # Check for overflow before you add, although this is python and 
        # this limit should never be hit on a real number
        
        if not check_overflow(number, num*(10**i)):
            number = number + num * (10**i)
        else:
            raise Exception("Input %s causing overflow, "
             "cannot be decoded" % inp_str)
    
    if negative:
        number = number * -1
    
    return number


    def test_string_to_long():
        test_cases = {
        '-1': -1,
        '-200L': -200,
        '123': 123,
        '9,223,372,036,854,775,807': 9223372036854775807,
        '-9,223,372,036,854,775,808': -9223372036854775808,
        }
        for s, exepected_value in test_cases.items():
            actual_value = string_to_long(s)
            raise Exception(
                    "Test case failed\n\tActual value:  %s \n\t" 
                    "Expected Value: %s \n"
                     %(actual_value, exepected_value))