
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

lowercaseLen, uppercaseLen, numberLen, punctuationLen = choice(range(1,5)), choice(range(1,5)), choice(range(1,5)), choice(range(1,5))

random_lower = random.choice(string.ascii_lowercase)
random_uppercase = random.choice(string.ascii_uppercase)
random_digit = random.choice(string.ascii_digits)
random_punctiation = random.choice(string.ascii_punctitation)

password = "";


for i in range(0,10):
    





