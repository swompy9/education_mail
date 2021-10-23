class CustomList(list):
    def __add__(self, other):
        if 'CustomList' not in str(type(other)):
            other = CustomList(other)
        temp = []
        if len(self) == len(other):
            for i in range(len(self)):
                temp.append(self[i] + other[i])
            return CustomList(temp)
        elif len(self) > len(other):
            for i in range(len(other)):
                temp.append(self[i] + other[i])
            temp.extend(self[len(other):])
            return CustomList(temp)
        else:
            for i in range(len(self)):
                temp.append(self[i] + other[i])
            temp.extend(other[len(self):])
            return CustomList(temp)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        temp = []
        if len(self) == len(other):
            for i in range(len(self)):
                temp.append(self[i] - other[i])
            return CustomList(temp)
        elif len(self) > len(other):
            for i in range(len(other)):
                temp.append(self[i] - other[i])
            temp.extend(self[len(other):])
            return CustomList(temp)
        else:
            for i in range(len(self)):
                temp.append(self[i] - other[i])
            temp.extend(other[len(self):])
            return CustomList(temp)

    def __rsub__(self, other):
        if len(self) == len(other):
            temp = [-i for i in self.__sub__(other)]
        elif len(self) > len(other):
            temp = [-i for i in self.__sub__(other)[:len(other)]]
            temp.extend([-i for i in self[len(other):]])
        else:
            temp = [-i for i in self.__sub__(other)[:len(self)]]
            temp.extend([i for i in other[len(self):]])
        return temp

    def __iadd__(self, other):
        if 'CustomList' not in str(type(other)):
            other = CustomList(other)
        temp = []
        if len(self) == len(other):
            for i in range(len(self)):
                temp.append(self[i] + other[i])
            return CustomList(temp)
        elif len(self) > len(other):
            for i in range(len(other)):
                temp.append(self[i] + other[i])
            temp.extend(self[len(other):])
            return CustomList(temp)
        else:
            for i in range(len(self)):
                temp.append(self[i] + other[i])
            temp.extend(other[len(self):])
            return CustomList(temp)

    def __isub__(self, other):
        temp = []
        if len(self) == len(other):
            for i in range(len(self)):
                temp.append(self[i] - other[i])
            return CustomList(temp)
        elif len(self) > len(other):
            for i in range(len(other)):
                temp.append(self[i] - other[i])
            temp.extend(self[len(other):])
            return CustomList(temp)
        else:
            for i in range(len(self)):
                temp.append(self[i] - other[i])
            temp.extend(other[len(self):])
            return CustomList(temp)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

a = [7]
b = CustomList([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print(a > b)