name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, {name}! I am {age} years old.")

item = "lanzones"
count = 10

sentence = "I bought {} {} today.".format(count, item)
print(sentence)

city = "Dapitan"
temperature = 34
# Use the % operator
print("The temperature in %s is %d degrees Celsius." % (city, temperature))
