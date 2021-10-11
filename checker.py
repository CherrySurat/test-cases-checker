from testrail import *
import pprint, re, sys

client = APIClient('https://natnapinmas.testrail.io/')
client.user = 'natnapin.m@pomelofashion.com'
client.password = 'pomelo123*QA'

cases = client.send_get('get_cases/2')
for mycase in cases['cases']:
    print("JIRA = %s, Section = %d, Title = %s" % (mycase['refs'],mycase['section_id'], mycase['title']))
# pprint.pprint(cases['cases'])

# Open feature file
FEATURE_FILE = 'test.feature'
try:
    handle = open(FEATURE_FILE,'r')
except:
    print >> sys.stderr, "[ERROR] Error while opening file {0}".format(FEATURE_FILE)
    exit(1)

# compil regexp
REGEXP_CASE = "^\s*\|\s*(?P<ID>[a-zA-Z0-9]+)\s*\|\s*(?P<TestCase>[a-zA-Z0-9_\-\s]+)\s*\|(.*)$"
feature_cases = {}

while True:
    # read file line by line
    line = handle.readline()
    # check if line empty (EOF)
    if not line:
        break
    # check if regexp match
    m = re.match(REGEXP_CASE, line)

    # if match, extract TestCase group + save in dict
    if m is not None:
        t = m.groupdict()
        feature_cases[t['ID'].strip()] = t['TestCase'].strip()    

print("")
print("---------- Read from feature file --------")
pprint.pprint(feature_cases)