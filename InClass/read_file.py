def altLine (file1, file2)
    input_file = open(file1)
    counter = 0
    for line in input_file:
        if (counter + 1) % 2 != 0:
            print(line)
        counter += 1

    input_file.close()
