def generate_password(n):

    password = ""

    for a in range(1, 21):
        for b in range(1, 21):
            if a != b:
                pair_sum = a + b
                if n % pair_sum == 0:
                    password += str(a) + str(b)

    return password

for n in range(3, 21):
    print(f"{n} - {generate_password(n)}")