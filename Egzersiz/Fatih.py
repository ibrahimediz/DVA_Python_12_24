
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

from random import choice, shuffle, randint
from string import ascii_uppercase as up, ascii_lowercase as low, digits as dig ,punctuation as pun

password = []
password.append(choice(up))
password.append(choice(low))
password.append(choice(dig))
password.append(choice(pun))

total = up + low + dig + pun
len = randint(12, 20)
for i in range(len - 4):
    password.append(choice(total))

shuffle(password)
password = ''.join(password)
print(password)
