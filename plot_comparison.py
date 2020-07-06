"""
Set5 Results Comparison vs. VDSR (Required to clone the project first)
git clone https://github.com/twtygqyy/pytorch-vdsr

"""

import matplotlib.pyplot as plt
import numpy
import scipy.misc
from matplotlib import rc

vdsr_labels=['baby','bird','butterfly','head','woman']
moremnas_models=['A', 'B', 'C', 'D']

GT_HR_IMAGES = 'dataset/Set5/img_00%d_SRF_2_HR.png'
VDSR_SR_IMAGES = '../pytorch-vdsr/Set5/%s_GT_scale_2.bmp'
MOREMNAS_SR_IMAGES = 'result/MoreMNAS-%s/Set5/img_00%d_SRF_2_SR.png'

METHODS = ['Ground Truth', 'VDSR','MoreMNAS-A', 'MoreMNAS-B', 'MoreMNAS-C', 'MoreMNAS-D']

REGIONS = [[[0,200],[100,300]],
        [[200,150],[300,250]],
        [[100,100],[200,200]],
        [[180,0],[280,100]],
        [[0,0],[100,100]],
]


def plot_sr_comparison():
    rc('font',**{'family':'serif'})
    rc('text', usetex=True)
    fig, axes = plt.subplots(5,6,figsize=(7,6)) #, 

    for i in range(1,6):
        gt_img = scipy.misc.imread(GT_HR_IMAGES % i)
        vdsr_img = scipy.misc.imread(VDSR_SR_IMAGES % vdsr_labels[i-1])
        moremnas_imgs = []
        for k in range(4):
            moremnas_imgs.append(scipy.misc.imread(MOREMNAS_SR_IMAGES % (moremnas_models[k],i)))

        imgs = [gt_img, vdsr_img] + moremnas_imgs

        region = REGIONS[i-1]
        [x1,y1], [x2,y2] = region
        for j in range(6):
            # print(imgs[j].shape, x1,y1, x2,y2)
            axes[i-1][j].imshow(imgs[j][x1:x2,y1:y2,:])
            axes[i-1][j].set_title(METHODS[j],fontsize='small')
            axes[i-1][j].axis('off')
            axes[i-1][j].set_aspect('equal')

    plt.tight_layout(pad=0)
    plt.subplots_adjust(hspace=0.3,wspace=0)
    
    plt.savefig('sr_comparison_x2.png')
    plt.show()
    

if __name__ == '__main__':
    plot_sr_comparison()
    


