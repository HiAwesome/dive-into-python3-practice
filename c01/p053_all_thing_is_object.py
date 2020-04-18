import c01.p044_humansize as humansize

print(humansize.approximate_size(4096, True))
print()
print(humansize.approximate_size.__doc__)

"""
4.0 KiB

Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string
    

"""
