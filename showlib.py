import matplotlib.pyplot as plt

def show1plt(img,n=""):
    plt.figure(figsize=(2,2));
    plt.imshow(img, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.show()

    
def show2plt(img,img2,n1="",n2=""):
    fig =plt.figure(figsize=(4,2));
    ax6=fig.add_subplot(121)
    cax6 = ax6.imshow(img, vmin=0, vmax=255)
    #fig.colorbar(cax6)

    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    axs=fig.add_subplot(122)
    cax2 = axs.imshow(img2, vmin=0, vmax=255)
    #fig.colorbar(cax2)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.show()


def show3plt(img,img2,img3,n1="",n2="",n3=""):
    plt.figure(figsize=(6,2));
    plt.subplot(131)
    plt.imshow(img, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(132)
    plt.imshow(img2, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.subplot(133)
    plt.imshow(img3, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n3);
    plt.show()

    
def show4plt(img,img2,img3,img4,n1="",n2="",n3="",n4=""):
    plt.figure(figsize=(8,2));
    plt.subplot(141)
    plt.imshow(img, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(142)
    plt.imshow(img2, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.subplot(143)
    plt.imshow(img3, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n3);
    plt.subplot(144)
    plt.imshow(img4, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n4);
    plt.show()

    
def show5plt(img,img2,img3,img4,img5,n1="",n2="",n3="",n4="",n5=""):
    plt.figure(figsize=(10,2));
    plt.subplot(151)
    plt.imshow(img, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(152)
    plt.imshow(img2, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.subplot(153)
    plt.imshow(img3, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n3);
    plt.subplot(154)
    plt.imshow(img4, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n4);
    plt.subplot(155)
    plt.imshow(img5, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n5);
    plt.show()

    
def show6plt(img,img2,img3,img4,img5,img6,n1="",n2="",n3="",n4="",n5="",n6=""):
    plt.figure(figsize=(12,2));
    plt.subplot(161)
    plt.imshow(img, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(162)
    plt.imshow(img2, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.subplot(163)
    plt.imshow(img3, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n3);
    plt.subplot(164)
    plt.imshow(img4, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n4);
    plt.subplot(165)
    plt.imshow(img5, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n5);
    plt.subplot(166)
    plt.imshow(img6, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n6);
    plt.show()

    
    
def show7plt(img,img2,img3,img4,img5,img6,img7,n1="",n2="",n3="",n4="",n5="",n6="",n7=""):
    plt.figure(figsize=(14,2));
    plt.subplot(171)
    plt.imshow(img, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(172)
    plt.imshow(img2, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.subplot(173)
    plt.imshow(img3, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n3);
    plt.subplot(174)
    plt.imshow(img4, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n4);
    plt.subplot(175)
    plt.imshow(img5, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n5);
    plt.subplot(176)
    plt.imshow(img6, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n6);
    plt.subplot(177)
    plt.imshow(img7, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n7);
    plt.show()

    
def show8plt(img,img2,img3,img4,img5,img6,img7,img8,n1="",n2="",n3="",n4="",n5="",n6="",n7="",n8=""):
    plt.figure(figsize=(16,2));
    plt.subplot(181)
    plt.imshow(img, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n1);
    plt.subplot(182)
    plt.imshow(img2, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n2);
    plt.subplot(183)
    plt.imshow(img3, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n3);
    plt.subplot(184)
    plt.imshow(img4, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n4);
    plt.subplot(185)
    plt.imshow(img5, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n5);
    plt.subplot(186)
    plt.imshow(img6, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n6);
    plt.subplot(187)
    plt.imshow(img7, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n7);
    plt.subplot(188)
    plt.imshow(img8, vmin=0, vmax=255)
    plt.xticks([]);
    plt.yticks([]);
    plt.title(n8);
    plt.show()
