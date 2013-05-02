_number_of_lines = 100000
import os
import glob
import heapq
import sys
import shutil

def write_block(next_block, counter, tmp_storage):
    filename = os.path.join(tmp_storage, 'tmp_%d.txt' % counter)
    with open(filename, 'w') as current_outputfile:
        next_block.sort()
        current_outputfile.write('\n'.join(next_block))



def read_chunks_and_sort(filename, number_of_lines, tmp_storage='./temp/'):
    counter = 0
    with open(filename) as mainfile:
        while 1:

            try:
                next_block = [mainfile.next() for x in xrange(number_of_lines)]
            except:
                write_block(next_block, counter, tmp_storage)
                break
            write_block(next_block, counter, tmp_storage)
            counter=counter+1




def merge(*streams):
    heap = []
    for stream in streams:
        for value in stream:
            heap.append((value, stream))
            break
    heapq.heapify(heap)

    while heap:
        current_value, iterator = heap[0]
        yield current_value
        for current_value in iterator:
            heapq.heapreplace(heap, (current_value, iterator))
            break
        else:
            heapq.heappop(heap)

def sort_log_file(logfilepath, chunk_size = 100000, tmp_storage='./temp/'):
    if not os.path.exists(tmp_storage):
        os.makedirs(tmp_storage)
    read_chunks_and_sort(logfilepath, chunk_size, tmp_storage)
    f_names = glob.glob('%s*.txt' % tmp_storage)
    _streams = []
    for filename in f_names:
        _streams.append(open(filename))
    for value in merge(*_streams):
        yield value
    shutil.rmtree(tmp_storage)
if __name__ == '__main__':

    for item in sort_log_file(sys.argv[1]):
        print item



 