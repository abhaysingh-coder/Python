from translate import Translator
a=input("Enter the sentence")
translator1 = Translator(to_lang="German")
translation = translator1.translate(a)
print(translation)
