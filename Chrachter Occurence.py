s=(input("Enter a word: "))
char=(input("Enter a character to find its occurrence: "))
i=0
count=0
while i<len(s):
 if s[i]==char:
  count=count+1
 i=i+1
print("The occurrence of",char,"in", "is:",count)
