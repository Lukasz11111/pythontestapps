import json
 
# Opening JSON file
f = open('tests/regr/data.json',)
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
print(data['test'])
 
# Closing file
f.close()

if revdebug.conn.mode == revdebug.Crash:
    raise RuntimeError('done')
