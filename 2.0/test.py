def compress(file_input):
    file = open(f'{file_input}', 'rb')
    data = file.read()
    file.close()
    counter_recurring = 0
    counter_non_recurring = 128
    list_recurring = []
    non_recuring = 0
    b = bytearray()
    flag = True
    for i in range(0, len(data)):
        #print(data[i], end=' ')
        if flag == True:
            flag = False
            continue
        if data[i - 1] == data[i]:
            if counter_non_recurring < 255:
                counter_non_recurring += 1
                non_recuring = data[i]
            elif counter_non_recurring >= 255:
                b.append(counter_non_recurring)
                b.append(data[i])
                counter_non_recurring = 129
            if len(list_recurring) > 0:
                b.append(len(list_recurring))
                for el in list_recurring:
                    b.append(el)
                list_recurring = []
        else:
            if counter_non_recurring < 255 and counter_non_recurring > 128:
                b.append(counter_non_recurring + 1)
                b.append(non_recuring)
                non_recuring = 0
                counter_non_recurring = 128
                continue
            if counter_non_recurring == 255:
                b.append(counter_non_recurring)
                b.append(non_recuring)
                counter_non_recurring = 129
            if len(list_recurring) <= 126:
                list_recurring.append(data[i - 1])
            elif len(list_recurring) >= 127:
                b.append(len(list_recurring))
                for el in list_recurring:
                    b.append(el)
                list_recurring = []
                list_recurring.append(data[i - 1])
    if data[-1] != data[-2]:
        if list_recurring == 0:
            list_recurring.append(data[-1])
            b.append(len(list_recurring))
            for el in list_recurring:
                b.append(el)
        if counter_non_recurring == 128:
            b.append(counter_non_recurring+1)
            b.append(data[-1])
    if len(list_recurring) > 0:
        list_recurring.append(data[-1])
        b.append(len(list_recurring))
        for el in list_recurring:
            b.append(el)
    else:
        if counter_non_recurring > 128:
            b.append(counter_non_recurring + 1)
            b.append(non_recuring)
    file = open('binary2', 'wb')
    file.write(b)
    file.close()




def RLE_decode2(decode_file):
    with open('binary2', 'rb') as code_file:
        data = code_file.read()
        b = bytearray()
        counter = data[0]
        for idx_byte in range(1, len(data)):
            current_byte = data[idx_byte]

            if 255 >= counter >= 128:
                counter -= 128
                for idx in range(counter):
                    b.append(current_byte)
                    counter -= 1

            elif 127 >= counter >= 1:
                b.append(current_byte)
                counter -= 1
                continue

            else:
                counter = current_byte

    with open(f'{decode_file}', 'wb') as decode_file:
        decode_file.write(b)


file_input = 'img_.bmp'
decode_file = 'img_decode.bmp'
compress(file_input)

RLE_decode2(decode_file)





'''
def decode():
    file = open('binary2', 'rb')
    data = file.read()
    file.close()
    b = bytearray()
    flag = True
    flag2 = True
    count = 0
    print('\n')
    for i in range(len(data)):
        if flag2 == True:
            if flag == True:
                if data[i] >= 128:
                    for j in range(0, data[i] - 128):
                        print(data[i + 1])
                        b.append(data[i + 1])
                    flag2 = False
                    continue
                if data[i] <= 127:
                    count = data[i] + 1
                    flag = False
            else:
                if count > 0:
                    b.append(data[i])
                    count -= 1
                else:
                    flag = True
        else:
            flag2 = True
            continue
    file = open('decode.png', 'wb')
    file.write(b)
    file.close()
'''

'''
def RLE_decode():
    with open('binary2', 'rb') as encode_file:
        data = encode_file.read()
        b = bytearray()
        counter = data[0]
        for i in range(1, len(data)):
            el = data[i]
            if (counter >= 128) and (counter <= 255):
                counter -= 128
                for j in range(counter):
                    b.append(el)
                    counter -= 1
            elif (counter >= 1) and (counter <= 127):
                b.append(el)
                counter -= 1
                continue
            else:
                counter = el
        file = open('decode.bmp', 'wb')
        file.write(b)
        file.close()
'''

'''
def RLE_decode():
    file = open('binary2', 'rb')
    data = file.read()
    file.close()
    b = bytearray()
    print('\n')
    print('\n')
    counter = data[0]
    for i in range(1, len(data)):
        #print(data[i], end=' ')
        el = data[i]

        if 255 >= counter >= 128:
            counter -= 128
            for j in range(counter):
                b.append(el)
                counter -= 1

        elif 127 >= counter >= 1:
            b.append(el)
            counter -= 1
            continue

        else:
            counter = el
        file = open('decode.', 'wb')
        file.write(b)
        file.close()
'''

'''def RLE_decode(file_name, out_img):
    with open(file_name, 'rb') as encode_file:
        print(f'file name={file_name}')
        im = encode_file.read()

        n_bytes = len(im)
        decode = bytearray()

        counter = im[0]
        for idx_byte in range(1, n_bytes):
            current_byte = im[idx_byte]

            if 255 >= counter >= 128:
                counter -= 128
                for idx in range(counter):
                    decode.append(current_byte)
                    counter -= 1

            elif 127 >= counter >= 1:
                decode.append(current_byte)
                counter -= 1
                continue

            else:
                counter = current_byte



    with open(f'{out_img}', 'wb') as decode_f:
        decode_f.write(decode)'''