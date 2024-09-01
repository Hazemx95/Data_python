filename = 'titles_names.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print(list(lines))
    for line in lines:
        print(line.rstrip())

        
