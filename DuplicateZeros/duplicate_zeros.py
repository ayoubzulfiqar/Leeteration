class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        
        # First pass: Determine the final length and the effective end of the original array
        # This finds the 'read_ptr' position for the second pass.
        possible_final_length = 0
        read_ptr = 0 # Pointer for the original array
        
        while read_ptr < n:
            if arr[read_ptr] == 0:
                possible_final_length += 2
            else:
                possible_final_length += 1
            
            # If we've reached or exceeded the original array's length,
            # we've found the effective end of the original array that contributes.
            if possible_final_length >= n:
                break
            read_ptr += 1
            
        # Second pass: Fill the array from right to left
        # write_ptr will be the index in the modified array
        
        write_ptr = n - 1
        
        # Handle the special case where the last zero encountered in the first pass
        # would cause an overflow if duplicated. In this case, we only write one zero.
        last_zero_overflow = False
        if possible_final_length > n:
            last_zero_overflow = True
            
        if last_zero_overflow:
            arr[write_ptr] = 0
            write_ptr -= 1
            read_ptr -= 1 # Move read_ptr back to process previous elements
            
        # Now, copy/duplicate elements from right to left
        # read_ptr is the current index in the original array to copy from
        # write_ptr is the current index in the result array to write to
        while read_ptr >= 0:
            if arr[read_ptr] == 0:
                # Duplicate the zero
                arr[write_ptr] = 0
                write_ptr -= 1
                arr[write_ptr] = 0
                write_ptr -= 1
            else:
                # Copy the non-zero element
                arr[write_ptr] = arr[read_ptr]
                write_ptr -= 1
            read_ptr -= 1