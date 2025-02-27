import numpy as np

image = np.random.randint(0, 255, size=(256, 256))

with open("../test_nvm.mem", 'w') as f:
    f.write("""// memory data file (do not edit the following line - required for mem load use)
// instance=/nvm1/ram
// format=mti addressradix=d dataradix=d version=1.0 wordsperline=1\n""")
    for i in range(256):
        for j in range(256):
            f.write(str(i * 256 + j) + ": ")
            f.write(str(image[i, j]))
            f.write('\n')

position = int(input("inter el index ya mo7trm\n"))

row = int(position / 256)
column = position - row * 256

print(row, column)

block = image[row:row + 16, column:column + 16]

with open("block", 'w') as f:
    for i in range(16):
        for j in range(16):
            f.write(str(block[i, j]))
            f.write('\n')

padded = np.lib.pad(block, ((1, 1), (1, 1)), 'constant', constant_values=((0, 0), (0, 0)))

with open("padded", 'w') as f:
    for i in range(18):
        for j in range(18):
            f.write(str(padded[i, j]))
            f.write('\n')

total = 0

for i in range(1, 17):
    for j in range(1, 17):
        total += abs(padded[i, j] - padded[i - 1, j])
        total += abs(padded[i, j] - padded[i + 1, j])
        total += abs(padded[i, j] - padded[i, j - 1])
        total += abs(padded[i, j] - padded[i, j + 1])

print("total= ", total)
