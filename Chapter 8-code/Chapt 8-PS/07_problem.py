def rem(i, word):
    n =[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n

l = ["Vedan", "Anoushkan", "Bhargavan", "Kimayan", "Shravanan"]
print(rem(l, "an"))