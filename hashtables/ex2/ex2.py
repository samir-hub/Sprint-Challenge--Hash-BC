#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        print(hash_table_retrieve(hashtable, tickets[i].source))
    first = hash_table_retrieve(hashtable, "NONE")    
    route.insert(0, first)
    print(hash_table_retrieve(hashtable, route[0]))
    for i in range(1, length-1):
        route[i] = hash_table_retrieve(hashtable, route[i-1])
    clean_result = [i for i in route if i is not None]  
    return clean_result 
    
# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# reconstruct_trip(tickets, 3)