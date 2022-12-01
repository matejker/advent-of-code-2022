def calories(file="input.txt"):
    elf_calories = [0]
    max_calories = 0
    with open(file) as f:
        for line in f.readlines():
            if line == "\n":
                max_calories = max(max_calories, elf_calories[-1])
                elf_calories.append(0)
            else:
                elf_calories[-1] = elf_calories[-1] + int(line.strip("\n"))

    elf_calories.sort(reverse=True)
    return max_calories, sum(elf_calories[:3])


assert calories("test.txt") == (24000, 45000)
print("Most caloric Elf %d, Sum of top 3 %d" % calories())
