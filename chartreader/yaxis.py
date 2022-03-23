import os
import cv2

# TODO (jonik): Lea braucht nur Striche bei de Zoihn
# Spalte links von da y-Achse von unten durchgeh, Obstände zwischen graue Pixel (Logarithmus-Striche) messen.
# Soboid da Obstond greßa is ois da vorherige, wiss ma, dass do a Zoih daneben steht und speichern den y-Wert von dem Strich fiad Lea.

class LogAxis:
    """
        Class for 10-Logarithm-Values on YAxis

        img {cv2.image} -- input image containing yaxis
        values {[number, number]} -- list for log-values on each row/y-axis or preciser
        valuesNoOffset {[number, number]} -- list for log-values on each row/y-axis or preciser with no Offset (according to pixel values on image)
    """

    originHeight = -72
    originGrayVal = 178
    unitStepGrayVal = 160

    def __init__(self, img):
        self.__img = img
        self.__values = self.getYAxisValuesOffset()
        self.__valuesNoOffset = self.getYAxisValues()

    def setValues(self, val):
        self.__values = val

    def getValues(self):
        return self.__values

    def delValues(self):
        del self.__values

    values = property(fget=getValues, fset=setValues, fdel=delValues, doc=None)

    def setValuesNoOffset(self, val):
        self.__valuesNoOffset = val

    def getValuesNoOffset(self):
        return self.__valuesNoOffset

    def delValuesNoOffset(self):
        del self.__valuesNoOffset

    valuesNoOffset = property(fget=getValuesNoOffset, fset=setValuesNoOffset, fdel=delValuesNoOffset, doc=None)

    def getOriginXPos(self):
        gray = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
        width = gray.shape[1]
        origin_x_pos = -1
        for i in range(width):
            if gray[self.originHeight, i] == self.originGrayVal:
                origin_x_pos = i

        return origin_x_pos

    def getYAxisValues(self):
        origin_x_pos = self.getOriginXPos()
        gray = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
        height = gray.shape[0]

        axis_end_y = -1
        for i in range(height + self.originHeight, 0, -1): # Spalte von da y-Achse wird von unten noch oben durch gonga (Werte umdraht weil links oben = 0/0, height + weil originHeight negativ)
            if gray[i, origin_x_pos] == 255: # Wonn d Achse aufhead, oiso da Grauwert s erste moi weiß is
                axis_end_y = i
                break

        axis_values = [*range(axis_end_y, height - (self.originHeight + 1))]

        # cv2.imshow('img', self.__img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        return axis_values

    def getYAxisUnitSteps(self):
        x_pos = self.getOriginXPos() - 1
        gray = cv2.cvtColor(self.__img, cv2.COLOR_BGR2GRAY)
        height = gray.shape[0]

        axisValues = self.getYAxisValuesOffset()
        axisValues.reverse()
        print(axisValues)

        oldDiff = 0
        curDiff = 0
        lastYValue = 0
        unitSteps = []

        for i in axisValues:
            if gray[i, x_pos] == self.unitStepGrayVal:
                oldDiff = curDiff
                curDiff = lastYValue - i
                if curDiff > oldDiff:
                    unitSteps.push(i)
                lastYValue = i

    def getYAxisValuesOffset(self):
        values = self.getYAxisValues()
        for i in values:
            i = i - self.originHeight
        return values



# 200 von xachse
# 255 * log()
# 255*log(wert)=y
# wert= 10^((1000+y)/255)
# wert = 10^((756+y)/255)

# 0 = 648
# 1 = 639
# 2 = 384
# d = 264
# 9

# x = 100

# hobs do eine do, damits nd beim import ausgführt wird
if __name__ == "__main__":
    for root, dirs, files in os.walk('../docs/Beispiele'):
        for filename in files:
            if filename.endswith('.png'):
                imgPath = os.path.join(root, filename)
                axis = LogAxis(cv2.imread(imgPath))
                axis.getYAxisUnitSteps()
