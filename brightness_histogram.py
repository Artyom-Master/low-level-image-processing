import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def drawBrightnessHistogram(img):
    histData = [0] * 256

    if(len(img.shape) == 3):
        print('Colored image')
        for i in range(0, len(img)):
            for j in range(0, len(img[i])):
                currentIndex = round(0.212 * img[i][j][0]
                                + 0.715 * img[i][j][1]
                                + 0.072 * img[i][j][2])
                histData[currentIndex] += 1

    elif(len(img.shape) == 2):
        print('Greyscale image')
        for i in range(0, len(img)):
            for j in range(0, len(img[i])):
                histData[img[i][j]] += 1
    
    else:
        print('Wrong image format')
        return

    fig, axs = plt.subplots(2)
    axs[0].imshow(img)
    axs[0].grid(False)
    axs[0].axis(False)
    axs[0].set_title('Source image')
    axs[1].bar(range(0, len(histData)), histData)
    axs[1].set_title('Brightness histogram (formula: Y=0.212*R+0.715*G+0.072*B)')

    plt.show()

def main():
    img = mpimg.imread('artsiomka_v_tanke.jpg').copy()
    drawBrightnessHistogram(img)

main()