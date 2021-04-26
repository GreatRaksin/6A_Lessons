'''
1. import library_name -> library_name.do_smth()
2. import library_name as ln -> ln.do_smth()
3. from library_name import do_smth, do_nothing -> do_nothing()
^ при таком импорте, вы забираете ТОЛЬКО определенные функции.
4. from library_name import * -> могу использовать все функции
для небольших библиотек лучше использовать 4 импорт.

Никогда не называйте файлы именем библиотек
'''
from turtle import *

tina = Turtle()  # создал черепашку
tina.shape('turtle')  # указал, что форма будет черепашкой

done()  # не даю окну закрыться сразу
