with open('file1.txt') as f1:
    lines_1 = [line[:-1] for line in f1]
    print(lines_1)

with open('file2.txt') as f2:
    lines_2 = [line[:-1] for line in f2]
    print(lines_2)

result = [number for number in (lines_1 and lines_2)
          if number in lines_1 and number in lines_2]

print(result)

# Dictionary comprehension
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result_dict = {word: len(word) for word in sentence.split()}
print(result_dict)





