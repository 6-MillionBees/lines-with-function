# Arden Boettcher
# 2/11/25
# Pygame Template

import pygame
import config
from random import randint


# Setting up the window
def setup_pygame():
  pygame.init()

  # Setting up the Window
  screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
  pygame.display.set_caption("Lines!!!")

  return screen



def randomize_lines(num_of_lines):
  line_colors = []
  line_starts = []
  line_ends = []
  line_weights = []

  for x in range(num_of_lines):
    line_colors.append((randint(0, 255), randint(0, 255), randint(0, 255)))
    line_starts.append((randint(0, config.WIDTH), randint(0, config.HEIGHT)))
    line_ends.append((randint(0, config.WIDTH), randint(0, config.HEIGHT)))
    line_weights.append(randint(2, 8))

  lines = list(zip(line_ends, line_starts, line_colors, line_weights))
  return lines




def draw_lines(surface, lines):
  for start, end, color, weight in lines:
    pygame.draw.line(surface, color, start, end, weight)



# Main loop
def main():
  global running
  lines = randomize_lines(6)

  screen = setup_pygame()

  # Setting up the clock
  clock = pygame.time.Clock()


  running = True
  while running:

    # Call events
    for event in pygame.event.get():
      # Quits the game when you press the x
      if event.type == pygame.QUIT:
        running = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
        if event.key == pygame.K_SPACE:
          lines = randomize_lines(6)

    # Fills window
    screen.fill(config.WHITE)

    # Draws lines
    draw_lines(screen, lines)

    # Updates the Display
    pygame.display.flip()

    # Limits the framerate

    clock.tick(config.FPS)


  pygame.quit()


# Calls the code
if __name__ == "__main__":
  main()