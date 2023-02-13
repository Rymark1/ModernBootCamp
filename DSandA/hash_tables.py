#  Hash Tables are basically a giant list that we add items to according to a calculated index(hash).  The key that is
#  passed gets run through the hash method, and then it returns an index that we will place the data.  We then load
#  that data as a list into the data_map.
#
#      key               run through the hash method          load into the data_map at secified index
#  ['bolts', 1000]    ->   index =  __hash('bolts')      ->  data_map[index].append(['bolts], 1000)
#
#  There is the chance that the different keys can result in the same index.  This is called collision and there are a
#  number of ways to handle it, but the best method to prevent is using a prime number of slots in the hash table and
#  another prime number for the hash calculation.  In our example below, we have a hash table of 7 total items and the
#  hash calculation sums up the value of each of the letters, multiplies that by 23 and divides it by the length of
#  the list(7).
#
#  This doesn't prevent all collisions, but for our setup, we can load as many items into an index as we would like.
#  When we are trying to get an item/value from the hash table, we need to iterate through the items at the specific
#  index we calculate for a given key.  When/if we find a match, we return the value.
#
#  Big O for hash tables for the set and get methods are O(1).  Even though it could essentially have 5-10 items only
#  at 1 address, the assumption is your hash calculation is good enough to distribute the items relatively evenly.
import time


class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ":", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for item in self.data_map[index]:
                if item[0] == key:
                    return item[1]
        return None

    def keys(self):
        all_keys = []
        for item in self.data_map:
            if item:
                for inner_item in item:
                    all_keys.append(inner_item[0])
        return all_keys


my_hash_table = HashTable()
my_hash_table.print_table()

print("\n**** Testing set_item ****")
my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)
my_hash_table.print_table()
print("\n**** Testing get_item ****")
print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('lumber'))
print(my_hash_table.get_item('testing'))
print("\n**** Testing keys ****")
print(my_hash_table.keys())


#  Sample interview question is to determine if there is a duplicate value in 2 separate lists.  The wrong way of
#  doing this would be to do nested for loops until you find a match.

#  This is O(n^2) which means for every additional item added, the time to completion grows exponentially.
def check_bad_dups(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False


#  This is O(n) which means we are only limited at worst case to the number of items contained in both lists.  It cuts
#  down on redundancy checks.
def check_good_dups(l1, l2):
    test_dict = {}
    for item in l1:
        test_dict[item] = True
    for item in l2:
        if item in test_dict:
            return True
    return False


# test1 = [1, 3, 5]
# test2 = [2, 4, 5]
# test3 = [1, 3, 5]
# test4 = [2, 4, 6]
test1 = range(1, 10000)
test2 = range(9999, 20000)
test3 = range(1, 10000)
test4 = range(10001, 20000)
print("\n**** Testing bad interview answer ****")
tic = time.perf_counter()
print(check_bad_dups(test1, test2))
print(check_bad_dups(test3, test4))
toc = time.perf_counter()
print(f"Total Runtime of : {toc - tic}")

print("\n**** Testing good interview answer ****")
tic = time.perf_counter()
print(check_good_dups(test1, test2))
print(check_good_dups(test3, test4))
toc = time.perf_counter()
print(f"Total Runtime of : {toc - tic}")
