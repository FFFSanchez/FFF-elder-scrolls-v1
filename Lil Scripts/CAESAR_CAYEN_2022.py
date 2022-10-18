def crypt(lmsg2):
    cmsg = ''
    j = 0
    for w in lmsg2:
        while j < len(msg):
            if msg[j].isalpha():
                if msg[j].isupper():
                    cmsg += (chr((ord(msg[j].lower()) + len(w) - 97) % 26 + 97)).upper()
                elif msg[j].islower():
                    cmsg += (chr((ord(msg[j]) + len(w) - 97) % 26 + 97))
            else:
                cmsg += msg[j]

            if msg[j] == ' ':
                j += 1
                break
            j += 1

    return cmsg

msg = input()
lmsg = msg.split()
lmsg2 = []

for i in range(len(lmsg)):
    lmsg3 = ''
    for j in range(len(lmsg[i])):
        if lmsg[i][j].isalpha():
            lmsg3 += lmsg[i][j]
    lmsg2.append(lmsg3)

print(crypt(lmsg2))