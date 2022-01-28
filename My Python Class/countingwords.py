a = input("Enter Your Introdution : ")
print(a)
character_count = 0
word_count = 1
for i in a:
    character_count+=1
    if(i == ''):
        word_count+=1
    print("Number Of Words In The String ")
    print(word_count)
    print(character_count)
    
