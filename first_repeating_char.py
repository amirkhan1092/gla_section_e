# https://www.hackerrank.com/contests/python37-l7/challenges/first-non-repeating-char

st = input()

for i in st:
    if st.count(i) == 1:
        print(i)
        break
else:
    print(None)
