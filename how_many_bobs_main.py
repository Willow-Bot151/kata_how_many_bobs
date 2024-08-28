def bob_count_func(my_string):
    bob_count = 0
    for i in range(len(my_string) - 2):
        if my_string[slice(i,i+3,1)].lower() == "bob":
            bob_count += 1
    return bob_count