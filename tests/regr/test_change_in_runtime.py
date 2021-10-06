o="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
revdebug.setrecmode(revdebug.Crash)
revdebug.flush()

print(o)
print("revdebug")
print(dir(revdebug))

print(o)
print("revdebug.code_spans(com)")
com=compile('sum([1, 2, 3])', '', 'single')
print(dir(revdebug.code_spans(com)))

print(o)
print("revdebug.clear()")
print(dir(revdebug.clear()))

print(o)
print("revdebug.clearall()")
print(dir(revdebug.clearall()))

print(o)
print("revdebug.code_known()")
print(dir(revdebug.code_known()))

print(o)
print("revdebug.code_recorded()")
print(dir(revdebug.code_recorded()))

print(o)
print("revdebug.code_sentinel")
print(dir(revdebug.code_sentinel))

print(o)
print("revdebug.conn")
print(dir(revdebug.conn))

print(o)
print("revdebug.exception()")
print(dir(revdebug.exception()))

print(o)
print("revdebug.flush()")
print(dir(revdebug.flush()))

print(o)
print("revdebug.live_sent()")
print(dir(revdebug.live_sent()))

def v():
    aa=1
print(o)
print("revdebug.recrepr(str,v())")
print(dir(revdebug.recrepr(str,v())))

print(o)
print("revdebug.setrecmode(4)")
print(dir(revdebug.setrecmode(4)))

print(o)
print("revdebug.setrecord()")
print(dir(revdebug.setrecord("a","a")))

print(o)
print("revdebug.snapshot(")
print(dir(revdebug.snapshot("z")))

print(o)
print("revdebug.snapshotall")
print(dir(revdebug.snapshotall("x")))

print(o)
print("revdebug.stringify")
print(dir(revdebug.stringify("x")))


print(o)
print("revdebug.type_special(str)")
print(dir(revdebug.type_special(str)))

print(o)
print("revdebug.block()")
print(dir(revdebug.block()))

print(o)
print("revdebug.cfg")
print(dir(revdebug.cfg))

# revdebug.cfg.host=None

# for x in range(1,100):
#     revdebug.cfg.solution="app"+str(x)
#     revdebug.snapshot("a")

# # revdebug.setrecmode(revdebug.Live)
# revdebug.flush()  # compensating for live recording deletion on server
raise "nope"

