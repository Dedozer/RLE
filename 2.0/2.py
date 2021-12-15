def compress():
    file = open('lazy_town.png', 'rb')
    data = file.read()
    file.close()
    counter_recurring = 0
    counter_non_recurring = 127
    list_recurring = []
    b = bytearray()
    s = bytearray()
    for i in range(len(data)-1):
        if data[i+1] == data[i]:
            if counter_recurring != 0:
                b.append(counter_recurring)
                for el in list_recurring:
                    b.append(el)
                counter_recurring = 0
                list_recurring = []
            if counter_non_recurring >= 255:
                b.append(counter_non_recurring)
                b.append(data[i])
                counter_non_recurring = 127
            else:
                counter_non_recurring += 1
        else:
            if counter_non_recurring > 127:
                counter_non_recurring += 1
                b.append(counter_non_recurring),
                b.append(data[i])
                counter_non_recurring = 127
                continue
            if counter_recurring >= 127:
                b.append(counter_recurring),
                for el in list_recurring:
                    b.append(el)
                list_recurring = []
                counter_recurring = 0
            else:
                counter_recurring += 1
                list_recurring.append(data[i])
        if i == len(data)-2:
            if list_recurring != []:
                b.append(counter_recurring)
                for el in list_recurring:
                    b.append(el)
            if counter_non_recurring != 127:
                b.append(counter_non_recurring)
                b.append(data[i-1])
    file = open('binary', 'wb')
    file.write(b)
    file.close()
    file = open('binary', 'rb')
    data2 = file.read()
    file.close()





compress()