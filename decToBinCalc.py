#!/usr/bin/env python3
# https://github.com/jrom876/CES_repository/blob/master/decToBinCalc.py
import math

## Note: The qty of functions required is
#   q = 2^n - n
# eg: We have 4 categories, bin, oct,
# dec, and hex; thus n = 4;
#   q = 2^4 - 4 = 12 functions required
# to cover all possible combinations
#========= Binary ==========#
def bin_to_dec(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

## Binary to octal the easy way
# def bin_to_oct(binary):
#     x = bin_to_dec(binary)
#     result = oct(x)
#     return result

## Binary to octal the hard way
def bin_to_oct(binary):
    octal, i, rem, val = 0, 1, 0, 0
    while(binary > 0):
        rem = binary % 1000
        if rem = 0:
            val = 0
        elif rem = 1:
            val = 1
        elif rem = 2:
            val = 2
        elif rem = 3:
            val = 3
        elif rem = 4:
            val = 4
        elif rem = 5:
            val = 5
        elif rem = 6:
            val = 6
        elif rem = 7:
            val = 7
    octal = (val * i) + octal
    binary = binary//1000
    i *= 10
    return '0o'+str(octal)

def bin_to_hex(binary):
    x = bin_to_dec(binary)
    result = hex(x)
    return result

#========= Octal ==========#
def oct_to_bin(oct):
    # return int(oct(x)[2:])
    dec = int(oct, 8)
    return bin(dec)

def oct_to_dec(oct):
    # return int(oct(x)[2:])
    dec = int(oct, 8);
    return dec

def oct_to_hex(oct):
    dec = int(oct, 8)
    return hex(dec)

#========= Decimal ==========#
# def dec_to_bin(x):
#     # return int(bin(x)[2:])
#     return bin(x)

def dec_to_bin(decimal):
    binary, i = 0, 0
    while(decimal != 0):
        bin = decimal % 2
        binary = binary + bin * pow(10, i)
        decimal = decimal//2
        i += 1
    return binary

# def dec_to_oct(x):
#     # return int(oct(x)[2:])
#     return oct(x)

def dec_to_oct(decimal):
    octal, i = 0, 0
    while(decimal != 0):
        oct = decimal % 8
        octal = octal + oct * pow(10, i)
        decimal = decimal//8
        i += 1
    return '0o'+str(octal)

# def dec_to_hex(x):
#     # return int(hex(x)[2:])
#     return hex(x)

def dec_to_hex(decimal):
    hexadec, i = 0, 0
    while(decimal != 0):
        hex = decimal % 16
        hexadec = hexadec + hex * pow(10, i)
        decimal = decimal//16
        i += 1
    return '0x'+str(hexadec)

#========= Hexadecimal ==========#
def hex_to_bin(hex):
    dec = int(hex, 16)
    return dec_to_bin(dec)

def hex_to_oct(hex):
    dec = int(hex, 16)
    return dec_to_oct(dec)

def hex_to_dec(hex):
    return int(hex, 16)

########################################
### User Interface ###
def getuserInput():
    print("1 = Binary to All    2 = Octal to All")
    print("3 = Decimal to All   4 = Hex to All")
    print("5 = Exit\n")
    choice = int(input("Choose from the above list:\t"))

    if choice == 1:# Binary to all
        bin = int(input("Binary in ==> to All: "))
        print(bin_to_oct(bin))
        print(bin_to_dec(bin))
        print(bin_to_hex(bin))
        return 0
    elif choice == 2:# Octal to All
        oct = input("Octal in ==> to All: ")
        print(oct_to_bin(oct))
        print(oct_to_dec(oct))
        print(oct_to_hex(oct))
        return 0
    elif choice == 3:# Decimal to All
        dec = int(input("Decimal in ==> to All: "))
        print(dec_to_bin(dec))
        print(dec_to_oct(dec))
        print(dec_to_hex(dec))
        return 0
    elif choice == 4:# Hex to All
        hex = input("Hex in ==> to All: ")
        print(hex_to_bin(hex))
        print(hex_to_oct(hex))
        print(hex_to_dec(hex))
        return 0
    elif choice == 5: # Exit
        exit_flag = 1
        return 0
    else:
        return 0

#########################################
# Driver program
if __name__ == "__main__":
    exit_flag = 0
    while exit_flag == 0:
        print("\nWelcome to Number Converter ")
        ch = input("To begin, choose (c)ontinue or (q)uit\n")
        if ch == "q":
            print("Now exiting the program\n ")
            exit_flag = 1
        elif ch == "c":
            getuserInput()
            exit_flag = 0
        else:
            print("Incorrect answer. \n Exiting\n ")
            exit_flag = 1
