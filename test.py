from operator import itemgetter
import sys

# current_word = None
# current_count = 0
# word = None
# lines = [['foo', 1], ['foo', 1], ['fo', 1], ['fooo', 1], ['foo', 1]]
# # input comes from STDIN
# for line in lines:
#     # remove leading and trailing whitespace
#     # line = line.strip()
#
#     # parse the input we got from mapper.py
#     # word, count = line.split(',', 1)
#     word, count = line[0], line[1]
#     # convert count (currently a string) to int
#     try:
#         count = int(count)
#     except ValueError:
#         # count was not a number, so silently
#         # ignore/discard this line
#         continue
#
#         # this IF-switch only works because Hadoop sorts map output
#     # by key (here: word) before it is passed to the reducer
#     if current_word == word:
#         current_count += count
#     else:
#         if current_word:
#             # write result to STDOUT
#             print('%s\t%s' % (current_word, current_count))
#         current_count = count
#         current_word = word
#
#         # do not forget to output the last word if needed!
# if current_word == word:
#     print("ss")
#     print('%s\t%s' % (current_word, current_count))

import sys
lines = [['foo', 1], ['foo', 1], ['fo', 1], ['fooo', 1], ['foo', 1]]
# input comes from STDIN (standard input)
for line in lines:
    # remove leading and trailing whitespace
    # line = line.strip()
    # split the line into words
    words = line[0]
    print('%s\t%s' % (words, 1))
    # increase counters
   # for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1


