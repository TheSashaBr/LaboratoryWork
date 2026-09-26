import sys

print(f"sys.argv = {sys.argv}")
print(f"Длина списка: {len(sys.argv)}")
print(f"sys.argv[0] = '{sys.argv[0]}'")
print(f"Аргументы после имени скрипта: {sys.argv[1:]}")