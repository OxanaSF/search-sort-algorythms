def sort_participants(lst):
  swap = 0
  for i in range(len(lst)):
    min_index = i

    for curr_index in range(i+1, len(lst)):

      if lst[min_index][1] >= lst[curr_index][1]:
        min_index = curr_index
    

    lst[i], lst[min_index] = lst[min_index], lst[i]
    swap += 1

  return (swap, lst[0][0], lst[-1][0])





participants = [("Anna", 4), ("Federico", 1), ("Mandy", 3), ("Igor", 2)]
nums = [2,6,8,4,3, 8]

print(sort_participants(participants))