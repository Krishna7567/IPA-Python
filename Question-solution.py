# Name str
# Language str
# City str
# Rating int

# questions=-- if name user have greater rating then input and english subject then print the name of the user.


# sample inputs:

# 4
# Amit
# Bhopal
# English
# 45
# Ashish
# Patna
# Hindi
# 34
# Anant
# Bhopal
# English
# 35
# Abhishek
# India
# English
# 10
# 12 - input for condition


namelist = []
langlist = []
ratinglist = []

n = int(input())
for i in range(n):
    name = input()
    city = input()
    lang = input()
    rating = int(input())
    namelist.append(name)
    langlist.append(lang.lower())
    ratinglist.append(rating)

inp = int(input()) # input for the given conditions

ans = []   #append all the condition satisfied output

if len(namelist) != 0 or len(langlist) != 0 or len(ratinglist) != 0:
    for kk in range(len(namelist)):
        if ratinglist[kk] >= inp and langlist[kk] == "english":
            ans.append(namelist[kk])

if len(ans) != 0:
    for j in range(len(ans)):
        print(ans[j])
else:
    print("No Name Found")
