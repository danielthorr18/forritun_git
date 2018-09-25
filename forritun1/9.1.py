input_file = open("test.txt", "r")
strengur = ""
for text in input_file:
    strengur += text.strip().replace(" ", "")
print(strengur)

input_file.close()