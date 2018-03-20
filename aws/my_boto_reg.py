
import boto
from boto.s3.key import Key

src_loc		= 'src'

src_bkt_nm = src_loc.split('/')[2]
src_prefix = src_loc.split('s3://' + src_loc.split('/')[2] + '/')[1]

src_bkt = boto.connect_s3(host='s3.amazonaws.com').get_bucket(src_bkt_nm)

# To find list of objects under the source
src_file_list = [f for f in src_bkt.list(prefix=src_prefix)]

#  To find size of the object
obj_size = [ f.size for f in s3_bkt.list(prefix=s3_prefix)]
total_size = sum(obj_size)


