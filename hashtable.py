#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # TODO: Count number of key-value entries in each of the buckets
        length_of_hash_table = 0
        for bucket in self.buckets:
            length_of_hash_table += bucket.length()
            return length_of_hash_table

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # TODO: Check if the given key exists in a bucket
        index_of_bucket = self._bucket_index(key)
        the_key = self.buckets[index_of_bucket].find(lambda x: x[0] == key)
        if the_key is not None:
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value
        index_of_bucket = self._bucket_index(key)
        maybe_value = self.buckets[index_of_bucket].find(lambda x: x[0] == key)
        print key, maybe_value
        if maybe_value is not None:
            return maybe_value[1]
        raise (KeyError, "Key not found")

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # TODO: Insert or update the given key-value entry into a bucket
        index_of_bucket = self._buc
        key_index(key)
        maybe_value = self.buckets[index_of_bucket].find(lambda x: x[0] == key)
        if maybe_value is not None:
            print "The value is: ", maybe_value
            self.delete(key)
        self.buckets[index_of_bucket].append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found

        index_of_bucket = self._bucket_index(key)
        print 'bucket', self.buckets[index_of_bucket]
        print 'key', key
        self.buckets[index_of_bucket].delete(key)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # TODO: Collect all keys in each of the buckets
        list_with_all_keys = []
        for bucket in self.buckets:
            for item in bucket:
                print item
                list_with_all_keys.append(item.data[0])
        return list_with_all_keys


    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets
        list_with_all_values = []
        for bucket in self.buckets:
            for item in bucket:
                list_with_all_values.append(item.data[1])
        return list_with_all_values
