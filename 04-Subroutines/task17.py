def letter_n(tx,n1):
    count=0
    for i in tx:
        if n1 == i:
            count = count+1
    print(count)

txt="You never get a second chance to make a first impression"
n="e"

letter_n(txt, n)

