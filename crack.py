import crypt
import click
import hashlib
from itertools import permutations,combinations_with_replacement 


def crack(cryptPass,dictFile):
    salt = cryptPass.split("$")[2]
    type_hash = cryptPass[0:3]
    print("salt is: ", salt, " " , "type_hash: " + type_hash)
    for word in dictFile.readlines():
        nospc = word.strip()
        dictWord = nospc.split(" ",1)[1]
        cryptWord = crypt.crypt(dictWord,type_hash+salt)
        print(cryptWord)
        if (cryptWord == cryptPass):
            print "[+] Found Password: "+dictWord+"\n"
            return
    print "[-] Password Not Found.\n"
    return




def permutationCrack(cryptPass,alpha):
    count = 0
    ascii = 'abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+":}|?><~'
    salt = cryptPass.split("$")[2]
    type_hash = cryptPass[0:3]
    print("salt is: ", salt, " " , "type_hash: " + type_hash)
    perms = [''.join(p) for p in combinations_with_replacement(ascii,alpha)]
    for word in perms:
        cryptWord = crypt.crypt(word,type_hash+salt)
        if (cryptWord == cryptPass):
            print "[+] Found Password: "+word+"\n"
            return
        
    print "[-] Password Not Found.\n"
    return





@click.group()
# @click.option("--tool", help = "produces an encrypted file from given text file ")
def cli():
  pass
@cli.command()
@click.argument('pwdfile', type = click.File('rb'))
@click.argument('dictionary', type = click.File('rb'))
def DictionaryCrack(pwdfile,dictionary):
    ''' 
    Read in shadow file and tries to generate password using a dictionary. The program
    reads in a password from the dictionary and generate a hash using the crypt.crypt()

    NOTE: as dictionary is quite large, It can take a while.

    Parameters:
        
        pwdFile: file of encrypted passwords (shadowfile)
        
        dictionary: file of dictionary used

    '''
    for line in pwdfile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            if cryptPass == '*':
                continue
            else:
                print("testing on" + cryptPass)
                print("[*] Cracking Password For: "+ user)
                crack(cryptPass,dictionary)



@cli.command()
@click.argument('pwdfile', type = click.File('rb'))
@click.argument('pwdlength', type = click.INT)
def permcrack(pwdfile,pwdlength):
    ''' 
    Read in shadow file and tries to generate password using a dictionary. The program
    then calculates the permutations of ascii character and generate a hash using the crypt.crypt()
    if the genreated has and matches on in file, password is found

    Parameters:
        
        pwdFile: file of encrypted passwords (shadowfile)
        
        pwdlength: persumed length of pasword

    '''
    
    for line in pwdfile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            if cryptPass == "*":
                continue
            else:
                print("testing on" + cryptPass)
                print("[*] Cracking Password For: "+ user)
                permutationCrack(cryptPass,pwdlength)

                
if __name__ == '__main__':
    cli()
