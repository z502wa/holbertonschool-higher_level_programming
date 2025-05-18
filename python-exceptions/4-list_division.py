#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divides element by element two lists.
    Prints error messages on exception and appends 0 for failures.
    Returns a new list of length list_length with all division results.
    """
    result = []
    for i in range(list_length):
        try:
            # attempt to divide corresponding elements
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        except (TypeError, ValueError):
            print("wrong type")
            res = 0
        finally:
            # always append a result (float or 0)
            result.append(res)
    return result
