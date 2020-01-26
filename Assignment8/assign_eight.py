def processed_line(raw_line):
    line = raw_line.strip()
    line_list = line.split()
    name = ' '.join(line_list[0:2])
    return [name,line_list[2],line_list[3]]

def courses_dictionary(file_name):
    dictionary = {}
    input_file = open(file_name, 'r') #open up the file
    for x in input_file: #for lines in the file,
        processed = processed_line(x)
        current_courses = processed[2].split(",")
        for x in current_courses:
            if x in dictionary: #if the word is already in the dictionary,
                dictionary[x] += processed[0] + "," #add 1 to the occurence value
            else:
                dictionary[x] = processed[0] + ","
        # dictionary[current_list[2]] = current_list[0]
    input_file.close() #close the file
    return(dictionary)
#
print(courses_dictionary("student_records"))
