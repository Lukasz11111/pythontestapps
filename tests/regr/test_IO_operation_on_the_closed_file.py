import json
 
# Opening JSON file
f = open('tests/regr/data.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Closing file
f.close()

data = json.load(f)

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')
