from collections import Counter

def main():
    print("")
    elf={}
    fatty_elf=0
    calories=0
    total={}
    top3_calories=0

    input = open("day1_input", "r")
    elf_data = input.readlines()

    for calorie_line in elf_data:

        if calorie_line == "\n":
            fatty_elf += 1
            elf["fatty_elf"] = fatty_elf
            elf["calories"] = calories
            total.update({elf["fatty_elf"]:elf["calories"]})
            calories = 0
   #         print("Elf ", elf["fatty_elf"], "Calories: ", elf["calories"])
        else:
            calories += int(calorie_line)
    print(dict(sorted(total.items(), key=lambda item: item[1])))

    top_3 = Counter(total).most_common(3)

    for i, v in enumerate(top_3):
        top3_calories += v[1]
        #print(v[1], type(v))
    print("Top 3 calories: ", top3_calories)

if __name__ == "__main__":
    main()
