numbers = [18, 29, 3, 45, 7, 12]

min_son = numbers[0]
max_son = numbers[0]

for son in numbers:
    if son < min_son:
        min_son = son
    if son > max_son:
        max_son = son

print("Eng kichik son:", min_son)
print("Eng katta son:", max_son)