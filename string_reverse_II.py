class Solution(object):
    def reverseWords(self, s):
        current_word = ''
        start = 0
        for i in range(len(s)):
            index = s[i]
            if index == ' ':
                beginning = s[:start]
                end = s[i:]
                s = beginning + current_word + end
                start = i + 1
                current_word = ''
            else:
                current_word = index + current_word
        s = s[:start] + current_word
        return s
