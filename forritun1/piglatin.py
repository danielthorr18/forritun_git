def serhljodi(char):
    all_vowels = 'aeiouAEIOU'
    return char in all_vowels


strengur = input("Sladu inn eitthvad ord: ")
bool = serhljodi(strengur[0])

a = len(strengur)
if bool==True:
	strengur=strengur+'yay'
	print (strengur)

else:
	strengur = strengur[1:]+strengur[0]+'ay'
	print (strengur)
	
#Þetta er kóðinn