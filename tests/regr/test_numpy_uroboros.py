#!/usr/bin/env python

import numpy as np

revdebug.flush()  # force first AppState packets to be sent so recording is not deleted

revdebug.recrepr(np.ndarray, revdebug.recrepr(str))

a       = np.array([[1, 2, 3], [4, 5, 6]])
a[0, 0] = -1
a       = a
a[:, 1] = [-2, -5]
a       = a

raise RuntimeError('some abnormal termination')
