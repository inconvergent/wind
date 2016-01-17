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
SIZE = 1500
ONE = 1./SIZE
LINEWIDTH = ONE*1.1

INIT_NUM = 1

FRAC_STP = ONE*3.


WIND_ANGLE_STP = 0.1



def show(render,wind):

  # def draw_sources():
    # for i,s in enumerate(sources):
      # if i not in fractures.visited:
        # render.circle(*s, r=4*ONE, fill=True)
    # render.ctx.line_to(*sources[c,:])
      # render.ctx.stroke()
      # render.ctx.move_to(*sources[start,:])

  render.clear_canvas()

  # render.ctx.set_source_rgba(*LIGHT)
  # draw_sources()


def main():

  from render.render import Animate
  from numpy.random import random
  from modules.wind import Wind

  W = Wind(
    NMAX,
    SIZE,
    WIND_ANGLE_STP
  )

  def wrap(render):

    # show(render,F)
    # render.write_to_png('{:04d}.png'.format(F.i))

    res = W.step()

    return res

  render = Animate(SIZE, BACK, FRONT, wrap)

  # def __write_svg_and_exit(*args):
    # gtk.main_quit(*args)
    # show(render,F)
    # render.write_to_png('./res/on_exit.png')

  render.window.connect("destroy", __write_svg_and_exit)

  gtk.main()


if __name__ == '__main__':

  main()

