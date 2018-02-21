import sys, json


with open('/tmp/json-file') as data_file:
	value = json.load(data_file)

def test(value1):
	print value1

#value = json.load(sys.argv[1])
test(value)

