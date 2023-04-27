import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def applyGammaCorrection(img, c, y):
    newImg = img.copy()

    if(len(newImg.shape) == 3):
        print('Colored image')
        for i in range(0, len(newImg)):
            for j in range(0, len(newImg[i])):
                newImg[i][j][0] = round(c * ((newImg[i][j][0] / 255) ** y) * 255)
                newImg[i][j][1] = round(c * ((newImg[i][j][1] / 255) ** y) * 255)
                newImg[i][j][2] = round(c * ((newImg[i][j][2] / 255) ** y) * 255)

    elif(len(newImg.shape) == 2):
        print('Greyscale image')
        for i in range(0, len(newImg)):
            for j in range(0, len(newImg[i])):
                newImg[i][j] = round(c * ((newImg[i][j] / 255) ** y) * 255)

    else:
        print('Wrong image format')
        return

    source_figure = plt.figure(1)
    plt.imshow(img)
    plt.grid(False)
    plt.axis(False)
    plt.suptitle('Source image')
    source_figure.show()

    corrected_figure = plt.figure(2)
    plt.imshow(newImg)
    plt.grid(False)
    plt.axis(False)
    plt.suptitle('Gamma corrected image')
    corrected_figure.show()

    print('Press enter to quit the program...')
    input()

def main():
    img = mpimg.imread('artsiomka_v_tanke.jpg').copy()

    c = float(input('Enter c: '))
    y = float(input('Enter y: '))

    applyGammaCorrection(img, c, y)

main()