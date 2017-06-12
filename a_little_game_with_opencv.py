# -*- coding=utf-8 -*-
from __future__ import print_function
import cv2
import numpy.random as random
import numpy as np

from tkMessageBox import askyesno

DEFAULT_WINDOW_NAME = 'find right door'

class find_right_door(object):
	"""docstring for find_right_door"""
	def __init__(self, window_name=None):
		self.right = random.randint(0, 3)
		self.window_name = window_name if window_name else DEFAULT_WINDOW_NAME
		self.key = 0

	def mouse_ops(self, event, x, y, flags, param):
		if event == cv2.EVENT_LBUTTONDOWN:
			print('{}, {}'.format(x, y))
			self.show_answer(x, y)

	def show_answer(self, x, y):
		result = "you're right! do u wanna continue?" if x / 200 == self.right else "you're wrong! do u wanna continue?"
		if askyesno('continue', result):
			self.start()
		else:
			self.close()

	def show_game(self):
		game_view = np.zeros((400, 600, 3), dtype=np.uint8) + 255
		first_door = np.array([[(0, 0), (199, 0), (199, 399), (0, 399)]])
		cv2.fillPoly(game_view, first_door, (255, 0, 0))
		
		second_door = np.array([[(200, 0), (399, 0), (399, 399), (200, 399)]])
		cv2.fillPoly(game_view, second_door, (0, 255, 0))
		
		third_door = np.array([[(400, 0), (599, 0), (599, 399), (400, 399)]])
		cv2.fillPoly(game_view, third_door, (0, 0, 255))
		
		cv2.namedWindow(self.window_name)
		cv2.setMouseCallback(self.window_name, self.mouse_ops)
		while self.key != 27:
			cv2.imshow(self.window_name, game_view)
			self.key = cv2.waitKey()

	def start(self):
		self.right = random.randint(0, 3)
		print('hello, right door is {}'.format(self.right))
		self.show_game()

	def close(self):
		print('goodbye')
		self.key = 27
		
if __name__ == '__main__':
	new_game = find_right_door()
	new_game.start()