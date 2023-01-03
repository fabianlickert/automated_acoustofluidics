import pco # camera library
import os # communication with operating system
from skimage import io
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore') # suppress camera warnings 

directory = os.getcwd()

class ControlCamera:
    
    # initialize the connection to the camera
    def __init__(self, delay_time=25, exposure_time=20):

        self.cam = pco.Camera()

        try:
            self.cam.sdk.open_camera()
            self.cam.sdk.set_delay_exposure_time(delay_time, 'ms', exposure_time, 'ms')
            self.cam.configuration = {'timestamp': 'binary & ascii'}
        except:
            print('Failed to setup camera')
                   
    # record a single image
    def record_image(self, name):

        self.cam.record(number_of_images=1, mode='sequence')
        image, meta = self.cam.image()

        io.imsave(name+'.tif',image)

    # record a sequency of multiple images
    def record_movie(self, name, no_images):

        self.cam.record(number_of_images=no_images, mode='sequence')
        images, metadatas = self.cam.images()

        count = 1
        for image in images:
            io.imsave(name+"{0:04d}.tif".format(count),image)
            count += 1

    # record a single image and plot it
    def show_image(self, min_count=0,max_count=2000):
        
        self.cam.record(number_of_images=1, mode='sequence')
        image, meta = self.cam.image()
        #plt.imshow(image, cmap='gray',clim=(min_count,max_count))
        plt.imshow(image)
        plt.axis('off')
        plt.show()    

    # close connection to the camera
    def close(self):
        self.cam.sdk.close_camera()

        