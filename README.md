This program is used to store your application passwords along with the name of the application and the username. 
It uses the cryptography module in order to encrypt the passwords in the txt file. After which a key is defined by which the string of text which is inputted is changed into encrypted form. 
It also has a master password which works in harmony with the key in encryption, so when the wrong master password is typed, the list of passwords and usernames cannot be accessed and the text will be decrypted wrongly. \
write_key() is used to create said key, which is run 1 time to create the key file.
load_key() is used to retrieve the key. 
view() is defined to view the exsisting passwords and add() is used to add new passwords. 
