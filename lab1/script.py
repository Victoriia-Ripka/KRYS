# PART ENCODING

# TASK ASCII
# chr() and ord()
# ascii_code = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
# def uncript_text(ascii_code):
#     return chr(ascii_code)

# def cript_text(letter):
#     return ord(letter)
# print(''.join(uncript_text(ascii) for ascii in ascii_code)) # crypto{ASCII_pr1nt4bl3}


# TASK HEX
# bytes.fromhex() and bytes.hex()
# letter -> ascii ->  base-16 numbers (hexadecimal)
# hex_string = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'
# bytes.fromhex(hex_string) # crypto{You_will_be_working_with_hex_strings_a_lot}
# text = 'crypto{You_will_be_working_with_hex_strings_a_lot}'
# print(text.encode().hex())


# TASK Base64
# Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.
# import base64
# hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
# bytes_string = bytes.fromhex(hex_string)
# b64_answer = base64.b64encode(bytes_string) # crypto/Base+64+Encoding+is+Web+Safe/


# TASK Bytes and Big Integers
# bytes_to_long() and long_to_bytes()
# handle text for numeric algorithms
# message -> bytes -> hexadecimal -> concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.
# message: HELLO
# ascii bytes: [72, 69, 76, 76, 79]
# hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]
# base-16: 0x48454c4c4f
# base-10: 310400273487
# from Crypto.Util.number import *
# import base64
# message = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# answer = long_to_bytes(message)
# answer = bytes_to_long(bytes.fromhex(message))




# PART XOR

# TASK Starter
# We can XOR strings by first converting each character to the integer representing the Unicode character.
# word = 'label'
# ascii_codes = [ord(letter) for letter in word] # [108, 97, 98, 101, 108]
#  We can XOR integers by first converting the integer from decimal to binary.
# integer = 13
# new_codes = [ ascii ^ integer for ascii in ascii_codes ] # [97, 108, 111, 104, 97]
# new_word = "".join(chr(code) for code in new_codes) # aloha


# TASK Properties
# from pwntools import xor
# def encrypt_flag():
#     KEY1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
#     KEY2_KEY1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
#     KEY2_KEY3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
#     WITH_FLAG = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'
#     key1 = bytes.fromhex(KEY1)
#     key2_and_key1 = bytes.fromhex(KEY2_KEY1)
#     key2_and_key3 = bytes.fromhex(KEY2_KEY3)
#     with_flag = bytes.fromhex(WITH_FLAG)
#     key2 = bytes(a ^ b for a, b in zip(key2_and_key1, key1))
#     key3 = bytes(a ^ b for a, b in zip(key2_and_key3, key2))
#     flag = bytes(
#         a ^ b ^ c ^ d
#         for a, b, c, d in zip(with_flag, key1, key2, key3)
#     )
#     return flag.decode() # crypto{x0r_i5_ass0c1at1v3}


# TASK Favourite byte
# encoded_text = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
# for i in range(0, 255):
#     option = bytes( i ^ letter for letter in bytes.fromhex(encoded_text))
#     print(option.decode())
# crypto{0x10_15_my_f4v0ur173_by7e}


# TASK you either know, xor you don't 
# encoded_text = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
# clue = 'crypto{'
# ascii_clue = [ord(letter) for letter in clue]
# key = bytes(a ^ b for a, b in zip(ascii_clue, bytes.fromhex(encoded_text))) # myXORke
# key = b"myXORkey"
# cipher_text = bytes.fromhex(encoded_text)
# answer = bytes(
#     c ^ key[i % len(key)]
#     for i, c in enumerate(cipher_text)
# ) # crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}


# TASK lemur
# from PIL import Image
# import numpy as np
# def encrypt_two_png(img1 = 'flag.png', img2 = 'lemur.png'):
#     np_img1 = np.array(Image.open(img1).convert('RGB'))
#     np_img2 = np.array(Image.open(img2).convert('RGB'))
#     if np_img1.shape != np_img2.shape:
#         raise ValueError("Images must have the same dimensions")
#     result = np.bitwise_xor(np_img1, np_img2)
#     Image.fromarray(result, 'RGB').save('result.png')





# PART MATHEMATICS

# TASK Greatest Common Divisor
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a
# print(gcd(11, 17))
# print(gcd(26513, 32321))





# PART DATA FORMATS

# TASK Privacy-Enhanced Mail?
from Crypto.PublicKey import RSA
key = RSA.importKey(open("privacy_enhanced_mail.pem").read())
print(key.d)
# (base) Viktoriias-MacBook-Pro:lab1 viktoriianowotka$ HEX=$(openssl rsa -in privacy_enhanced_mail.pem -noout -text \
#   | sed -n '/^privateExponent:/,/^prime1:/p' | sed '1d;$d' | tr -d ' :\n')

# python3 -c "print(int('$HEX', 16))"
# 15682700288056331364787171045819973654991149949197959929860861228180021707316851924456205543665565810892674190059831330231436970914474774562714945620519144389785158908994181951348846017432506464163564960993784254153395406799101314760033445065193429592512349952020982932218524462341002102063435489318813316464511621736943938440710470694912336237680219746204595128959161800595216366237538296447335375818871952520026993102148328897083547184286493241191505953601668858941129790966909236941127851370202421135897091086763569884760099112291072056970636380417349019579768748054760104838790424708988260443926906673795975104689


# if __name__ == '__main__':
    # print(encrypt_flag())
    # encrypt()
    

