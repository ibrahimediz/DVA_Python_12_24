
# # Şifre üreten bir program yazarken aşağıda yer alan şartları kontrol etmemiz ve şifreyi üretmemiz gerekiyor.
# # * en az 12 karakter uzunluğunda olacak
# # * içerisinde en az bir küçük harf olacak
# # * içerisinde en az bir büyük harf olacak
# # * içerisinde en az bir rakam olacak
# # * içerisinde en az bir noktalama işareti olacak
# # -----
# # bu programı yazarken aşağıdaki kodları kullanabilirsiniz:
# # from random import choice
# # from string import ascii_uppercase, ascii_lowercase, digits, punctuation
# # ----


from random import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

def createLower():
    return choice(ascii_lowercase)

def createUpper():
    return choice(ascii_uppercase)

def createDigit():
    return choice(digits)

def createPunct():
    return choice(punctuation)

funcList = [createLower, createUpper, createDigit, createPunct]

passwordChars = [createLower(), createUpper(), createDigit(), createPunct()]

for time in range(20):
    passwordChars.append(choice(funcList)())

password = " ".join(str(x) for x in passwordChars)
print(password)