def calc(nums):
    median = ''
    avg = sum(nums) / len(nums)
    maximum = max(nums)
    nums = sorted(nums)
    if len(nums) % 2 != 0:
        median = nums[int((len(nums) - 1) / 2)]
    elif len(nums) % 2 == 0:
        median = (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2) - 1]) / 2
    return (avg, median, maximum)
