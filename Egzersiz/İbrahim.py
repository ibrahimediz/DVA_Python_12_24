
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
kHarf = bHarf = rakam = noktalama = False
sifre = ""
while not ( kHarf and bHarf and rakam and noktalama):
    kHarf = bHarf = rakam = noktalama = False
    sifre = ""
    for i in range(12):
        sifre += choice(choice([ascii_uppercase, ascii_lowercase, digits, punctuation]))
    for item in sifre:
        if item.isalpha() and not bHarf and not kHarf:
            if item.isupper():
                bHarf = True
            else:
                kHarf = True
        if item.isdigit() and not rakam:
            rakam = True
        if item in punctuation:
            noktalama = True
else:
    print(sifre)