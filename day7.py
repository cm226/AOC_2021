import functools

input = open("day7.dat", "r")


nums = list(map(lambda x : int(x), input.readline().split(',')))
nums = sorted(nums)


## part 1
# print(nums)
# middle = int((len(nums)/2)-1)
# if len(nums) % 2 != 0:
#     median = nums[middle]
# else:
#     median = (nums[middle] + nums[middle+1] ) /2

# fule = 0
# for num in nums:
#     fule += abs(median - num)

## part 2

average = int(functools.reduce(lambda x,y: x+y, nums)/len(nums))

fule = 0
for num in nums:
    dist = abs(average - num)
    fule += (dist*(dist-1)) - (((dist-1)/2)*(dist)) + dist

print(fule)
