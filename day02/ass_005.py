big_str = "The Python Software Foundation is the organization behind Python. Become a member of the PSF and help advance the software and our mission."

strs = big_str.split()

for s in strs:
    print(s)

print(big_str[56:87])
print(big_str[21:187:2])
print(len(strs))