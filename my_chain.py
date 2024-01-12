class Chain:
    def __init__(self, *args):
        if not args:
            raise ValueError("You didn't insert any arguments.")
        self.args = args

    def __iter__(self):
        for i in self.args:
            for j in i:
                yield j

    def __eq__(self, other):
        return list(self) == other


assert list(Chain([1, 2, 3], "123")) == [1, 2, 3, '1', '2', '3']
assert list(Chain([1, 2, 3])) == [1, 2, 3]
assert list(Chain([1, 2, 3], ("a", "b", "c"), "456")) == [1, 2, 3, 'a', 'b', 'c', '4', '5', '6']
print("All assertions passed!")
