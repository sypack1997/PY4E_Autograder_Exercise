# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
name = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    # print(line)
    num = line[20:]
    name = name + float(num)
    # print(name)
# print("Done", count)
print("Average spam confidence:", name/count)
