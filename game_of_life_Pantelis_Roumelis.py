#In this programm we creating the game of life 
'''The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
It is a zero-player game, 
meaning that its evolution is determined by its initial state, requiring no further input'''

import pygame
from pygame.locals import *
import random
import time
def main():

	exit = False
	currentCells = FIRST_GEN_CELLS
	nextCells = []
	SCREEN.fill(BLACK)
	DrawCells(BLOCK_SIZE, currentCells, WINDOW_WIDTH, WINDOW_HEIGHT)
	pygame.display.update()
	time.sleep(0.5)

	while not exit:
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit = True
			if event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					exit = True

		SCREEN.fill(BLACK)

		
		nextCells = CountNeighbours(BLOCK_SIZE, currentCells, WINDOW_WIDTH, WINDOW_HEIGHT)
		currentCells = nextCells

		 
		DrawCells(BLOCK_SIZE, currentCells, WINDOW_WIDTH, WINDOW_HEIGHT)
		pygame.display.update()

		CLOCK.tick(UPDATE_RATE)
	pygame.quit()

def CountNeighbours(cellSize, cells, width, height):
	newCells = []


	for x in range(int(width/cellSize)):
		for y in range(int(height/cellSize)):
			Neighbours = 0
			if (x+1, y) in cells:
				Neighbours += 1
			if (x-1, y) in cells:
				Neighbours += 1
			if (x, y+1) in cells:
				Neighbours += 1
			if (x, y-1) in cells:
				Neighbours += 1
			if (x+1, y+1) in cells:
				Neighbours += 1
			if (x-1, y-1) in cells:
				Neighbours += 1
			if (x+1, y-1) in cells:
				Neighbours += 1
			if (x-1, y+1) in cells:
				Neighbours += 1
			
			if (x,y) in cells:
				if Neighbours == 3:
					newCells.append((x,y))
				elif Neighbours == 2:
					newCells.append((x,y))
			else:
				if Neighbours == 3:
					newCells.append((x,y))

	return newCells
#we are drawing the cells 
def DrawCells(cellSize, cells, width, height):

	



	for x in range(int(width/cellSize)):
		for y in range(int(height/cellSize)):
			if (x,y) in cells:
				cell = pygame.Rect(x*cellSize, y*cellSize, 
					cellSize, cellSize)
				pygame.draw.rect(SCREEN, ColorGen(), cell)


def SeedGenerator(numberOfCells, width, height, cellSize):
	
	

	

	seed = []

	maxX = width/cellSize
	maxY = height/cellSize

	for cell in range(numberOfCells):
		x = random.randrange(0, maxX+1)
		y = random.randrange(0, maxY+1)

		seed.append((x,y))

	return seed


def ColorGen():

	
	
	color = ()

	red = random.randrange(30, 256)
	green = random.randrange(30, 256)
	blue = random.randrange(30, 256)

	color = (red, green, blue)

	return color



BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
WHITE = (255, 255, 255)

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BLOCK_SIZE = 20

UPDATE_RATE = 2

pygame.init()

SCREEN = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption('Conway\'s Game of Life')
pygame.mouse.set_visible(0)
CLOCK = pygame.time.Clock()


FIRST_GEN_CELLS = SeedGenerator(100, WINDOW_WIDTH, WINDOW_HEIGHT, BLOCK_SIZE)

#this is the main function of the programm
if __name__ == "__main__":
	main()
