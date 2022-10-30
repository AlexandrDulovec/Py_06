print("Test hesla:")
password = input();
import re
h = True
while h:
    if not re.search("[a-z]",password):
        print ("Aby heslo splňovalo daná specifika musí obsahovat nejméně jedno malé písmeno [a-z].")
        break 
    elif not re.search("[A-Z]",password):
        print ("Aby heslo splňovalo daná specifika musí obsahovat nejméně jedno malé písmeno [a-z].")
        break
    elif not re.search("[0-9]",password):
        print ("Aby heslo splňovalo daná specifika musí obsahovat nejméně jednu číslici [0-9].")
        break
    elif not re.search("[$#@]",password):
        print ("Aby heslo splňovalo daná specifika musí obsahovat jeden znak [$#@].")
        break
    elif (len(password)<6 or len(password)>16):
        print ("Aby heslo splňovalo daná specifika musí obsahovat nejméně 6 znaků a nejvíce 16 znaků")
        break
    else:
        print("Heslo splňuje všechny daná specifika");
        h = False
        break;