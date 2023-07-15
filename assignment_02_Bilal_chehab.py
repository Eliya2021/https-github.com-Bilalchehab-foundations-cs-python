def choiceMenue():
  print("the The choices are:\n" + 
        "1-Count Digits\n " +
        "2-Find Max\n" +
        "3-Count Tags\n" +
        "4-Exit\n") 




  print("--------------------")

  choice = input("please choose one of the following choices to proceed")

  while (not choice.isnumeric()):
    choice = input("please enter a     numeric choice")

  choice = int(choice)
  
  while (choice > 4):
    choice = input("please enter one of the choices")

  while  (choice < 1):
    choice = input("please enter one of the choices")

  

  

#-----------------------




  def choice1(n):

    
   
    if (n==0):
      return 0 

    else: 
      return 1 + choice1(n // 10)

    print(choice1(n))



#########################
# choice 2 
##########################

 
  
  def choice2(my_list,max):
    print(my_list)
    for a in range(my_list[a]):
      max = a
       
    if len(my_list)== 0 :
      return max

    else:
        if my_list[0] > max:
          return choice2(my_list[1:], my_list[0])

        else:
          return choice2(my_list[1:],max)

    
  
    


#############################

  if choice == 1 :
    n = int(input("please enter any integer you want"))
    choice1(n)
    print(choice1(n))
      
  elif choice == 2 :
    input2 = input("Enter a list of values (comma-separated): ")

    input_list = input2.split(",")
 
    my_list = [int(item) for item in input_list]

    
    for a in range(my_list[a]):
      max = a
    
    
    choice2(my_list,max)
    print(choice2(my_list,max))
    



choiceMenue()





