# Write a python script to determine whether a string contains a specific substring.
s=input("Enter a string : ")
c=s.count(input("Enter substring : "))
print("Yes exists!" if c>0 else "Does not exists!")
