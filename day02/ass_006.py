original_str = "The purpose of this page is to outline a very easy way to get up and running with a desktop wiki. This could be useful for a number of use-cases including, an experimental wiki for newcomers, a development instance for preliminary setup, a personal organization framework, et al. The main thing to remember about this instruction, is that THERE IS NO CONSIDERATION FOR NETWORK SECURITY outside of the localhost domain on your own computer."

strs = original_str.split()

words = {}

for s in strs:
    if s not in words:
        words[s] = 1
    else:
        words[s] += 1

print(words)
