def sort_string(first_string, second_string):
    len_str = len(first_string)
    print(len_str)
    i = 0
    while i < len_str:
        sim = first_string[i]
        if sim != second_string:
            print(sim)
        i += 1


sort_string('hellow', 'l')
