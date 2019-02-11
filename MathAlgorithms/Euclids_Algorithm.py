'''
Euclids Algorithm is used to find the greatest common factors between 2 numbers
'''


def find_gcf(num1, num2, verbose=False):
    if num1 == num2:
        if verbose:
            print('{0} equals to {1}, so the GCF is {0}'.format(num1, num2))
        return num1
    else:
        while num1 != num2:
            greater_num = max(num1, num2)
            smaller_num = min(num1, num2)
            new_num = greater_num - smaller_num
            if verbose:
                print('{0} is greater than {1}, so the new number is {0} - {1} = {2}'.format(greater_num, smaller_num, new_num))
            if new_num == smaller_num:
                if verbose:
                    print('{0} equals to {1}, so the GCF is {0}'.format(new_num, smaller_num))
                return new_num
            else:
                num1 = new_num
                num2 = smaller_num
                if verbose:
                    print('{0} is used to replace {1}, so the new pair of numbers are {0} and {2}'.format(new_num, greater_num, smaller_num))


# Testing
find_gcf(81+63, 162, True)
