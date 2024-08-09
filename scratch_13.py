def sequence(n):
    arr = []
    i = 0
    # creating the sequence required for
    # implementing railfence cipher
    # the sequence is stored in array
    while (i < n - 1):
        arr.append(i)
        i += 1
    while (i > 0):
        arr.append(i)
        i -= 1
    return (arr)


# this is to implement the logic
def railfence(cipher_text, n):
    # converting into lower cases
    cipher_text = cipher_text.lower()
    L = sequence(n)
    print("The raw sequence of indices: ", L)
    temp = L
    while (len(cipher_text) > len(L)):
        L = L + temp


for i in range(len(L) - len(cipher_text)):
    L.pop()

temp1 = sorted(L)

print("The row indices of the characters in the cipher string: ", L)

print("The row indices of the characters in the plain string: ", temp1)

print("Transformed message for decryption: ", cipher_text)

# converting into plain text
plain_text = ""
for i in L:
    k = temp1.index(i)
    temp1[k] = n
    plain_text += cipher_text[k]

print("The plain text is: ", plain_text)

cipher_text = input("Enter the string to be decrypted: ")
n = int(input("Enter the number of rails: "))
railfence(cipher_text, n)