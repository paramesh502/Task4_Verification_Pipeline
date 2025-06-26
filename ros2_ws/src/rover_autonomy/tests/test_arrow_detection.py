import unittest
import cv2
import numpy as np

def detect_arrow(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)
        if len(approx) == 4:
            area = cv2.contourArea(cnt)
            if 10000 < area < 50000:
                return True
    return False

class TestArrowDetection(unittest.TestCase):
    def test_arrow_present(self):
        image = np.ones((480, 640, 3), dtype=np.uint8) * 255
        cv2.rectangle(image, (100, 100), (200, 200), (0, 0, 0), -1)
        self.assertTrue(detect_arrow(image))

    def test_no_arrow(self):
        image = np.ones((480, 640, 3), dtype=np.uint8) * 255
        self.assertFalse(detect_arrow(image))

if __name__ == '__main__':
    unittest.main()
