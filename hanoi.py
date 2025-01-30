import pygame
import sys
import time
import math

def center_window(window):
    window.update_idletasks() 
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"+{x}+{y}")

pygame.init()

WIDTH, HEIGHT = 960, 600
BACKGROUND_COLOR = (34, 34, 51)
DISK_COLORS = [(255, 102, 102), (102, 204, 255), (255, 178, 102), (178, 102, 255), (102, 255, 178)]
PEG_COLOR = (200, 200, 200)
BASE_COLOR = (70, 70, 90)
TEXT_COLOR = (240, 240, 240)
BUTTON_COLOR = (100, 100, 150)
HIGHLIGHT_COLOR = (150, 150, 200)
MESSAGE_COLOR = (255, 255, 0)
FPS = 60
FONT = pygame.font.SysFont("Arial", 24)
INSTRUCTION_FONT = pygame.font.SysFont("Arial", 18)

peg_positions = [(200, 500), (400, 500), (600, 500)]
disks = []
timer_start = time.time()

animation_speed = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower of Hanoi")
clock = pygame.time.Clock()

move_sound = pygame.mixer.Sound('move_sound.wav')
win_sound = pygame.mixer.Sound('win_sound.wav')

class Disk:
    def __init__(self, width, height, color, peg):
        self.width = width
        self.height = height
        self.color = color
        self.peg = peg
        self.rect = pygame.Rect(0, 0, width, height)
        self.update_position()

    def update_position(self):
        peg_x, peg_y = peg_positions[self.peg]
        disk_count = sum(d.peg == self.peg for d in disks)
        self.rect.midtop = (peg_x, peg_y - disk_count * self.height)

    def draw(self, selected=False):
        shadow_rect = self.rect.copy()
        shadow_rect.move_ip(3, 3)
        pygame.draw.rect(screen, (20, 20, 20), shadow_rect, border_radius=5)
        pygame.draw.rect(screen, self.color, self.rect, border_radius=5)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2, border_radius=5)
        if selected:
            pygame.draw.rect(screen, (255, 255, 0), self.rect, 3, border_radius=5)

def create_disks(num_disks):
    global disks
    disks = []
    disk_height = 20
    max_disk_width = 150
    for i in range(num_disks):
        width = max_disk_width - i * 20
        color = DISK_COLORS[i % len(DISK_COLORS)]
        disks.append(Disk(width, disk_height, color, 0))

def ease_out_quad(t, b, c, d):
    t /= d
    return -c * t * (t - 2) + b

undo_stack = []
message = ""
message_timer = 0

def move_disk(from_peg, to_peg):
    global message, message_timer
    from_disks = [disk for disk in disks if disk.peg == from_peg]
    to_disks = [disk for disk in disks if disk.peg == to_peg]

    if not from_disks:
        return

    top_disk = from_disks[-1]

    if not to_disks or to_disks[-1].width > top_disk.width:
        undo_stack.append((top_disk.peg, to_peg))
        animate_disk(top_disk, to_peg)
        top_disk.peg = to_peg
        top_disk.update_position()
        move_sound.play()
        message = ""
    else:
        message = "Invalid move: You cannot place a larger disk on a smaller one."
        message_timer = time.time()

def undo_move():
    if undo_stack:
        last_move = undo_stack.pop()
        move_disk(last_move[1], last_move[0])

def animate_disk(disk, target_peg):
    target_x, target_y = peg_positions[target_peg]
    start_x, start_y = disk.rect.midtop

    mid_y = 100
    duration = 20

    for t in range(duration):
        fraction = t / duration
        x = ease_out_quad(fraction, start_x, target_x - start_x, 1)
        y = ease_out_quad(fraction, start_y, mid_y - start_y, 1)
        disk.rect.midtop = (x, y)
        draw_game()
        clock.tick(FPS)

    for t in range(duration):
        fraction = t / duration
        x = ease_out_quad(fraction, target_x, 0, 1)
        y = ease_out_quad(fraction, mid_y, target_y - mid_y, 1)
        disk.rect.midtop = (x, y)
        draw_game()
        clock.tick(FPS)

def draw_game():
    for i in range(HEIGHT):
        shade = 34 + i * (255 - 34) // HEIGHT
        pygame.draw.line(screen, (shade, shade, shade), (0, i), (WIDTH, i))

    pygame.draw.rect(screen, BASE_COLOR, (50, 550, 700, 10))
    for peg_x, peg_y in peg_positions:
        pygame.draw.rect(screen, PEG_COLOR, (peg_x - 5, peg_y - 150, 10, 200))
    for disk in disks:
        disk.draw(selected=(disk == selected_disk))
    elapsed_time = time.time() - timer_start
    display_text(f"Time: {int(elapsed_time)} seconds", 20, 20)
    display_text(f"Moves: {move_count}", WIDTH - 150, 20)

    if message and time.time() - message_timer < 3:
        display_message(message, WIDTH // 2, 40)

    if check_win():
        display_win_screen()
    pygame.display.flip()

def display_text(text, x, y):
    render = FONT.render(text, True, TEXT_COLOR)
    screen.blit(render, (x, y))

def display_message(text, x, y):
    render = FONT.render(text, True, MESSAGE_COLOR)
    rect = render.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(render, rect.topleft)

def check_win():
    return all(disk.peg == 2 for disk in disks)

def display_win_screen():
    win_sound.play()
    screen.fill(BACKGROUND_COLOR)
    display_text("Congratulations! You Win!", WIDTH // 2 - 150, HEIGHT // 2 - 50)

    play_again_button = pygame.Rect(WIDTH // 2 - 75, HEIGHT // 2 + 20, 150, 50)
    pygame.draw.rect(screen, BUTTON_COLOR, play_again_button)
    display_text("Play Again", WIDTH // 2 - 60, HEIGHT // 2 + 35)

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    main_menu()
                    waiting_for_input = False

def main_menu():
    screen.fill(BACKGROUND_COLOR)
    display_text("Select Difficulty:", WIDTH // 2 - 150, HEIGHT // 2 - 100)

    buttons = []
    for i, num_disks in enumerate(range(5, 8)):
        button = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 50 + i * 60, 100, 40)
        buttons.append((button, num_disks))
        pygame.draw.rect(screen, BUTTON_COLOR, button)
        display_text(f"{num_disks} Disks", button.x + 15, button.y + 10)

    pygame.display.flip()

    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button, num_disks in buttons:
                    if button.collidepoint(event.pos):
                        create_disks(num_disks)
                        global move_count, timer_start
                        move_count = 0
                        timer_start = time.time()
                        waiting_for_input = False

def main():
    global selected_disk, move_count, is_paused, message
    main_menu()
    move_count = 0
    is_paused = False
    selected_disk = None
    message = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    undo_move()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for disk in reversed(disks):
                    if disk.rect.collidepoint(pos):
                        if not selected_disk or disk.peg == selected_disk.peg:
                            selected_disk = disk
                            break
            elif event.type == pygame.MOUSEBUTTONUP and selected_disk:
                pos = pygame.mouse.get_pos()
                for i, (peg_x, _) in enumerate(peg_positions):
                    if abs(pos[0] - peg_x) < 50:
                        move_disk(selected_disk.peg, i)
                        move_count += 1
                        break
                selected_disk = None

        draw_game()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

center_window(screen)