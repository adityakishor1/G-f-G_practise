class Solution:
    def matchPairs(self, n, nuts, bolts):
        order = ["!", "#", "$", "%", "&", "*", "?", "@", "^"]
        order_index = {char: i for i, char in enumerate(order)}
        nuts.sort(key=lambda x: order_index[x])
        bolts.sort(key=lambda x: order_index[x])
