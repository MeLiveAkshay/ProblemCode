array = [26, 58, 79, 12, 34, 11, 9, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200]
print(array)

print(str(array[0]) + " is the first element")  # First element
print(str(array[-1]) + " is the last element")  # Last element
print(str(array[1]) + " is the second element")  # Second element
print(str(array[-2]) + " is the second last element")  # Second last element
print(str(array[2]) + " is the third element")  # Third element
print(str(array[-3]) + " is the third last element")  # Third last element



array.append(6)
print(array)

array.pop()
print(array)

array.insert(0, 6)
print(array)

array.remove(6)
print(array)

array.sort()
print(array)

array.reverse()
print(array)

print(len(array))
