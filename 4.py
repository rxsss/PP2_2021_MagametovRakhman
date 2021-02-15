#creating variables
x = 111
a = "rxsss"

print(x)
print(a)


#Variables do not need to be declared with any particular type, and can even change type after they have been set.
b = 5
b = "b is now - string"
print(b)

#casting variables

d = str(3) #'3'
e = int(3.2) #3
f = float(3) #3.0
print(d, e, f)

#type of variable
print(type(d), type(e), type(f))


# ' same as ". "John" = 'John'

#case-sensitivity

O = "100"
o = 200

if o != O:
    print("case-sensitivity. O not equal to o")