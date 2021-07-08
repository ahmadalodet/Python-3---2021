import random;

def play():
    
 # 1-user intput
 user_input = input("""Please choose your hand
     S for stone
     P for paper
     SC for scissors""");



 # 2-computer input

 choises = ["S","P","SC"];
 computer_input = random.choices(choises);


 def is_winner(ui, ci):
     if(ui == 'S' and ci == 'P') or (ui == 'P' and ci == 'S')or (ui == 'S' and ci == 'SC'):
             return True
             return False;
     
     
 user_input = input("""Please choose your hand
     S for stone
     P for paper
     SC for scissors""");


 x = is_winner(user_input, computer_input);
 if(x):
        print("you win , waw");
 else:
        print("try again");
        


 # 3-logic compare the winner and the losser

 # 4- notify
while(True):

         play();










