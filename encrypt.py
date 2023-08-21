import random
#colors
RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'   

#### file modes #####
r, w, a = 'r','w','a'

print()
print(BLUE + '*'  * 50)
print(GREEN + '*'  * 16+ ' VENTRICK 💻 ' + GREEN + '*' * 22)
print(BLUE + '*'  * 50)
print('')

def main():
   global option
   ## selecting options , Encrypt or decrypt
   #def select():
   print()
   global select_mode
   select_mode = int(input(f"{WHITE}  ENTER {GREEN}1 {WHITE}TO ENCRYPT || {GREEN}2 {WHITE}TO DECRYPT{WHITE}: "))
      
   #select()
   
   ## All characters,numbers and symbols
   alpha_letters = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%&-+(~`|•√Π÷×/=:;©._®™℅[*"\')[?!]\n'

   
   ## a copy of Alpha_letters but shuffled  #
   key = ['N', 'g', ' ', '[','.' ,'H', '5', 'I', 'f', 'M', ')', '?', '3', 'D', '∄1�7', 'T', '9', 'z', 'q', '-', 'o', 'c', 'G', 'p', '|', 'Π', 'e', '=', ']', '*', 's', '@', 'W', "'", 'v', 'Q', 'a', '7', ' 1�7', '©', 'A', '6', 'Z', 'b', '2', 'J','_', 'l', 'V', 'P', '(', '÷', '"', 'd', 'B', 'Y', 'X', 'r', 'E', 'K', ';','U', '/','1', '!', 'C', '℄1�7', '+', 'j', '®', '×', '0', 'x', '%', 't', '$', '℄1�7', '4', 'S', 'h', '&', 'O', 'k', '#', 'i', '`', 'u', '[', 'F', 'm', 'n',':','~', 'L', 'y', 'R', 'w','8','\n' ]
   
   
   #shufled_letters = alpha_letters.copy()
  # random.shuffle(shuffled_letters)
     
   #print(alpha_letters)
   #print(shuffled_letters)
   
   
   
   
   ### creating a dictionary for the encrypting text ###
   def encrypt():
      
      ## input file path for Encrypting ##
      print()
      inp= input(f"  2: Enter {GREEN}File Path {WHITE}To {GREEN}Encrypt {WHITE}: ")
      #Assining inp to file_path
      file_path = inp 
      print()
      
      #### starting of the file request ###
      def filess():
         #path = 'check.txt'
         with open (file_path, r) as read_file:
            file = read_file.read()
            print(file)
            print(len(file))
         encrypted_text = ''
         for i in file:
             if (i in alpha_letters):
                index = alpha_letters.index(i)
                encrypted_text += key[index]
         print ( )  
         print("👉ENCRYPTED TEXT:👇👇👇👇👇👇" )
         print(BLUE +'*' * 50)
         print("")
         print(f"  {GREEN} {encrypted_text}" )
         print('')
         print(BLUE +'*' * 50)
         print('')
         print(f"👉 {WHITE}NUMBER OF CHARACTERS:{GREEN} {len(encrypted_text)}")
      filess()
      
   # NOTE THAT The encrypt() function will be called when the user selects encryption mode by a prompt 
      
      
      
       ## Creating a Dictionary for decrypting   text  ##
   def  decrypt():
      print()
      inp= input(f"  2: Enter {GREEN}File Path {WHITE}To {GREEN}Decrypt {WHITE}: ")
      #Assining inp to file_path
      file_path = inp 
      print()
      
      def filess2():
         #path = 'check.txt'
         with open (file_path, r) as read_file2:
            file2 = read_file2.read()
            print(file2)
            print(len(file2))
         decrypted_text = ''
         for i in file2:
             if (i in key):
                index = key.index(i)
                decrypted_text += alpha_letters[index]
         print ( )  
         print("👉DECRYPTED TEXT:👇👇👇👇👇👇" )
         print(BLUE +'*' * 50)
         print("")
         print(f"        {GREEN} {decrypted_text}" )
         print('')
         print(BLUE +'*' * 50)
         print('')
         print(f"👉 {WHITE}NUMBER OF CHARACTERS:{GREEN} {len(decrypted_text)}")
      filess2()
   
   
   ###... For user selection between encrypting or decrypting.... ###
   
   
   if (select_mode == 1):
         encrypt()
   
   elif (select_mode == 2):
         decrypt()
   elif (select_mode != 1 or select_mode != 2):
      print()
      print(RED + '  please enter a valid option ‼️‼️')
      
      
   #print (type(select_mode))
   #def go_back():
   print('')
   global back_option
   def back_option():
      global back
      back = input(f'{WHITE}  ENTER {GREEN}1 {WHITE}TO GO BACK TO {GREEN}MENU {WHITE}: ')
      #go_back()
      return back
   back_option()   

main()

def statement():
   
  # print(RED +'only numbers are allowed')
   while True:
       if (back == '1'):
        main()
        print()
       elif (back != '1'):
          print()
          print(RED + '  please enter a valid option ‼️‼️')     
          print()
          back_option()
statement()