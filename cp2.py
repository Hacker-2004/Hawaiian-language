dictnary={"a":"ah","e":"eh","i":"ee","o":"oh","u":"oo"}
dict_2 = {"ai" : "eye", "ae" : "eye", "ao": "ow", "au" : "ow", "ei" : "ay", "eu" : "eh-oo-", "iu" : "ew-",
              "oi" : "oyo", "ou" : "ow","ui" : "ooey"}
def hawaina():
    userin=input("Enter words to translate into Hawaiian Words =>")
    words=userin.lower()
    char=["a","e","i","o","u","p","k","h","l","m","n","w"]
    ws=""
    num=0
    truech=0
    for i in range(len(words)):
        if(words[i]=="a" or words[i]=="e" or words[i]=="i" or words[i]=="o" or words[i]=="u" or
           words[i]=="p" or words[i]=="k" or words[i]=="h" or words[i]=="l" or words[i]=="m" or
           words[i]=="n" or words[i]=="w" or words[i]==" " or words[i]=="'"):
        
            num+=1
        else:
            ws=ws+words[i]
    if(num!=len(words)):
        print(ws,"Invalid Char")
        hawaina()
    else:
        return dictnaryy(words)
def check():
    check=input("Do you want to go again type Y/YES/N/NO =>")
    if(check=="YES" or check=="Y" or check=="N" or check=="No"):
        if(check=="YES" or check=="Y"):
            hawaina()
        else:
            return
    else:
        print("Enter Y, YES,N or NO")
        recheck()
    return
def recheck():
    check()
        
def dictnaryy(userin):
    word=userin.lower()
    output=""
    index=0
    while index< len(word):
        pair=word[index]
        pairs=word[index:index+2]
        if pairs in dict_2:
            if(pairs in dict_2 and word[index+2:index+3] in dictnary):
                if(word[index+4:index+5]==" " or word[index+4:index+5]=="'"):
                    output=output+dict_2[pairs]+"-"
                    output=output+dictnary[word[index+2]]
                else:
                    output=output+dict_2[pairs]+"-"
                    output=output+dictnary[word[index+2]]+"-"
                index=index+3
            else:
                if(word[index+3:index+4]==" " or word[index+3:index+4]=="'"):
                    output=output+dict_2[pairs]
                else:
                    output=output+dict_2[pairs]+"-"
                index=index+2
        elif pair in dictnary:
            if(word[index+1:index+2]==" " or word[index+1:index+2]=="'"):
                output=output+dictnary[pair]
            else:
                output=output+dictnary[pair]+"-"
            index=index+1
        else:
            if((word[index-1:index]=="i" or word[index-1:index]=="e") and word[index:index+1]=="w"):
                output=output+"v"
            else:
                output=output+word[index]
            index=index+1
    if(output[-1]=="-"):
        output=output[:-1]
    print(userin.upper()+" is pronunced "+output.capitalize())
    check()
hawaina()

