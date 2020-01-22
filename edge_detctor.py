from skimage import data, io, filters
from matplotlib import pyplot as plt

def main():
    #image = data.coins()
    image = io.imread('samolot00.jpg', as_gray=True)
    gauss = filters.gaussian(image, sigma=1)
    edges = filters.sobel(gauss)
    io.imshow(edges)
    plt.show()
    
main()
