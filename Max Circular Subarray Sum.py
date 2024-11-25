def circularSubarraySum(arr):
    def kadane(arr):
        max_ending_here = arr[0]
        max_so_far = arr[0]
        for i in range(1, len(arr)):
            max_ending_here = max(arr[i], max_ending_here + arr[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far
    max_kadane = kadane(arr)
    total_sum = sum(arr)
    for i in range(len(arr)):
        arr[i] = -arr[i]
    min_kadane = kadane(arr)
    circular_sum = total_sum + min_kadane 
    if circular_sum == 0:
        return max_kadane
    return max(max_kadane, circular_sum)
