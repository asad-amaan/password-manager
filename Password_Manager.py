#Encrypting the passwords using the Cryptography package and Fernet Module. 

from  cryptography.fernet import Fernet
#Function to open key file. Used only once. 
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)'''



#Function for encrypting. 
def load_key():
    #Opening file in read bytes mode. 
    file = open("key.key", "rb") 
    key = file.read()
    file.close()
    return key

#Master Password. 
m_pwd = input("Please enter the master password : ")

key = load_key() + m_pwd.encode()
fer = Fernet(key) 


#Function for adding passwords.
def add():
    app = input("Enter the Application Name : ")
    name = input("Enter the  username : ")
    pwd = input("Enter the Password : ")
    
    #Opening a file to store the App, username and passwords in append mode. 
    with open('passwords.txt', 'a') as f: 
        f.write( app + "|" + name + '|' + fer.encrypt(pwd.encode()).decode() + "\n")

#Function for viewing passwords.
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            #r.strip deletes extra line that is added in line 11 
            data = line.rstrip()
            #Printing the app name, account name and pw without pipe. 
            app, user, pwdd = data.split("|")
            print("Application Name : ", app, "Username : ",user, "Password: ", fer.decrypt(pwdd.encode()).decode())
            




while True: 
    #Checking if user wants to view or add password. 
    mode = input("Do you want to add a new password or view exsisting password? (Add/View) or Q to quit : ").lower()
      
    if mode == "q":
        break 
    
    if mode == "view":
        view()
    elif mode == "add":
        add() 
    else:
        print("Invalid mode. Please try again. ")
        continue 