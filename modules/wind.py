# -*- coding: utf-8 -*-

from __future__ import print_function

from numpy import pi
from numpy import array
from numpy import zeros
from numpy import arange
from numpy import reshape
from numpy import row_stack
from numpy.random import random
from numpy.random import randint
from numpy.linalg import norm
from numpy import cos
from numpy import sin
from numpy import arctan2
from collections import defaultdict


TWOPI = pi*2
HPI = pi*0.5


class Wind(object):

  def __init__(
      self,
      nmax,
      size,
      wind_angle_stp
    ):

    self.nmax = nmax
    self.size = size
    self.wind_angle_stp = wind_angle_stp
    self.i = 0
    self.__init_data()

  def __init_data(self):

    self.angle = random()*TWOPI
    self.xy = zeros((self.nmax,2), 'float')
    self.p = zeros((self.nmax,1), 'int')-1
    self.n = 0

  def seed(self,num):

    n = self.n
    self.xy[n:n+num,:] = random((num,2))
    self.n = n + num

    return self.n

  def step(self, dbg=False):

    self.i += 1

    return True

