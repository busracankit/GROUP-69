import pygame
import sys
import math
import csv
from datetime import datetime
from collections import defaultdict

from fontTools.ttLib.tables.O_S_2f_2 import OS2_UNICODE_RANGES


# --- CSV'DEN VERİYİ OKU ---
def load_user_data(csv_path, user_id):
    hata_sayilari = defaultdict(int)
    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if str(row['user_id']) == str(user_id):
                tarih_str = row['datetime'][:10]
                try:
                    tarih = datetime.strptime(tarih_str, "%Y-%m-%d")
                    hata_sayilari[tarih] += 1
                except Exception as e:
                    print(f"Tarih hatası: {tarih_str} -> {e}")

    sorted_tarihler = sorted(hata_sayilari.keys())
    haftalar = []
    basari_oranlari = []
    for i in range(8):  # Sabit 8 hafta
        if i < len(sorted_tarihler):
            tarih = sorted_tarihler[i]
            hata = hata_sayilari[tarih]
            basari = round(((10 - hata) / 10) * 100)
        else:
            basari = 100  # Eksik hafta varsa başarı %100
        haftalar.append(i + 1)
        basari_oranlari.append(basari)
    return haftalar, basari_oranlari

# --- KULLANICI ID AYARI ---
USER_ID = 1
csv_path = "disleksi_egzersiz.csv"
haftalar, basari_oranlari = load_user_data(csv_path, USER_ID)

# --- RENKLER ve AYARLAR ---
WIDTH, HEIGHT = 1200, 700
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139, 69, 19)  # Kahverengi
ORANGE = (255, 165, 0)

# --- Pygame Başlat ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎮 LetStep Gelişim Yolculuğu")
clock = pygame.time.Clock()

# --- GÖRSELLER ---
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
character_walk = [
    pygame.transform.scale(pygame.image.load(f"walk{i}.png"), (80, 80)) for i in range(1, 5)]
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
step_index = -1
speed = 3
walk_frame = 0
walk_timer = 0
WALK_ANIM_DELAY = 150

# --- GRADIENT ÇİZGİ ---
def draw_gradient_line(surface, start, end, color_start, color_end, width=5):
    steps = int(math.hypot(end[0]-start[0], end[1]-start[1]))
    for i in range(steps):
        t = i / steps
        r = color_start[0] + t * (color_end[0] - color_start[0])
        g = color_start[1] + t * (color_end[1] - color_start[1])
        b = color_start[2] + t * (color_end[2] - color_start[2])
        x = start[0] + t * (end[0] - start[0])
        y = start[1] + t * (end[1] - start[1])
        pygame.draw.circle(surface, (int(r), int(g), int(b)), (int(x), int(y)), width//2)

# --- OYUN DÖNGÜSÜ ---
running = True
while running:
    dt = clock.tick(FPS)
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- GRAFİK ÇİZGİSİ ---
    for i in range(len(path) - 1):
        draw_gradient_line(screen, path[i], path[i+1], (255, 165, 0), (0, 255, 0), width=5)

    # --- NOKTALAR ve ETİKETLER ---
    for i, pos in enumerate(path):
        pygame.draw.circle(screen, WHITE, pos, 8)
        label = pixel_font.render(f"Week {haftalar[i]}", True, WHITE)  # ✅ Kahverengi etiket
        screen.blit(label, (pos[0] - 40, pos[1] + 25))

    # --- KARAKTER HAREKETİ ---
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

    # --- YÜRÜYEN KARAKTER ANİMASYONU ---
    walk_timer += dt
    if walk_timer >= WALK_ANIM_DELAY:
        walk_timer = 0
        walk_frame = (walk_frame + 1) % len(character_walk)
    screen.blit(character_walk[walk_frame], (char_pos[0] - 40, char_pos[1] - 80))

    # --- BAŞARI YÜZDESİ BALONU ---
    current_index = max(0, min(step_index, len(haftalar) - 1))
    success = basari_oranlari[current_index]
    text_surface = pixel_font.render(f"%{success}", True, BLACK)
    pygame.draw.rect(screen, WHITE, (char_pos[0] - 25, char_pos[1] - 110, 50, 30), border_radius=6)
    screen.blit(text_surface, (char_pos[0] - 20, char_pos[1] - 105))

    # --- ROZET PARLAMA (ZİRVE NOKTADA) ---
    if current_index == max_index:
        t = pygame.time.get_ticks() / 200
        size = 40 + 5 * math.sin(t)
        glowing_badge = pygame.transform.scale(badge, (int(size), int(size)))
        screen.blit(glowing_badge, (char_pos[0] - size / 2, char_pos[1] - 130))

    pygame.display.update()

pygame.quit()
sys.exit()
