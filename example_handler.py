from YUVHandler import *
from sys import argv


# YUV path, width, height
yuv_handle = YUVHandler(argv[1], argv[2], argv[3])

# whole file read (watch out for memory usage)
#Y,U,V = yuv_handle.get_frame_arrays()

#yuv_handle.plot_frame( Y[0], U[0], V[0] )
#yuv_handle.plot_frame( Y[99], U[99], V[99] )


# per frame file read
y_i,u_i,v_i = yuv_handle.get_single_frame()
si, ti = [] , []
for i in range(50):
    y_ii,u_ii,v_ii = yuv_handle.get_single_frame()
    si.append(yuv_handle.get_SI(y_ii))
    ti.append(yuv_handle.get_TI(y_i, y_ii))
    #print(i, si_ti[0], si_ti[1])

print('MEAN_SITI:',np.mean(si), np.mean(ti) )

