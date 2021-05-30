sample_list = [20, 15, 35, 300, 50, 2, 225,2,3,4]

target = 647
newlist_le_target = [a for a in sample_list if a <= target]
while target <= 647:
    if sum(sample_list) >= target:
        sample_list.pop()
        


print(newlist_le_target)
print(sum(newlist_le_target))
