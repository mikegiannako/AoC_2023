from parsing import *
import re

# Problem link: https://adventofcode.com/2023/day/1/input

def part1():
    # The total sum of the numbers
    count : int = 0

    data : list[str] = rdln()

    # Each line consists of strings that contain letters and numbers.
    # We want to extract the numbers and convert them to integers.
    for line in data:
        # We use regex to find all numbers in the string
        numbers : list[str] = re.findall(r'\d+', line)

        # We merge the first digit of the first number with the last digit of the last number (could be the same number)
        count += int(numbers[0][0]+numbers[-1][-1])
    
    return count

def part2():
    count = 0

    data = rdln()

    # This time we want to also take into consideration the words that represent digits as well.
    # The reason why the dictionary values are not just the digits is because there where cases where
    # this would happen "twone" would be replace by "tw1" if the dictionary value was 1. This is because
    # in the for loop below we use "for word in text_to_num" and it would always find "one" first.
    # 
    # So the problem is that this case ("twone") should be replace by "21" and not "tw1" or "2ne".
    # That's why we use the following dictionary. So when replacing the words with numbers, we keep the
    # first and last letter of the word and replace the rest with the number in case there where other
    # digits as words that used one of these letters.
    text_to_num = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e",
                    "six" : "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
    
    for line in data:
        # We replace the words with numbers
        for word in text_to_num:
            line = line.replace(word, text_to_num[word])

        # We use regex to find all numbers in the string
        numbers : list[str] = re.findall(r'\d+', line)

        # We merge the first digit of the first number with the last digit of the last number (could be the same number)
        count += int(numbers[0][0]+numbers[-1][-1])
    
    return count

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
