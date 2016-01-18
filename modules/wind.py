# -*- coding: utf-8 -*-

from __future__ import print_function

from numpy import pi
from numpy import array
from numpy import zeros
from numpy import arange
from numpy import reshape
from numpy import logical_and
from numpy import column_stack
from numpy.random import random
from numpy.random import randint
from numpy.linalg import norm
from scipy.spatial import cKDTree as kdt
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
      stp,
      angle_stp,
      angle_local_stp
    ):

    self.i = 0
    self.nmax = nmax
    self.size = size
    self.stp = stp
    self.angle_stp = angle_stp
    self.angle_local_stp = angle_local_stp

    self.__init_data()

  def __init_data(self):

    self.angle = random()*TWOPI
    self.xy = zeros((self.nmax,2), 'float')
    self.p = zeros((self.nmax,1), 'int')-1
    self.n = 0

  def rnd_seed(self,num):

    n = self.n
    self.xy[n:n+num,:] = random((num,2))
    self.n = n + num

    return self.n

  def seed(self,xy):

    n = self.n
    self.xy[n:n+len(xy),:] = xy
    self.n = n + len(xy)

    return self.n

  def step(self, dbg=False):

    self.i += 1
    n = self.n
    stp = self.stp

    self.angle += (1-2*random())*self.angle_stp
    angle = self.angle + (1-2*random(n))*self.angle_local_stp

    xy = self.xy[:n,:]
    p = self.p[:n,:]

    tree = kdt(xy)

    new_p = xy + column_stack([cos(angle),sin(angle)]) * stp

    if len(new_p)>0:
      ind = tree.query_ball_point(new_p, stp)
      mask = [i for i,v in enumerate(ind) if not v]

      if mask:

        new_num = len(mask)
        self.p[n:n+new_num] = reshape(mask,(-1,1))
        self.xy[n:n+new_num,:] = new_p[mask,:]

        inside = n+(logical_and(self.xy[n:n+new_num,:]<1.0,
                                self.xy[n:n+new_num,:]>0.0).sum(axis=1)==2)\
          .nonzero()[0]
        li = len(inside)
        self.xy[n:n+li,:] = self.xy[inside,:]
        self.p[n:n+li] = self.p[inside]
        self.n = n + li

    return True

