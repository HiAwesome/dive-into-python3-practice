import pickletools

from file_path_collect import output_pickle_path_dir as output


def protocol_version(file_object):
    maxproto = -1
    for opcode, arg, pos in pickletools.genops(file_object):
        maxproto = max(maxproto, opcode.proto)

    return maxproto


with open(output + 'entry.pickle', 'rb') as f:
    v = protocol_version(f)
    print(v)

"""
3
"""
