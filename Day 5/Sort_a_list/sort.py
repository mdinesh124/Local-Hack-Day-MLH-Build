#Writa a script to sort a list

l = input("Enter a list of numbers separated by commas").split(',')
sorted_list = sorted(l)
print("The sorted list is:-",sorted_list)


                    #OR
                    
l = input("Enter a list of numbers separated by commas").split(',')
l.sort()
print("The sorted list is:-",l)
