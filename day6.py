'''vowel_con = input("Enter a letter:")
if vowel_con in "AEIOUaeiou":
    print("Vowel")
else:
    print("con")'''

'''Time_aday = input("Enter 24hours time: ")
parts_ = Time_aday.split(":")
print(parts_)
hours_ = int(parts_[0])
Min_ = int(parts_[1])
print(hours_)
print(Min_)
if hours_ >=13 and Min_ < 60:
    print(f"{Time_aday} convert into {hours_-12} :{Min_}pm")
else:
    print(f" you have entered nrml or min are incorrect")'''

#List ---> collection of different items inside the [] , which are seperated by (,)
#4eg: [1,"Name",[1,2,"Chinni"]]

List_1 = [1,2,3,"python",[1,2,["python","java"],"Language"]]
print(List_1[4][2][0][3])

List_2 = [1,2,3,4,5,"Chinni",[1,2,3,["Honey","Bujji"],"Name"]]
print(List_2[6][3][1][0])

#Methods of list
#---------------
#append()--> this method is used to add new items into list, it will only go for the last index of the
#list
#syntax--->variable_name.append(item)            #only one item
#extend()--> this method is used to add items to list in the last index,where each item or substring is
#each index in the list
#remove()--> This method will delete the items or value directly
#pop()--> This method will delete the item or value based on index position
#syntax --> variable_name.pop(index value)

#Mutable --> i can directly modify on that particular variable
#immutable --> i cannot modify directly on the particular variable


List_3 = [1,2,3,4,5]
print(List_3)
List_3.append(67)
print(List_3)
List_3.append([29,11]) #to add items with exactly same what to give for add in the list ,e.g-(1,2,3,4,[29,11])
#List_3.append(29,11) -- TypeError: list.append() takes exactly one argument (2 given)
print(List_3)
#List_3.extend(0.8)#float alone cannot be extended #TypeError: 'float' object is not iterable
#print(List_3)
List_3.extend([0.8]) #float alone cannot be extended bcz within list give the values
print(List_3)
List_3.extend([1,0.8])          
print(List_3)
List_4 = [23,56,89]
List_4.extend("Chinni")  #seperates every item even if its a string, list
List_4.append("Chinni")
print(List_4)
List_5 = [23,56,7]
List_0 = List_5.extend("Bujji")
print(List_0)

List_6 = [23,85,56,6,9,89,90,85,"Bujji",85]
List_6.remove(85)
print(List_6)

List_7 = [23,"python",56,89,6] # index position start with 0
List_7.pop(1)
print(List_7)
