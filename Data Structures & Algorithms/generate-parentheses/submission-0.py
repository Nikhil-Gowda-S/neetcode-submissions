class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_cnt, close_cnt, cur):
            if open_cnt == n and close_cnt == n:
                res.append("".join(cur))
                return

            if open_cnt < n:
                cur.append("(")
                backtrack(open_cnt + 1, close_cnt, cur)
                cur.pop()

            if close_cnt < open_cnt:
                cur.append(")")
                backtrack(open_cnt, close_cnt + 1, cur)
                cur.pop()

        backtrack(0, 0, [])
        return res

        