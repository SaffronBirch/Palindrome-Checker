"""
A function that is used to check whether a string is a palindrome. It 
iterates through the first half of the string and adds each character to a stack,
and then iterates through the last half of the string in order to check to see of the
elements in the stack are the same as the string. If they match, then the string is
a palindrome, if not then it isn't a palindrome.
"""
def is_palindrome(palindrome):
    stack = []
    palindrome_list = []
    n = int(len(palindrome))

    """
    Adding the elements of the string to a list, to make them more accessible
    """
    for c in palindrome:
        palindrome_list += c
    
    """
    A for loop is used to check whether an element is a space or not. If it is, then
    it is skipped over, and the next element is looped at. If it is not a space, then
    it is added to the stack.
    """
    for chr in range(int(n/2)):
        if (chr == " "):
            chr = chr + 1
        else:
            stack += palindrome[chr]
    
    
    """
    A while loop is used in order to check whether the stack is empty or not,
    if it is empty then an if statement along with a for loop is used to check whether
    n is odd or even. The function then checks if the first element in the stack is
    equal to the element last element of the string and if they match, then the 
    character is removed from the stack, and the for loop continues. If they do not match, 
    then 'False' is returned. Once the stack is empty, 'True' is returned to indicate 
    that the string is a palindrome.
    """
    while (stack != []):
        if (n % 2 == 0):
            for i in stack:
                if i == palindrome_list[-1]:
                    stack.pop()
                    palindrome_list.pop(-1)
                else:
                    return False
                    break
        if (n % 2 != 0):
            for i in stack:
                if i == palindrome_list[-1]:
                    stack.pop()
                    palindrome_list.pop(-1)
                else:
                    return False
                    break
    
    if (stack == []):
        return True



print(is_palindrome('level'))