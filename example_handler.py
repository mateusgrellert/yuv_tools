from YUVHandler import *
from sys import argv


yuv_handle = YUVHandler(argv[1], argv[2], argv[3])

# whole file read (watch out for memory usage)
Y,U,V = yuv_handle.get_frame_arrays()

yuv_handle.plot_frame( Y[0], U[0], V[0] )
yuv_handle.plot_frame( Y[99], U[99], V[99] )


# per frame file read
for i in range(10):
    y,u,v = yuv_handle.get_single_frame()
    yuv_handle.plot_frame( y,u,v)
