import time

my_list = range(999999)
a = time.time()
result = []

for number in my_list:
    result.append(str(number))

final_result = ''.join(result)
print(final_result)

b = time.time()

print("Temps d'execution: {}".format(b - a))


