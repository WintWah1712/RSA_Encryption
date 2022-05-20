
ctext=[2,3,4,5,6,7,8]
private_key=(10,11)
def decrypt(ctext, private_key):
    try:
        key, n = private_key
        key=2
        n=2
        text = [chr(pow(char, key, n))
                for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    data =decrypt(ctext , private_key)
    print(data)