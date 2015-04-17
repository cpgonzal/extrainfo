#python friend_count.py /home/user/datasci_course_materials/assignment3/data/friends.json
import MapReduce
import sys

"""
Inverted index Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    mr.emit_intermediate(record[0], 1)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    mr.emit((key, sum(list_of_values)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)


