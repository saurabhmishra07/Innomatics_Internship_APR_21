import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import cv2

data=pd.read_csv("Datas.csv")
print(data)

"""Means  $ Mean=Sum of all outcomes/Total outcomes$
"""
img2=cv2.imread("Mean.png",cv2.IMREAD_GRAYSCALE)
plt.imshow(img2,cmap="gray"),plt.axis("off")
plt.title("Means")
plt.show()

Means=(np.mean(data.Annual_HH_Income))
print("Mean of data is",Means)

"""Median   $Median=the median is the value separating the higher half
                    from the lower half of a data sample, a population, or a
                     probability distribution. $"""
img3=cv2.imread("Median.png",cv2.IMREAD_GRAYSCALE)
plt.imshow(img3,cmap="gray"),plt.axis("off")
plt.title("Medians")
plt.show()

Medians=np.median(data.Mthly_HH_Income)
print("Median of data is",Medians)

"""Mode= = =The mode is the value that appears most frequently in
            a data set. A set of data may have one mode, more than one mode,
            or no mode at all. Other popular measures of central tendency 
            include the mean, or the average of a set, and the median, 
            the middle value in a set."""
img4=cv2.imread("Mode.png",cv2.IMREAD_GRAYSCALE)
plt.imshow(img4,cmap="gray"),plt.axis("off")
plt.title("Mode")
plt.show()

Modes=stats.mode(data.Mthly_HH_Expense)
print("Mode of data is",Modes)

Variance="""Variance === variance is the expectation of the squared 
                        deviation of a random variable from its mean."""
img9=cv2.imread("variance.jpg",cv2.IMREAD_GRAYSCALE)
plt.imshow(img9,cmap="gray"),plt.axis("Off")
plt.title("Variance")
plt.show()

Variance=np.var(data.Mthly_HH_Expense)
print("Variace of data is",Variance)

Standard_deviation=  """Standard Deviations"""
img10=cv2.imread("std.png",cv2.IMREAD_GRAYSCALE)
plt.imshow(img10,cmap="gray"),plt.axis("Off")
plt.title("Standard Deviation")
plt.show()

std=np.std(data.Mthly_HH_Expense)
print("Standard deviation of data is",std)

correlation=     """Correlation """
img=cv2.imread("Correlation_Formulas.png",cv2.IMREAD_GRAYSCALE)
plt.imshow(img,cmap="gray"),plt.axis("off")
plt.title("Correlations")
plt.show()


Correlations=(data.corr())
print(Correlations.Mthly_HH_Income)


"""Normal Distribution """
x = np.linspace(1,50,200)
img1=cv2.imread("Normal-Distribution.jpg",cv2.IMREAD_GRAYSCALE)
plt.imshow(img1,cmap="gray"),plt.axis("on")
plt.show()
img5=cv2.imread("ND_graph.png",cv2.IMREAD_GRAYSCALE)
plt.imshow(img5,cmap="gray"),plt.axis("off")
plt.show()
def normal_dist(x, mea, sd):
    prob_density = (np.pi * sd) * np.exp(-0.5 * ((x - mea) / sd) ** 2)
    return prob_density
mea = np.mean(x)
sd = np.std(x)
pdf = normal_dist(x,mea,sd)
plt.plot(x,pdf , color = 'red')
plt.xlabel('Data points')
plt.ylabel('Probability Density')


"""Features of Normal Distribution"""

"""The mean-mode-median is in the center.
It is the mean because it is the ARITHMETIC average of all the scores.
It is the mode because of all the scores the mean score happens MOST often.
It is the median because when the scores are displayed from lowest to highest,
 the mean is the MIDDLE score, the median.
The EXPECTED value is the mean.
The frequency curve is bell shaped.
The bell shape has perfect bilateral symmetry - the left balances exactly 
         with the right.
The score at -2 is balanced by a score at +2 and the frequencies from 0 to +2
         and from 0 to -2 are equal.
The area under the curve from 0 to +2 is exactly the same as the area under 
         the curve from 0 to -2.
Fifty percent of the scores are above the mean and 50% are below the mean.
The probability a score is above the mean is 50% and the probability a score
         is below the mean is 50%"""

#img6=cv2.imread("Features.jpg",cv2.IMREAD_GRAYSCALE)
#plt.imshow(img6,cmap="gray"),plt.axis("Off")
#plt.show()


"""Positive and Negative Skewness"""
""""Negative skewness= = =a negatively skewed (also known as left-skewed) distribution 
                is a type of distribution in which more values are concentrated on 
                the right side (tail) of the distribution graph while the left tail of 
                the distribution graph is longer."""
img7=cv2.imread("Negative-skewed.jpg",cv2.IMREAD_GRAYSCALE)
plt.imshow(img7,cmap="gray"),plt.axis("Off")
plt.title("Negative-Skewness")
plt.show()


"""Positive Skewness= = = A right-skewed distribution has a long right tail.
            Right-skewed distributions are also called positive-skew distributions. 
            That’s because there is a long tail in the positive direction on the
             number line.The mean is also to the right of the peak."""
img8=cv2.imread("Positive-skewed.jpg",cv2.IMREAD_GRAYSCALE)
plt.imshow(img8,cmap="gray"),plt.axis("Off")
plt.title("Positive-Skewness")
plt.show()


"""Effect on Mean, Median and Mode due to Skewness = = =
           generally if the distribution of data is skewed to the Negative,
           the mean is less than the median, which is often less than the mode.
           If the distribution of data is skewed to the Positive, the mode is often
           less than the median, which is less than the mean."""
"""What is Q-Q plot= = = Q Q Plots (Quantile-Quantile plots) are plots of two 
        quantiles against each other. A quantile is a fraction where certain values
         fall below that quantile. For example, the median is a quantile where 50%
          of the data fall below that point and 50% lie above it. 
          The purpose of Q Q plots is to find out if two sets of data come from 
          the same distribution. A 45 degree angle is plotted on the Q Q plot;
           if the two data sets come from a common distribution, the points will fall
            on that reference line."""
img10=cv2.imread("Q-Qplot.png",cv2.IMREAD_GRAYSCALE)
plt.imshow(img10,cmap="gray"),plt.axis("Off")
plt.title("Positive-Skewness")
plt.show()
