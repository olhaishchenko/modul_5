def real_len(text):

    text1 = text.replace('\n', '') if text.rfind('\n') != -1 else text
    text2 = text1.replace('\t', '') if text1.rfind('\t') != -1 else text1
    text3 = text2.replace('\r', '') if text2.rfind('\r') != -1 else text2
    text4 = text3.replace('\f', '') if text3.rfind('\f') != -1 else text3
    text5 = text4.replace('\v', '') if text.rfind('\v') != -1 else text4
    return len(text5)

a = 'Alex\nKdfe23\t\f\v.\r'
b = 'Al\nKdfe23\t\v.\r'
print(real_len(b))