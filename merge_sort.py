width = 1
arr = [2,5,4,9,16,1,7,3,8,11]

n = len(arr)

while width < n:
    sorted_arr = []
    print(f"New Outer Loop: width = {width}")
    for i in range(0, n, 2*width):
        print("New Loop")
        print(f'i = {i}')
        left = arr[i:i+width]
        right = arr[i+width:i+2*width]
        print(f'Left: {left},Right: {right}')
        print(f'length of left: {len(left)}, length of right: {len(right)}')
        
        
        l=0
        j=0
        k=i
        
        while l < len(left) and j < len(right):
            if left[l] < right[j]:
                arr[k] = left[l]
                # sorted_arr.append(left[l])
                # print(f'Sorted array: {sorted_arr}')
                l += 1
                # print(f'arr when left is less: {arr}')
            else:
                arr[k] = right[j]
                # sorted_arr.append(right[j])
                # print(f'Sorted array: {sorted_arr}')
                j += 1
                print(f'arr when right is less: {arr}')
            k += 1
            print("\n")
            print (f'l = {l}, j={j}, k={k}, arr= {arr}')
            print("\n")
        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        
        
        
    width *= 2
print(">>>>>>>>>>>>>>>>>>") 
print(arr)
