import  re

#only the word starts from starting it will take example below
pattern = r"sp" #it will accept
pattern1= r"spam" #it will accept
pattern2 = r"pamspam" #it will not accept becuase word starting from p.

if(re.match(pattern,"spamspamspam")):
    print ("MAtched")
else:
    print ("Not Matched")