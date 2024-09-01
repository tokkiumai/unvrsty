import time
import psutil
import argparse

from .rot_13 import hash_rot_13
from .caesar import hash_caesar_cipher
from .str_by_four import hash_str_by_four
from .str_in_half import hash_str_in_half
from .string import hash_str
from .util import cls, generate_str, print_info

start_time = time.time()
parser = argparse.ArgumentParser(description='Hash Composition')
parser.add_argument('-s', '--stringL', help='string len to hash', required=False)
parser.add_argument('-t', '--hashL', help='hash len to test', required=False)
parser.add_argument('-r', '--maxRAM', help='max RAM to use', required=False)
parser.add_argument('-c', '--maxCollisionsNumber', help='collisions num to find', required=False)
parser.add_argument('-trace', '--trace', help='show info', required=False)
parser.add_argument('-loops', '--loops', help='loops to hash', required=False)
args = parser.parse_args()

STR_LEN = int(args.stringL or 12)
HASH_LEN = int(args.hashL or 12)
MAX_RAM = int(args.maxRAM or 4096)
MAX_COLLISIONS = int(args.maxCollisionsNumber or 1)
SHOULD_TRACE = args.trace or False
LOOPS_TO_HASH = int(args.loops or 5)

hashmap = {}
collisions = {}


def show_init_info():
    print(
        "params: \n\n" +
        "string len: %s \n hash len: %s \n max RAM: %s \n max collisions: %s" % (
        STR_LEN, HASH_LEN, MAX_RAM, MAX_COLLISIONS)
    )


def control_or_store(key, val):
    global hashmap
    if key in hashmap and hashmap.get(key) != val:
        global collisions
        collisions.update({hashmap.get(key): val})
        print('collision detected..')
        print('hash: ' + key + ' with value of ' + val)
        print('in ' + str(time.time() - start_time) + ' sec')
        return True
    else:
        hashmap.update({key: val})
        return False


cls()
show_init_info()
collisions_number = 1
test_number = 0
while collisions_number <= MAX_COLLISIONS:
    virtual_memory = str(psutil.virtual_memory())
    virtual_memory = int(virtual_memory[55:57])
    test_number += 1
    if SHOULD_TRACE and test_number % 100000 == 0:
        print_info(test_number, virtual_memory, collisions_number, len(hashmap), start_time)
    s1 = generate_str(STR_LEN)
    s2 = generate_str(STR_LEN)
    h1 = hash_str(s1, LOOPS_TO_HASH)
    h2 = hash_str(s2, LOOPS_TO_HASH)
    if control_or_store(h1, s1) or control_or_store(h2, s2):
        collisions_number += 1
    if virtual_memory > MAX_RAM:
        print('stopping... RAM bounds')
        break

end_time = time.time()
exec_time = end_time - start_time
print('top stopping...')
print('list of collisions: \n' + str(collisions.items()))
print('in ' + str(exec_time) + ' secs')
