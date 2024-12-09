liste = ["İbrahim", "Seyfullah", "Fatih", "Furkan", "Mustafa", "Tolga","Melis","Enes","Yusuf",
"Özge","Gizem","İpek",
         ]
metin = """
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
"""
import pathlib
folder = pathlib.Path(__file__).absolute().parent
for item in liste:
    with open(folder / f"{item}.py","a+") as dosya:
        dosya.write(metin)
