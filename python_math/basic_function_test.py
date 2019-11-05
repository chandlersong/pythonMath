import unittest
from unittest import TestCase

import pandas as pd
from matplotlib import pyplot as plt
import math


class TestFunctionFeature(TestCase):
    def test_plot_linear_function(self):
        # Create a dataframe with an x column containing values from -10 to 10
        df = pd.DataFrame({'x': range(-10, 11)})

        # Define slope and y-intercept
        m = 1.5
        yInt = -2

        # Add a y column by applying the slope-intercept equation to x
        df['y'] = m * df['x'] + yInt

        plt.plot(df.x, df.y, color="grey")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.axhline()
        plt.axvline()

        # label the y-intercept
        plt.annotate('y-intercept', (0, yInt))

        # plot the slope from the y-intercept for 1x
        mx = [0, 1]
        my = [yInt, yInt + m]
        plt.plot(mx, my, color='red', lw=5)

        plt.show()
        print("ok")

    def test_calculate_vale(self):
        print("5th power of 3: {}".format(5 ** 3))  # power
        print("Calculate square root of 25: {}".format(math.sqrt(25)))  # root
        print("Calculate cube root of 64: {}".format(64 ** (1 / 3)))  # root
        print("common log_4(64) : {}".format(math.log(16, 4)))  # log
        print("nature log(ln): {}".format(math.log(10)))  # log
        print("nature log_10(ln): {}".format(math.log10(100)))  # log

    def test_how_to_check_equation(self):
        from random import randint
        x = randint(1, 100)

        self.assertTrue((x ** 2 - 9) == (x - 3) * (x + 3))

    def test_plot_parabola(self):
        def plot_parabola_from_formula(a, b, c):
            import math

            # Get vertex
            print('CALCULATING THE VERTEX')
            print('vx = -b / 2a')

            nb = -b
            a2 = 2 * a
            print('vx = ' + str(nb) + ' / ' + str(a2))

            vx = -b / (2 * a)
            print('vx = ' + str(vx))

            print('\nvy = ax^2 + bx + c')
            print('vy =' + str(a) + '(' + str(vx) + '^2) + ' + str(b) + '(' + str(vx) + ') + ' + str(c))

            avx2 = a * vx ** 2
            bvx = b * vx
            print('vy =' + str(avx2) + ' + ' + str(bvx) + ' + ' + str(c))

            vy = avx2 + bvx + c
            print('vy = ' + str(vy))

            print('\nv = ' + str(vx) + ',' + str(vy))

            # Get +x and -x (showing intermediate calculations)
            print('\nCALCULATING -x AND +x FOR y=0')
            print('x = -b +- sqrt(b^2 - 4ac) / 2a')

            b2 = b ** 2
            ac4 = 4 * a * c
            print('x = ' + str(nb) + '+-sqrt(' + str(b2) + ' - ' + str(ac4) + ')/' + str(a2))

            sr = math.sqrt(b2 - ac4)
            print('x = ' + str(nb) + ' +- ' + str(sr) + ' / ' + str(a2))
            print('-x = ' + str(nb) + ' - ' + str(sr) + ' / ' + str(a2))
            print('+x = ' + str(nb) + ' + ' + str(sr) + ' / ' + str(a2))

            posx = (nb + sr) / a2
            negx = (nb - sr) / a2
            print('-x = ' + str(negx))
            print('+x = ' + str(posx))

            print('\nPLOTTING THE PARABOLA')

            # Create a dataframe with an x column a range of x values to plot
            df = pd.DataFrame({'x': range(round(vx) - 10, round(vx) + 11)})

            # Add a y column by applying the quadratic equation to x
            df['y'] = a * df['x'] ** 2 + b * df['x'] + c

            # get min and max y values
            miny = df.y.min()
            maxy = df.y.max()

            # Plot the line

            plt.plot(df.x, df.y, color="grey")
            plt.xlabel('x')
            plt.ylabel('y')
            plt.grid()
            plt.axhline()
            plt.axvline()

            # Plot calculated x values for y = 0
            plt.scatter([negx, posx], [0, 0], color="green")
            plt.annotate('-x=' + str(negx) + ',' + str(0), (negx, 0), xytext=(negx - 3, 5))
            plt.annotate('+x=' + str(posx) + ',' + str(0), (posx, 0), xytext=(posx - 3, -10))

            # plot the line of symmetry
            sx = [vx, vx]
            sy = [miny, maxy]
            plt.plot(sx, sy, color='magenta')

            # Annotate the vertex
            plt.scatter(vx, vy, color="red")
            plt.annotate('v=' + str(vx) + ',' + str(vy), (vx, vy), xytext=(vx - 1, vy - 10))

            plt.show()

        plot_parabola_from_formula(2, -16, 2)


if __name__ == '__main__':
    unittest.main()
