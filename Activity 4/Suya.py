sampleText1 = "My name is {}. I love {}. I love playing {}. {}"
sampleText1a = sampleText1.format("Christian", "Ice Cream", "Volleyball" , "Strawberry")

print(sampleText1a)

sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("Volleyball", "Ice Cream", "Volleyball", "Straw berry")
print(sampleText2a)

sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(play="Volleyball", name="Christian",food="Ice Cream")
print(sampleText3a)
