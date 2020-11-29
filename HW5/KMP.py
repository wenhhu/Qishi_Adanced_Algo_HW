# LC 214

class Problem1:
    def construct_pmt(self, s: str):
        pmt = [0] * (len(s) + 1)
        for i in range(2, len(s) + 1):
            cur = pmt[i - 1]
            while cur != 0 and s[i - 1] != s[cur]:
                cur = pmt[cur]
            if s[i - 1] == s[cur]:
                cur += 1
            pmt[i] = cur

        return pmt

    def shortestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        pmt = self.construct_pmt(s)
        reverse = s[::-1]
        cur = 0

        for i in range(len(reverse)):
            while cur != 0 and reverse[i] != s[cur]:
                cur = pmt[cur]

            if reverse[i] == s[cur]:
                cur += 1
            if i + 2 + cur >= len(s):
                if cur != 0 and cur < len(s):
                    if i + 2 + cur == len(s):
                        return reverse[:len(s) - 2 * cur - 1] + s
                    else:
                        return reverse[:len(s) - 2 * cur] + s
                else:
                    return reverse[:len(s) - 1] + s


class Problem2:
    def longestPrefix(self, s: str) -> str:
        pmt = [0] * (len(s) + 1)
        for i in range(2, len(pmt)):
            cur = pmt[i - 1]
            while cur != 0 and s[cur] != s[i - 1]:
                cur = pmt[cur]

            if s[cur] == s[i - 1]:
                cur = cur + 1
            pmt[i] = cur

        return s[:pmt[-1]]