from YUVHandler import *
from sys import argv


yuv_handle = YUVHandler(argv[1], argv[2], argv[3])

# whole file read (watch out for memory usage)
Y,U,V = yuv_handle.get_frame_arrays()

#yuv_handle.plot_frame( Y[0], U[0], V[0] )
#yuv_handle.plot_frame( Y[99], U[99], V[99] )


# per frame file read
for i in range(1):
    y,u,v = yuv_handle.get_single_frame(i)
    for j in range(4):
	    yuv_handle.get_luma_CTUs(y, 64, j)
    #yuv_handle.plot_frame( y,u,v)
