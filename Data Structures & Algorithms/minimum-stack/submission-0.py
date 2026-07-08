class MinStack:

    def __init__(self):
        self.st = []
        self.stMin = []

    def push(self, val: int) -> None:
        self.st.append(val)
        temp = val
        if len(self.stMin) > 0:
            temp = min(temp, self.stMin[-1])
        self.stMin.append(temp)

    def pop(self) -> None:
        self.st.pop()
        self.stMin.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.stMin[-1]

