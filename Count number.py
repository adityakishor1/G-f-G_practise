class solution:
      def totalNumbers(self, N : int) -> int:
        # code here
        from bisect import bisect_left
        global needCompute
        global data
        if needCompute:
            val = set()
            for mask in range(1<<11):
                for x in range(10):
                    for y in range(10):
                        num = 0
                        cur_mask = mask
                        while cur_mask > 0:
                            if cur_mask & 1 > 0:
                                num = 10 * num + x
                            else:
                                num = 10 * num + y
                            cur_mask >>= 1
                        val.add(num)
            data.extend(sorted(val))
            needCompute = False
        
        return bisect_left(data, N + 1)
