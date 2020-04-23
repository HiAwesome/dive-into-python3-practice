import gzip

from file_path_collect import output_txt_path_dir as dir

gz_file = dir + 'out.log.gz'

with gzip.open(gz_file, mode='wb') as z_file:
    z_file.write('A nine mile walk is no joke, especially in the rain.'.encode('utf-8'))
