class Solution(object):
    def maximum69Number (self, num):
        return int(str(num).replace('6', '9', 1))
        """
        :type num: int
        :rtype: int
        """
        