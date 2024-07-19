import time


def print_info(test_n, ram_used, collisions_number, hashmap_len, start_time):
    print('\n')
    print(str(test_n) + ' values tested in ' + str(time.time() - start_time) + ' seconds')
    print('RAM used ' + str(ram_used) + '%')
    print(str(collisions_number - 1) + ' collisions found')
    print(str(hashmap_len) + ' entries in hashmap.')
    print('\n')
