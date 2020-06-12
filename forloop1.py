print("Second Number Pattern ")
lastNumber = int(input("give some value for iterating"))
for row in range(1, lastNumber):
    print("row number",row)
    for column in range(1, row + 1):
        print("column number",column)
        print(column, end=' ')
    print("finsh column")

