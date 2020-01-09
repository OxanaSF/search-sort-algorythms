def sort_elements(lst):
  n = len(lst)
  swaps = 0

  for i in range(n):
    swapped = False
    for j in range(0, n-i-1):
      if lst[j] > lst[j+1]:
        lst[j], lst[j+1] = lst[j+1], lst[j]
        swapped = True
        swaps += 1
       

    if not swapped:
      break

  first_el = lst[0]
  last_el = lst[-1]
  return (swaps, first_el, last_el)

print(sort_elements(['Al', 'Mg', 'Ca', 'K', 'Nb', 'I']))

#(5, 'Al', 'Nb')