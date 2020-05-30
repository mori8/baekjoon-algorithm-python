num = input()
if len(num) == 1:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    gap = int(num[0]) - int(num[1])
    for i in range(1, len(num)-1):
        if (int(num[i]) - int(num[i+1])) != gap:
            print("흥칫뿡!! <(￣ ﹌ ￣)>")
            exit(0)
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")