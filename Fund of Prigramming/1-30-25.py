#BC
while True:
    value = int(input('please enter an integer value in the range 0...1023: '))

    binary_string = ' '

    if 0 <= value < 1024:
        if value >= 512:
            binary_string += '1'
            value %= 512
        else:
            binary_string += '0'
        if value >= 256:
            binary_string += '1'
            value %= 256
        else: 
            binary_string += '0'
        if value >= 128:
            binary_string += '1'
            value %= 128
        else:
            binary_string += '0'
        if value >= 64:
            binary_string += '1'
            value %= 64
        else:binary_string += '0'
        if value >= 32:
            binary_string += '1'
            value %= 32
        else:binary_string += '0'
        if value >= 16:
            binary_string += '1'
            value %= 16
        else:binary_string += '0'
        if value >= 8:
            binary_string += '1'
            value %= 8
        else:binary_string += '0'
        if value >= 4:
            binary_string += '1'
            value %= 4
        else:binary_string += '0'
        if value >= 2:
            binary_string += '1'
            value %= 2
        else:binary_string += '0'
        if value >= 1:
            binary_string += '1'
            value %= 1
        else:binary_string += '0'

        print(binary_string)
            


# binary_string += srt(value//512)
    # value %= 512

    