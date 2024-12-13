import math

from matrixenc.password_extension import *
from matrixenc.rules import *

def encode(text, password):

    text_length = len(text)
    ext_pass = extend_password(password, text_length)
    enc_text = ""

    for i in range(text_length):

        x = ord(text[i]) / ord(ext_pass[i])

        for j in rules:
            if j[0] < x < j[1]:
                if j[2] == "+":
                    x += j[3]
                if j[2] == "/":
                    x /= j[3]
                if j[2] == "-sin":
                    x -= math.fabs(math.sin(i) * j[3])
                if j[2] == "+sin":
                    x += math.fabs(math.sin(i) * j[3])

        enc_text += chr(round(round(x, 4) * 10000))

    return enc_text

def decode(code, password):

    code_len = len(code)
    ext_pass = extend_password(password, code_len)
    enc_text = ""

    for i in range(code_len):

        for n in range(10000):
            x = n / ord(ext_pass[i])

            for j in rules:
                if j[0] < x < j[1]:
                    if j[2] == "+":
                        x += j[3]
                    if j[2] == "/":
                        x /= j[3]
                    if j[2] == "-sin":
                        x -= math.fabs(math.sin(i) * j[3])
                    if j[2] == "+sin":
                        x += math.fabs(math.sin(i) * j[3])

            if round(x, 4) == ord(code[i]) / 10000:
                enc_text += chr(n)
                break

    return enc_text