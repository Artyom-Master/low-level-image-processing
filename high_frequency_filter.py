import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def getNewValueFromMatrixes(m1, m2):
    return (m1[0][0] * m2[0][0] + m1[0][1] * m2[0][1] + m1[0][2] * m2[0][2]
            + m1[1][0] * m2[1][0] + m1[1][1] * m2[1][1] + m1[1][2] * m2[1][2]
            + m1[2][0] * m2[2][0] + m1[2][1] * m2[2][1] + m1[2][2] * m2[2][2])

def applyHighFrequencyFilter(img, h):
    newImg = img.copy()

    if(len(newImg.shape) == 3):
        print('Colored image')
        for i in range(0, len(newImg)):
            i_prev = 1
            i_next = 1
            
            if i == 0:
                i_prev = 0

            if i == len(newImg) - 1:
                i_next = 0
            
            for j in range(0, len(newImg[i])):
                j_prev = 1
                j_next = 1

                if j == 0:
                    j_prev = 0

                if j == len(newImg[i]) - 1:
                    j_next = 0

                for k in range(0, 3):
                    newImg[i][j][k] = getNewValueFromMatrixes([[img[i - i_prev][j - j_prev][k], img[i - i_prev][j][k], img[i - i_prev][j + j_next][k]]
                                                           , [img[i][j - j_prev][k], img[i][j][k], img[i][j + j_next][k]]
                                                           , [img[i + i_next][j - j_prev][k], img[i + i_next][j][k], img[i + i_next][j + j_next][k]]], h)

    elif(len(newImg.shape) == 2):
        print('Greyscale image')
        for i in range(0, len(newImg)):
            for j in range(0, len(newImg[i])):
                newImg[i][j] = getNewValueFromMatrixes([[img[i - i_prev][j - j_prev], img[i - i_prev][j], img[i - i_prev][j + j_next]]
                                                           , [img[i][j - j_prev], img[i][j], img[i][j + j_next]]
                                                           , [img[i + i_next][j - j_prev], img[i + i_next][j], img[i + i_next][j + j_next]]], h)

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

def printMatrix(matrix, matrixName):
    print('\t\t', matrix[0][0], ' ', matrix[0][1], ' ', matrix[0][2])
    print(matrixName, ' =\t', matrix[1][0], ' ', matrix[1][1], ' ', matrix[1][2])
    print('\t\t', matrix[2][0], ' ', matrix[2][1], ' ', matrix[2][2])

def main():
    img = mpimg.imread('artsiomka_v_tanke.jpg').copy()

    h1 = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]
    h2 = [[0, -1, 0], [-1, 5, -1], [0, -1, 0]]
    h3 = [[1, -2, 1], [-2, 5, -2], [1, -2, 1]]

    print('Choose filter coefficients:')
    printMatrix(h1, '1')
    printMatrix(h2, '2')
    printMatrix(h3, '3')
    choice = int(input())
    
    if choice == 1:
        applyHighFrequencyFilter(img, h1)
    elif choice == 2:
        applyHighFrequencyFilter(img, h2)
    elif choice == 3:
        applyHighFrequencyFilter(img, h3)

main()