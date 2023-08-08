class Solution:
    def count(self, n : int, s : str) -> List[str]:
        # code here
        ans = 0
        ans_t = 0
        cur = None
        cur_t = 0
        for c in s:
            if c != cur:
                if cur_t > ans_t:
                    ans_t = cur_t
                    ans = cur
                cur = c
                cur_t = 1
            else:
                cur_t += 1
        if cur_t > ans_t:
            ans = cur
            ans_t = cur_t
        return [ans, ans_t]
