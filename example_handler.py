from YUVHandler import *
from sys import argv


yuv_handle = YUVHandler(argv[1], argv[2], argv[3])

y_frames,u_frames,v_frames =yuv_handle.get_frame_arrays()


yuv_handle.plot_frame(y_frames[0], u_frames[0], v_frames[0])
