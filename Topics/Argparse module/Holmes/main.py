import argparse


def decode_caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


parser = argparse.ArgumentParser()
parser.add_argument("--file")
args = parser.parse_args()
filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
opened_file.close()  # always close the files you've opened
alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"

for n in range(len(alpha) - 1):
    decode_caesar_cipher(s=encoded_text, n=n)
