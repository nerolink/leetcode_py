import re


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if s.startswith('-') or s.startswith('+'):
            s = s[1:len(s)]
        l = len(s)
        if s.endswith('e') or s.startswith('e') or s.startswith('.e'):
            return False
        match = re.match(r'\d+', s)  # 匹配整数
        if match and match.span()[1] == l:
            return True
        match = re.match(r'\d*\.\d+', s)  # 匹配小数
        if match and match.span()[1] == l:
            return True
        match = re.match(r'\d+\.\d*', s)  # 匹配小数
        if match and match.span()[1] == l:
            return True
        match = re.match(r'(\d*\.?\d*)e[-+]?\d+', s)  # 匹配e
        if match and match.span()[1] == l:
            return True
        return False
if __name__ == '__main__':
    test = Solution()
    print(test.isNumber("-7e"))
