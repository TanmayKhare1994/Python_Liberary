ages ={"Akhilesh":12,"Rama":23,"Tenali":21}

for items in ages:
    print items,ages[items]

primary = {
    "Red":[0,255,0],
    "Blue":[255,0,0],
    "Green":[0,0,255]
    }

print primary["Red"]

# list cannot be key of dictonarry only immutable objects are eligible for keys.
bad_dict = {[1,2,3]:"one two three"} #thows and error