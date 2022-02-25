file2Open = open("testingWhatIdontKnow.txt", "w")

file2Open.write('ten')



newFile = open("createdFileByMe.txt", "w+")

for i in range(20):
    newFile.write(f"This is line {i} in this document\n")
    file2Open.write('ten\n')

newFile.close()
file2Open.close()
