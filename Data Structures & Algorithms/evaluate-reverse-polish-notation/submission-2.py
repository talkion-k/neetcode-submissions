class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for t in tokens:
            if t not in {"+", "-", "*", "/"}:
                st.append(t)
            else:
                r = int(st.pop())
                l = int(st.pop())
                if t == "+":
                    st.append(l + r)
                elif t == "-":
                    st.append(l - r)
                elif t == "*":
                    st.append(l * r)
                else:
                    st.append(l / r)
        return int(st[0])

