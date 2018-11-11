text = 'Sample text to Save \nNew Line'
saveFiles = open('exampleFile.txt', 'w')  # 'a' for append text

# Write information

saveFiles.write(text)

# Finally close the file

saveFiles.close()

readMe = open('exampleFile.txt', 'r').readlines()
print(readMe)


