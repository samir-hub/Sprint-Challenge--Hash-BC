#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    results_array = []
    for i in range(length):
        hash_table_insert(ht, weights[i], i)
    for i in range(length):
        target = limit - weights[i]
        result = (hash_table_retrieve(ht, target)) 
        results_array.append(result) 
        clean_results = [i for i in results_array if i is not None]
        if len(clean_results) == 0:
            return None
    return sorted(clean_results, reverse=True)


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")



#print(get_indices_of_item_weights([6,5,8,7,1], 5, 11))
