s1 = "mit u rock"
s2 = "i rule mit"
count = 0
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                count += 1
                break

print(count)
