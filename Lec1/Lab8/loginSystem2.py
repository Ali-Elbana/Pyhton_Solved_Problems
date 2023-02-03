import os

os.system('cls')

print()
# Write your code here:


# Is a database for the users names and passwords:
users_database = {  1: { 'name': 'Ahmed', 'pass': 1394 },
                  
                    2: { 'name': 'Ali'  , 'pass': 6078 },
                    
                    3: { 'name': 'Amr'  , 'pass': 9345 }
                }
 
# Is a flag to detect the right username index in the database:
names_flag = False

# Is a flag to detect the right password index in the database:
pass_flag  = False 

# Is a counter for the number of tries of the incorrect entered names:
name_tries : int = 0

# Is a counter for the number of tries of the incorrect entered passwords:
pass_tries : int = 0

# Get the username from the user:
user_name = str( input( "Please enter your name: " ) )

# Loop in the database to check that's the right username:
for names in users_database :
    
    # if the username not found keep the initial value of the flag:
    if user_name not in users_database[names]['name'] :
        
        names_flag = False
    
    # if you found the username then keep the index of it on the flag and stop looping:
    else :
        
        names_flag = names
        
        break
  
# Give the user 3 more tries to enter the right name:
if  names_flag == False :
    
    while (name_tries < 2) and (names_flag == False) :
        
        print( 'Incorrect Username, please try again\n' ) 
        
        name_tries += 1
        
        # Get the username from the user:
        user_name = str( input( "Please enter your name: " ) )
        
        # Loop in the database to check that's the right username:
        for names in users_database :
            
            # if the username not found keep the initial value of the flag:
            if user_name not in users_database[names]['name'] :
                
                names_flag = False
            
            # if you found the username then keep the index of it on the flag and stop looping:
            else :
                
                names_flag = names
                
                break
    
# After you finished the searching process if the input username not found, then its an incorrect username: 
if  names_flag == False :
    
    print( 'Incorrect Username, no more tries' )     
 
 
# If the entered username is correct, then check for the enterd password:
if  names_flag != False : 
 
    # Get the password from the user:
    password = int( input( "Please enter your password: " ) )
            
    # Loop in the database to check that's the right password:                
    for passes in users_database :
        
        # if the password not found keep the initial value of the flag:
        if password != users_database[passes]['pass'] :
            
            pass_flag = False
        
        # if you found the password then keep the index of it on the flag and stop looping:
        else :
            
            pass_flag = passes
            
            break
            
    # Give the user 3 more tries to enter the right password: 
    if  pass_flag == False :
        
        while (pass_tries < 2) and (pass_flag == False) :
            
            print( 'Incorrect password, please try again\n' ) 
            
            pass_tries += 1
            
            # Get the password from the user:
            password = int( input( "Please enter your password: " ) )
            
            # Loop in the database to check that's the right password:                
            for passes in users_database :
                
                # if the password not found keep the initial value of the flag:
                if password != users_database[passes]['pass'] :
                    
                    pass_flag = False
                
                # if you found the password then keep the index of it on the flag and stop looping:
                else :
                    
                    pass_flag = passes
                    
                    break
                
    # After you finished the searching process if the input password not found, then its an incorrect password:            
    if  pass_flag == False :
    
        print( 'Incorrect Password, no more tries' )     
          
                    
    # If the user entered the right name and pass the print a welcome message:            
    else:
        
        print( f" \nWelcome { users_database[names_flag]['name'] } " ) 
            
            
# The end of your code. 
print(), print()
