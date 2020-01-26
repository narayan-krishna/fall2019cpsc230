user_str = "zombie attack"

sub_str3 = user_str[-6:]

out = ""
for x in range(4):
    add = sub_str3 + ","
    out = out + add

print(out)
