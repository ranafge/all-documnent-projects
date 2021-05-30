def count_lines(file_name):
    """ Count the number of lines in a file.
    """
    try:
        return len(open(file_name, 'r').readlines())
    except IOError:
        return 0


my_file = input('Enter file name ')
print(count_lines(my_file))
