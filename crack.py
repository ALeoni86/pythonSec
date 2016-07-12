import crypt

def testPass(cryptPass):
    salt = cryptPass[0:6]
    dictFile = open('dictionary.txt','r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        print salt
        print cryptPass
        print cryptWord
        if (cryptWord == cryptPass):
            print "[+] Found Password: "+ word +"\n"
            return
    print "[-] Password Not Found.\n"

def main():
    passFile = open('passwords.txt','r')
    for line in passFile.readlines():
        if ":" in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print "[+] Cracking Password For: "+user
            testPass(cryptPass)

if __name__ == "__main__":
    main()