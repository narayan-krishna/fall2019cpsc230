# dictionary = {'Andy': 12345, 'Bob': 98765, 'Chuck': 10000}
#
# print(dictionary['Bob'])
#
# for key,value in dictionary.items():
#     if value == 10000:
#         print(key)
#
# dictionary["Dave"] = 577775
#
# print(dictionary.items())

def count_letters(string):
    dictionary = {}
    for x in string:
        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1
    return dictionary

print(count_letters("the quick brown fox jumps over the lazy dog").items())
