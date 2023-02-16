name = input('Type your name: ')
print('Welcome', name, 'to this adventure!!!')
print('Find the gold to win!')

answer = input('It is dark. You are on a dirt road. The road comes to an end. Do you want to go left or right?: ').lower()

if answer == 'left':
  print('You go left.')
  answer = input('You come to a river. You can walk a little bit and cross over a wooden bridge some meters ahead, or you can swim through it and cross it faster. Type "walk" to go to the bridge or "swim" to swim through the river: ').lower()

  if answer == 'walk':
    print('You decide to walk for some meters and move safely over the bridge')
    answer = input('However, a bear starts chasing you! You run and reach an old mine. Do you enter it?: ').lower()

    if answer == 'yes':
     print('You enter the mine')
     answer = input('It is very dark but you have a flashlight. You can go up or down in the mine. Which path do you choose?: ').lower()
      
     if answer == 'up': 
      answer = input('After walking a lot, you reach some rubble. You dig up a suspicious chest. Do you open it or prefer to leave, since it seems a trap to you(yes/no)?: ').lower()
       
      if answer == 'yes':
        print('You find the gold!!! YOU WIN!')
        print('Thank you for playing ', name)
        quit()
        
      elif answer == 'no':
       print('You go back. After walking for many hours, you realise that you are completely lost. You lose')
       print('Thank you for playing ', name)
       quit()

      else:
       print('Not a valid option. You lose.')
       quit()
    
      
     elif answer == 'down':
      print('After walking for many hours, you realise that you are completely lost. You lose')
      print('Thank you for playing ', name)
      quit()

     else:
      print('Not a valid option. You lose.')
      quit()
    
        
    elif answer == 'no':  
      print('Unfortunately, you become the bear\'s meal. You lose.')
      print('Thank you for playing ', name)
      quit()
      
    else:
      print('Not a valid option. You lose.')
      quit()
    
    
  elif answer == 'swim':
    print('There was a crocodile in the water that didn\'t miss on the opportunity for a good lunch. You lose.')
    print('Thank you for playing ', name)
    quit()
    
  else:
    print('Not a valid option. You lose.')
    quit()
    

elif answer == 'right':
  print('You go right.')
  answer = input('You keep on walking and you enter a dark forest. You find a house that seems haunted to you. Do you enter it?: ').lower()

  if answer == 'yes':
      print('You investigate the house but you hear many weird sounds. You are starting to think that it is indeed ghosts and at the end you collapse, ovecome by fear. You lose')
      print('Thank you for playing ', name)
      quit()

  elif answer == 'no':
   answer = input('You keep on exploring the forest but you hear a pack of wolves in a short distance. You find a cave. Do you enter it, to avoid the wolves?: ').lower()
    
   if answer == 'yes':
    print('You enter the cave just to discover that it is an angry bear\'s house! You lose.')
    print('Thank you for playing ', name)
    quit()
  
   elif answer == 'no':
    answer = input('You don\'t enter the cave. However, a bear starts chasing you! You run and reach an old mine. Do you enter it?: ').lower()
      
    if answer == 'yes':
      print('You enter the mine')
      answer = input('It is very dark but you have a flashlight. You can go up or down in the mine. Which path do you choose?: ').lower()
      
      if answer == 'up': 
        answer = input('After walking a lot, you reach some rubble. You dig up a suspicious chest. Do you open it or prefer to leave, since it seems a trap to you(yes/no)?: ').lower()
       
        if answer == 'yes':
          print('You find the gold!!! YOU WIN!')
          print('Thank you for playing ', name)
          quit()
        
        elif answer == 'no':
          print('You go back. After walking for many hours, you realise that you are completely lost. You lose')
          print('Thank you for playing ', name)
          quit()
    
        else:
         print('Not a valid option. You lose.')
         quit()
    
      
      elif answer == 'down':
        print('After walking for many hours, you realise that you are completely lost. You lose')
        print('Thank you for playing ', name)
        quit()
  
   
      else:
        print('Not a valid option. You lose.')
        quit()

  
else:
  print('Not a valid option. You lose.')
  quit()
  