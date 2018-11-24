import cv2
import numpy as np
from robot.api import logger
from robot.errors import ExecutionFailed

class ImageComparison:
    """
    Library for comparing images. It can find an image in template.

    = Table of contents =

    - Keywords

    """

    ROBOT_LIBRARY_VERSION = 1.0
    ROBOT_LIBRARY_SCOPE = 'TEST CASE'
    TRESHOLD = 0.8

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
        self.threshold = float(treshold)
        loc = np.where(self.res >= self.threshold)
        if any(map(len, loc)):
            logger.info('Template ' + template + ' found.')
            return True
        logger.error("Template " + template + "has not been found.")
        raise ExecutionFailed("Template has not been found.")

    def find_images(self, templates, screenshot, treshold=TRESHOLD):
        """
        Returns True if a template has been found in screenshot. 

        Example:

        | ${result} | Find In Template | @{templates} | screenshot.png | 0.7 |

        """
        result = 1
        for template in templates:
            if not self.find_in_template(template, screenshot, treshold):
                result = 0
        if result == 0:
            logger.error("Template has not been found.")
            raise ExecutionFailed("Template has not been found.")
        return result

