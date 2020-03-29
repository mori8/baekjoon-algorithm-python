str = input()

def make_pelindrome(string):
    for i in range(int(len(str)/2), len(str)):
        if str[i] == str[i+1]:
            newstr1 = str[:i+1]
            newstr2 = newstr1[::-1]
            newstr = newstr2 + newstr1
            if newstr[:len(str)] == str:
                print(len(newstr))
                break
        elif str[i-1] == str[i+1]:
            newstr1 = str[:i + 1]
            newstr2 = newstr1[::-1]
            newstr = newstr2 + newstr1
            if newstr[:len(str)] == str:
                print(len(newstr))
                break


make_pelindrome(str)
