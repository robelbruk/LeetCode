'''
pseudo:
    
    what do i know:
        - integer array, nums, is sorted in increasing order (i.e [1, 1, 3, 4, 5, 5])

    
    what do i need to do:
        - remove any duplicates in list, nums: going to use sets
        - going to change list, nums, in place
        - return len(nums)=k, length of UNIQUE list
'''

def removeDuplicates(nums):
    rm_dup = set(nums) # creating a set to remove duplicates in nums
    lst_rm_dup = list(rm_dup) # converting set back to list

    lst_rm_dup.sort() # sort new list
    nums.clear()

    for n in range(len(lst_rm_dup)):
        nums.append(lst_rm_dup[n])
    
    return len(nums)
