def twoSum(nums: List[int], target: int) -> List[int]:
    hm={}
    for i in range(0,len(nums)):
        hm[nums[i]] = i # 2:0

    for i in range(0,len(nums)):
        remain = target - nums[i]
        if remain in hm and hm[remain] != i: #hm[remain] != i no duplicate 
            return [i,hm[remain]]
