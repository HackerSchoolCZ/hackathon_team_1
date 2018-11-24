import cv2
import numpy as np
from robot.api import logger

class ImageComparison:
    """
    Library for comparing images. It can find an image in template.

    = Table of contents =

    - Keywords

    """

    ROBOT_LIBRARY_VERSION = 1.0
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'
    TRESHOLD = 0.8

    def __init__(self):
        pass

    def find_in_template(self, template, screenshot, treshold=TRESHOLD):
        """
        Returns True if a template has been found in screenshot. 

        Example:

        | ${result} | Find In Template | template.png | screenshot.png | 0.7 |

        """

        logger.info('Template:' + template)
        logger.info('Screenshot:' + screenshot)
        self.template = cv2.imread(template, 0)
        self.img = cv2.imread(screenshot, 0)
        self.res = cv2.matchTemplate(self.img, self.template, cv2.TM_CCOEFF_NORMED)
        self.threshold = treshold
        loc = np.where(self.res >= self.threshold)
        if any(map(len, loc)):
            return True
        return False



if __name__ == '__main__':
    test = ImageComparison()
    print(test.find_in_template('template.png', 'screenshot.png', 1.0))
    print(test.find_in_template('python.jpg', 'screenshot.png', 1.0))
