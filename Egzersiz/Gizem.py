
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

import random
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
mylist=((ascii_uppercase),(ascii_lowercase),(digits),(punctuation))
passw=""
for i in range(12):
    passw=passw+(random.choice(mylist[i%4]))
print(passw)