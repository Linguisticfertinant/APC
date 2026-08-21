def count_lines():
    f = open("story.txt", "r")
    total = 0
    count = 0
    for line in f:
        total += 1
        if not line.startswith("T"):
            count += 1
    f.close()
    print("Total number of lines:", total)
    print("Lines not starting with T:", count)

count_lines()