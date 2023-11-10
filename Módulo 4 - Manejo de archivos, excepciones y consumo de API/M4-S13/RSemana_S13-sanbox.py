
# initializing string
test_str = 'geeks4geeks'
 
print("The original string is : " + str(test_str))
 
# using any() to check for any occurrence
digitl_valid = any(chr.isdigit() for chr in test_str)
 
print(digitl_valid)

#print("Does string contain any digit ? : " + str(res))