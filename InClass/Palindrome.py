import string

def clean(input_string):
    word = input_string
    for x in (string.punctuation + string.whitespace):
        word = word.replace(x,"")
    return word.upper()

def palindrome_check(input_string):
    if input_string == input_string[::-1]:
        print("yes, palindrome")
    else:
        print("no, not palindrome")

def palidrome_main():
    str_input = input("input supposed palindrome: ")
    str_clean = clean(str_input)
    print(str_clean)
    palindrome_check(str_clean)

palidrome_main()

this_is_input = input("enter input")
