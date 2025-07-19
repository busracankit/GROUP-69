import pygame
import sys
import math

# --- VERİLER ---
haftalar = [1, 2, 3, 4, 5, 6, 7]
basari_oranlari = [35, 42, 45, 50, 60, 70, 85]

# --- RENKLER ve AYARLAR ---
WIDTH, HEIGHT = 1200, 700
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# --- Pygame Başlat ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 LetStep Gelişim Yolculuğu")
clock = pygame.time.Clock()

# --- GÖRSELLER ---
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

character_walk = [
    pygame.transform.scale(pygame.image.load(f"walk{i}.png"), (80, 80)) for i in range(1, 5)
]

badge = pygame.image.load("badge.png")
badge = pygame.transform.scale(badge, (40, 40))

# --- FONT ---
pixel_font = pygame.font.Font("pixel_font.ttf", 18)

# --- POZİSYON HESABI ---
def get_position(week_index):
    x = 150 + week_index * 140
    y = HEIGHT - (basari_oranlari[week_index] * 5)
    return x, y

path = [get_position(i) for i in range(len(haftalar))]
max_index = basari_oranlari.index(max(basari_oranlari))

# --- ANİMASYON DEĞİŞKENLERİ ---
char_pos = list(path[0])
step_index = 0
speed = 3
walk_frame = 0
walk_timer = 0
WALK_ANIM_DELAY = 150  # ms

# --- GRADIENT ÇİZGİ ---
def draw_gradient_line(surface, start, end, color_start, color_end, width=5):
    steps = int(math.hypot(end[0] - start[0], end[1] - start[1]))
    for i in range(steps):
        t = i / steps
        r = color_start[0] + t * (color_end[0] - color_start[0])
        g = color_start[1] + t * (color_end[1] - color_start[1])
        b = color_start[2] + t * (color_end[2] - color_start[2])
        x = start[0] + t * (end[0] - start[0])
        y = start[1] + t * (end[1] - start[1])
        pygame.draw.circle(surface, (int(r), int(g), int(b)), (int(x), int(y)), width // 2)

# --- YENİ FONKSİYONLAR ---
def draw_path():
    for i in range(len(path) - 1):
        draw_gradient_line(screen, path[i], path[i + 1], (255, 165, 0), (0, 255, 0), width=5)

def draw_labels():
    for i, pos in enumerate(path):
        pygame.draw.circle(screen, WHITE, pos, 8)
        label = pixel_font.render(f"Week {haftalar[i]}", True, WHITE)
        screen.blit(label, (pos[0] - 40, pos[1] + 25))

def update_character(dt):
    global step_index, char_pos
    if step_index < len(path) - 1:
        target_x, target_y = path[step_index + 1]
        dx, dy = target_x - char_pos[0], target_y - char_pos[1]
        distance = math.hypot(dx, dy)

        if distance < speed:
            char_pos = [target_x, target_y]
            step_index += 1
        else:
            angle = math.atan2(dy, dx)
            char_pos[0] += math.cos(angle) * speed
            char_pos[1] += math.sin(angle) * speed

def draw_character(dt):
    global walk_frame, walk_timer
    walk_timer += dt
    if walk_timer >= WALK_ANIM_DELAY:
        walk_timer = 0
        walk_frame = (walk_frame + 1) % len(character_walk)

    screen.blit(character_walk[walk_frame], (char_pos[0] - 40, char_pos[1] - 80))

def draw_success_balloon():
    current_index = min(step_index, len(haftalar) - 1)
    success = basari_oranlari[current_index]
    text_surface = pixel_font.render(f"%{success}", True, BLACK)
    pygame.draw.rect(screen, WHITE, (char_pos[0] - 25, char_pos[1] - 110, 50, 30), border_radius=6)
    screen.blit(text_surface, (char_pos[0] - 20, char_pos[1] - 105))

def draw_badge():
    if step_index == max_index:
        t = pygame.time.get_ticks() / 200
        size = 40 + 5 * math.sin(t)
        glowing_badge = pygame.transform.scale(badge, (int(size), int(size)))
        screen.blit(glowing_badge, (char_pos[0] - size / 2, char_pos[1] - 130))

# --- OYUN DÖNGÜSÜ ---
running = True
while running:
    dt = clock.tick(FPS)
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_path()
    draw_labels()
    update_character(dt)
    draw_character(dt)
    draw_success_balloon()
    draw_badge()

    pygame.display.update()

pygame.quit()
sys.exit()
