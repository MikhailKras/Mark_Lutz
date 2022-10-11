class NewInt(int):
    def __new__(cls, num=1):
        return int.__new__(int, num)


x = NewInt()
y = NewInt(2)
print(x, y)  # 1 2
