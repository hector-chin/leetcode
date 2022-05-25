def sortByBits(arr):
    bit_dict = {}
    final_list = []
    def count_binary(x):
        how_many_bits = 0
        quotient = 1
        while quotient != 0:
            quotient = x // 2
            reminder = x % 2
            if reminder == 1:
                how_many_bits += 1
            x = x // 2
        return how_many_bits
    for i in range(0, len(arr)):
        if count_binary(arr[i]) in bit_dict:
            bit_dict[count_binary(arr[i])] += [arr[i]]
            continue
        bit_dict[count_binary(arr[i])] = [arr[i]]

    key_list = sorted(bit_dict.keys())
    for i in key_list:
        final_list += sorted(bit_dict[i])
    print(final_list)
    return final_list




arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
test = sortByBits(arr)
