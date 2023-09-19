class Set:
    def __init__(self):
        self.l = eval(input("enter list: "))
        self.l1 = [[], self.l]
        self.length = len(self.l)
    def subset(self, n):
        s = '[['
        for i in range(n - 1):
            s += f"t.l[i{i}], "
        s += f"t.l[i{n - 1}]] for i0 in range({t.length}) "
        for j in range(1, n):
            s += f"for i{j} in range(i{j - 1}, {t.length})  "
        s += "]"
        return eval(s)
    def powerset(self):
        if not self.l:
            return([[]])
        else:
            for k in range(1, self.length):
                l2 = self.subset(k)
                self.l1 +=l2
            return self.l1
    @property
    def l(self):
        return self._l
    @l.setter
    def l(self, l):
        l3 = []
        if type(l) != type([]):
            raise TypeError("invalid input datatype")
        else:
            for i in l:
                if i in l3:
                    raise ValueError("input has repeating values")
                l3.append(i)
            else:
                self._l = l
t = Set()
print(t.powerset())
        