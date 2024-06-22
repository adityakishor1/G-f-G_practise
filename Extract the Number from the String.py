class Solution:
    def ExtractNumber(self, sentence: str) -> int:
        words = sentence.split()
        max_num = -1
        for word in words:
            if word.isdigit():
                num = int(word)
                if '9' not in str(num):
                    max_num = max(max_num, num)
        return max_num
