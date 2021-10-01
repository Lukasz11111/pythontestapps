i=1
revdebug.setrecmode(revdebug.Live)

revdebug.snapshot("1")
revdebug.clear(False)
revdebug.snapshot("2")
revdebug.clear("False")

revdebug.snapshot("3")
revdebug.clearall(False)
revdebug.snapshot("4")
revdebug.clearall("False")

