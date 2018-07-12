def even_number(list):

       even = 0

    for even in list:
         if (even % 2 == 0):

             even += even

        else:
            pass

    return even


print([2,4,6,8,10,12])
