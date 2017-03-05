import json
import ijson
import sys



def get_bucket_primary_dict(json_file_path):
	bucket_primary_dict={}
	bucket_name = None
	primary_peer = None
	with open(json_file_path, 'r') as f:
		parser = ijson.parse(f)
		for prefix, event, value in parser:
			if prefix == "entry.item.name":
				bucket_name = value
			if value == "0xffffffffffffffff":
				primary_peer = prefix
			if bucket_name is not None and primary_peer is not None:
				bucket_primary_dict[bucket_name]=primary_peer
				bucket_name = None
				primary_peer = None


	return bucket_primary_dict




if __name__ == '__main__':

	before_master_restart = sys.argv[1]
	after_master_restart =  sys.argv[2]

	bucket_dict_before_restart = get_bucket_primary_dict(before_master_restart)
	bucket_dict_after_restart = get_bucket_primary_dict(after_master_restart)


	same_count = 0
	diff_count = 0
	diff_dict = {}
	for key in bucket_dict_before_restart.keys():
		if bucket_dict_before_restart[key] == bucket_dict_after_restart[key]:
			same_count = same_count + 1
		else:
			diff_count = diff_count + 1
			diff_dict[key] = bucket_dict_before_restart[key] + "-vs-" +bucket_dict_after_restart[key]

	same_percentage = str(float(same_count)*100/(same_count+diff_count))+"%"
	print "{same_percentage} pecentage of buckets' primary doesn't change".format(same_percentage = same_percentage)

	print "diff: "
	for item in diff_dict.items():
		print item