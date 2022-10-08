# Write a python script to reverse a String. (“iNeuron”).
s,s1=" ","iNeuron"
l=len("iNeuron")-1
while(l>=0):
    s=s+s1[l]
    l=l-1
print(s)