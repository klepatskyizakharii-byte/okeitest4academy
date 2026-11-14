import colorama
from colorama import Fore, Style, Back
print(dir(colorama))

print("Думаю що це саме важливе бо тут тіпа много чого написано ну і короче воно важливе але якщо по коду я думаю що"
      " воно дає змогу робити кольоровий текст стиль і вертатися обратно")
print("- Fore:", [attr for attr in dir(Fore) if not attr.startswith('_')])
print("- Back:", [attr for attr in dir(Back) if not attr.startswith('_')])
print("- Style:", [attr for attr in dir(Style) if not attr.startswith('_')])


print(Fore.RED + "This text is red? )")
#upd after print fore.red реально красный
