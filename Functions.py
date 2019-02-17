def format(filename, text, originalstring = "{\TEXT}"):
    with open(filename, encoding='utf-8') as f:
        s = f.read()
    s = s.replace(originalstring, text)
    return s
