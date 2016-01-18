#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import gtk


BACK = [1,1,1,1]
FRONT = [0,0,0,0.8]
LIGHT = [0,0,0,0.2]
CYAN = [0,0.5,0.5,0.2]
BLUE = [0,0,1,0.3]


NMAX = 10**6
SIZE = 540
ONE = 1./SIZE
LINEWIDTH = ONE*1.1

INIT_NUM = 3

STP = ONE *7

FRAC_STP = ONE*3.


WIND_ANGLE_STP = 1



def show(render,wind):

  render.clear_canvas()
  render.set_line_width(ONE)
  render.ctx.set_source_rgba(*FRONT)

  xy = wind.xy
  n = wind.n

  for x in xy[:n,:]:
    render.circle(*x, r=2*ONE, fill=True)

  for i,p in enumerate(wind.p[:n]):
    if p>-1:
      # x = xy[p,:].flatten()
      render.ctx.move_to(*xy[p,:].flatten())
      render.ctx.line_to(*xy[i,:].flatten())
      render.ctx.stroke()


def main():

  from render.render import Animate
  from numpy.random import random
  from numpy import array
  from modules.wind import Wind

  W = Wind(
    NMAX,
    SIZE,
    STP,
    WIND_ANGLE_STP
  )

  # W.rnd_seed(INIT_NUM)
  W.seed(array([[0.5,0.5]]))

  def wrap(render):

    show(render,W)
    render.write_to_png('{:04d}.png'.format(W.i))
    res = W.step()

    return res

  render = Animate(SIZE, BACK, FRONT, wrap)

  def __write_and_exit(*args):
    gtk.main_quit(*args)
    show(render,W)
    render.write_to_png('./res/exit.png')

  render.window.connect("destroy", __write_and_exit)

  gtk.main()


if __name__ == '__main__':

  main()

