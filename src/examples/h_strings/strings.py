def test_config():
    return True

def hello_world():
    hello = "hello world!"
    print(hello[0])

def loop_str(str):
    for i in str:
        print(i)

def loop_str_while(str):
    indx = 0

    while indx < len(str):
        print(str[indx])
        indx+= 1

def concat_strings(str1,str2):
    return str1 + str2

def str_sub_str(sub_str,str):
    return sub_str in str