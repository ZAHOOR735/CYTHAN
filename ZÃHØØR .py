import os 
from os import system as c
import marshal
try:
    from Cython.Build.BuildExecutable import build as executa
except:
    print("pip install cython >/dev/null")
logo = (f"""
\033[0;92m                                                   
\033[1;91m _______  _______           _______  _______  _______   
\033[1;92m/ ___   )(  ___  )|\     /|(  ___  )(  ___  )(  ____ ) 
\033[1;93m/    )  || (   ) || )   ( || (   ) || (   ) || (    )|  
\033[1;94m    /   )| (___) || (___) || |   | || |   | || (____)|  
\033[1;95m   /   / |  ___  ||  ___  || |   | || |   | ||     __)  
\033[1;96m  /   /  | (   ) || (   ) || |   | || |   | || (\ (     
\033[1;32m /   (_/\| )   ( || )   ( || (___) || (___) || ) \ \__  
\033[1;31m(_______/|/     \||/     \|(_______)(_______)|/   \__/  
\033[1;37m ----------------------------------------------
\033[1;97m[\033[1;91m•\033[1;97m] TOOL ONWER  \033[1;91m: \033[1;96m  KHØSØ ZAHOOR 
\033[1;97m[\033[1;91m•\033[1;96m] TOOL NAME   \033[1;91m:  \033[1;93m ZAHOOR AHMED 
\033[1;97m[\033[1;91m•\033[1;97m] STATUS      \033[1;91m:  \033[1;97m FREE,😎
\033[1;97m[\033[1;91m•\033[1;94m] BROTHER     \033[1;94m:  \033[1;94m KHØSØ IMRAN 🇵🇰🤍
\033[1;97m[\033[1;91m•\033[1;96m] TOOL TYPE     \033[1;91m: \033[1;92m CYTHAN+MARSHALA.💕
\033[1;37m ----------------------------------------------""") 
os.system('espeak -a 600 " Welcome To ZAHOOR CYTHAN TOOLS,"')
def clear():
    c("clear")
    print(logo)
def main():
    clear()
    print("----------------------------------------")
    print(" [1] Marshal enc")
    print(" [2] Cython Executable ")
    print(" [0] exit Terminal ")
    print("----------------------------------------")
    option=input("Choice : ")
    if option in["01","1"]:
        marshal_enc()
    elif option =="2":
        cython()
    if option in["00","0"]:
        exit()
    else:
        exit("Select veiled option")
def marshal_enc():
    clear()
    file=input("Enter File Name : ")
    filex=input("output File Name : ")
    try:
        file_open=open(file,'r').read()
    except:
        exit("File Not Found")
    compilex=compile(file_open,'dg','exec')
    dump=marshal.dumps(compilex)
    run_code=f'import marshal \nexec(marshal.loads({dump}))'
    out_put=open(filex,'w')
    out_put.write(run_code)
    out_put.close()
    print("----------------------------------------")
    print(" Enc Compiled ")
    print(" out put file save :"+filex)
    print("----------------------------------------")
#------cython enc---------#
def cython():
    clear()
    file = input(" Enter Your File : ")
    try:
        filex=open(file,'r').read()
    except:
        exit(" File Not Found Error")
    error=filex.replace('    ','    ') 
    slove=open(file,'w').write(error)
    executa(file)
    clear()
    print(" Cython Executable Done ")
    save = file[:-3]
    print(" Cython file Save as : "+save)
main()