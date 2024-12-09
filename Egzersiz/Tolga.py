
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

sifre = "Cemil Olabilir Mi Cem1l?"
hasLowerCase = False
hasUpperCase = False
hasDigit = False
hasNoktalama = False
for i in sifre:
    if i.isupper():
        hasUpperCase = True
    if i.islower():
        hasLowerCase = True
    if i.isdigit():
        hasDigit = True
    if not i.isalnum():
        hasNoktalama = True
if len(sifre) >= 12 and hasLowerCase and hasUpperCase and hasDigit and hasNoktalama:
    print("Valid")
else:
    print("Not Valid")