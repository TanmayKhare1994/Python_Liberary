# Describing Looping Scenario
Continents=["Asia","Africa","Atlantic","Arctic","North America","South America"]
counter =0
max_index=len(Continents)-1
while counter<=max_index:
    print Continents[counter];
    counter+=1;


# Using For loop getting the things done easily
for items in Continents:
    print items

for numbers in range(0,10,2):
    for numbers1 in range(0,2):
        print numbers1;
       # print "\n";
    print numbers;