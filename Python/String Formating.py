def print_formatted(number):
    length=len(bin(number))

    oct_list = []
    hex_list = []
    bin_list = []
    dec_list = []

    for i in range(number+1):
        dec_list.append(str(i))
        oct_list.append(oct(i)[2:])
        hex_list.append(hex(i)[2:])
        bin_list.append(bin(i)[2:])

        hex_list1=[k.upper() for k in hex_list]

    for j in range(1,number+1):
        print(dec_list[j].rjust(length-2), oct_list[j].rjust(length-2), hex_list1[j].rjust(length-2), bin_list[j].rjust(length-2))

print_formatted(17)