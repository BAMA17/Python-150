def checkio(numbers_array):
    """The value of the key parameter should be a function that takes a single argument and returns a key to use for sorting purposes. 
    This technique is fast because the key function is called exactly once for each input record."""
    
    #key specifies a function of one argument that is used to extract a comparison key from each list element
    return sorted(list(numbers_array) , key=abs  )

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"