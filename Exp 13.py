#1.
# line_count = 0
# word_count = 0
# char_count = 0

# with open(file_path, 'r', encoding='utf-8') as f:
#     for line in f:
#         line_count += 1
#         words = line.split()
#         word_count += len(words)
#         char_count += len(line)

# print("Lines      :", line_count)
# print("Words      :", word_count)
# print("Characters :", char_count)


#2.
# lines_list = []
# with open(file_path, 'r', encoding='utf-8') as f:
#     for line in f:
#         lines_list.append(line.rstrip('\n'))

# print(lines_list)


#3.
# with open(csv_path, 'r', newline='', encoding='utf-8') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

#4.
# file1 = r"D:\MU\pwp\Python-main\ict.txt"
# file2 = r"D:\MU\pwp\Python-main\ict2.txt"
# merged = r"D:\MU\pwp\Python-main\merged.txt"

# with open(file1, 'r', encoding='utf-8') as f1, \
#      open(file2, 'r', encoding='utf-8') as f2, \
#      open(merged, 'w', encoding='utf-8') as out:
#     out.write(f1.read())
#     out.write('\n')
#     out.write(f2.read())

# print("Files merged into:", merged)

# with open(merged, 'r', encoding='utf-8') as f:
#     print("\nMerged file content:\n")
#     print(f.read())
