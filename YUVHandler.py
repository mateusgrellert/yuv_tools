import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class YUVHandler:
    def __init__(self, yuv_path = None, w = 0, h = 0, sampling = '420'):
        self.yuv_path = yuv_path
        self.yuv_fp = None
        self.w = int(w)
        self.h = int(h)
        self.sampling = sampling
        self.frames_read = 0
        self.YUV = None
        self.yuv = None
        self.Y = self.U = self.V = None

        if self.yuv_path:
            self.yuv_fp = open(self.yuv_path, 'rb')




    def set_yuv_path(self, yuv_path):
        self.yuv_path = yuv_path
    def set_res(self, h, w):
        self.h, self.w = h, w
    def set_sampling(self, sampling):
        self.sampling = sampling

    def get_frame_arrays(self, max_frames = float('+inf')):
        if self.yuv_path:
            self.YUV = np.fromfile(self.yuv_path,dtype='uint8')
        else: return

        YUV, h, w = self.YUV, self.h, self.w
        subsample = 2 if self.sampling == '420' else 1

        px = w*h
        Y, U, V = [], [], []

        i = 0
        while (i < YUV.shape[0]) and self.frames_read != max_frames:

            luma_end = i+px
            cb_end = luma_end + (px//(subsample**2))
            cr_end = cb_end + (px//(subsample**2))

            Y.append(YUV[i:luma_end].reshape(h,w))
            U.append(YUV[luma_end:cb_end].reshape(h//subsample,w//subsample))
            V.append(YUV[cb_end:cr_end].reshape(h//subsample,w//subsample))


            i = cr_end
            self.frames_read += 1



        self.Y, self.U, self.V = np.asarray(Y), np.asarray(U), np.asarray(V)

        return self.Y, self.U, self.V

    def get_single_frame(self, idx):
        YUV, h, w = self.YUV, self.h, self.w
        subsample = 2 if self.sampling == '420' else 1
        px = w*h

        frame_size = px + 2*(px//(subsample**2))

        if self.yuv_fp and frame_size:
            self.yuv_frame = np.fromfile(self.yuv_fp,dtype='uint8', count = frame_size)
            yuv_frame = self.yuv_frame
        else: return


        y, u, v = [], [], []

        luma_end = px
        cb_end = luma_end + (px//(subsample**2))
        cr_end = cb_end + (px//(subsample**2))

        y = yuv_frame[i:luma_end].reshape(h,w)
        U = yuv_frame[luma_end:cb_end].reshape(h//subsample,w//subsample)
        V = yuv_frame[cb_end:cr_end].reshape(h//subsample,w//subsample)


        self.y, self.u, self.v = np.asarray(y), np.asarray(u), np.asarray(v)
        return self.y, self.u, self.v

    def plot_frame(self, y, u = None, v = None, file = None):
        if u is not None and v is not None:
            yuv_rgb = self.to_RGB(y,u,v)
            plt.imshow(yuv_rgb)
        else:
            plt.imshow(y, cmap = 'gray')

        if file:
            plt.savefig(y)
        else:
            plt.show()

    def to_RGB(self,y,u,v):
        h,w = y.shape
        Ufull = np.repeat(u, 2,axis=0)
        Ufull = np.repeat(Ufull, 2,axis=1)
        Vfull = np.repeat(v, 2,axis=0)
        Vfull = np.repeat(Vfull, 2,axis=1)

        #yuv_ycbcr = np.concatenate((y,Ufull,Vfull[...,None]), axis = 2)
        yuv_ycbcr = np.stack((y, Ufull, Vfull), axis = 2)

        return Image.fromarray(yuv_ycbcr, mode = 'YCbCr').convert('RGB')

