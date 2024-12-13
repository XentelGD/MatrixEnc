import matrixenc


text = matrixenc.encode(
    "Я люблю покет код, но об этом никто не узнает, ведь я зашифровал это с помощью MatrixEnc",
    ";Перейди на сикод, ведь леня ганин лучший"
)

print("encrypted: " + text)

text2 = matrixenc.decode(text, ";Перейди на сикод, ведь леня ганин лучший")

print("decrypted: " + text2)