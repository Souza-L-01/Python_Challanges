friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
lucky_numbers = [4, 8, 15, 16, 23, 42]

# friends.extend(lucky_numbers) #add the lucky_numbers list to the friends list
friends.append("Creed") #add an element to the end of the list
friends.insert(1, "Kelly") #add an element to the list in a specific position
friends.remove("Jim") #remove an element from the list
friends.pop() #remove the last element from the list
friends.sort() #sort the list
friends.reverse() #reverse the list
# friends.clear() #clear the list
friends2 = friends.copy() #copy the list
print(friends2)

print
print(friends.index("Kevin")) #print the index of the element
print(friends.count("Jim")) #print the number of times the element appears in the list
print(friends)
print(friends[0])
print(friends[1])
print(friends[1:3]) #modify the range of the list
print(friends[1:]) #print from 1 to the end