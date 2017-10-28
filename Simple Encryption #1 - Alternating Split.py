Simple Encryption #1 - Alternating Split
https://www.codewars.com/kata/57814d79a56c88e3e0000786

def encrypt(text, n):
    text1 = ""
    text2 = ""
    z = ""
    y = 0
    if text == "":
        return ""
    elif n <= 0:
        return text
    else:
        while y < n:
            text1 = text[1::2]
            text2 = text[0::2]
            text = text1+text2
            y += 1
    return text
def decrypt(encrypted_text, n):
    s1 = ""
    s2 = ""
    res = []
    i = ""
    j = ""
    y = 0
    orig = encrypted_text
    if encrypted_text == "":
        return ""
    elif n <= 0:
        return encrypted_text
    else:
        while y < n:
            s1 = encrypted_text[0:int(len(encrypted_text)//2)]
            s2 = encrypted_text[int(len(encrypted_text)//2):len(encrypted_text)]
            s1 = list(s1)
            s2 = list(s2)
            encrypted_text = [j for i in zip(s2,s1) for j in i]
            y += 1
            res = encrypted_text
            if len(orig)%2!=0:
                res.append(s2[-1])
            res = "".join(res)
            res = str(res)
            print (res)
    return res
