def sum13(nums):
    """jdhdjkls"""
    if len(nums) == 0:
        return 0
    my_sum = 0
    for i in range(0, len(nums)):
        if nums[i] == 13:
            if nums[i+1] == 13:
                nums[i+1]
            else:
                my_sum += nums[i]
    return my_sum

print(sum13([1,13,1]))
