

# open("text_sample.txt", "r+") # read and write
# open("text_sample.txt", "w") # write
# open("text_sample.txt", "a") # append

# print(text_sample.read())
# print(text_sample.readable())
# print(text_sample.readline())
text_sample = open("text_sample.txt", "r") # read
for line in text_sample.readlines():
  print(line)
# print(text_sample.readlines()[1])
text_sample.close()


