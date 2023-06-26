import pygame
import time

# Инициализация Pygame
pygame.init()

# Определение размеров окна
window_width = 400
window_height = 300

# Создание окна
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Выращивание куста марихуаны")

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Определение параметров куста марихуаны
bush_health = 100
bush_thirst = 0
bush_fertilizer = 0
bush_temperature = 25

# Определение размеров и позиции прямоугольников для отображения состояния куста
health_rect = pygame.Rect(50, 50, 200, 20)
thirst_rect = pygame.Rect(50, 100, 200, 20)
fertilizer_rect = pygame.Rect(50, 150, 200, 20)
temperature_rect = pygame.Rect(50, 200, 200, 20)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка взаимодействия с кустом марихуаны
    if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши нажата
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Проверка, была ли нажата кнопка внутри прямоугольника состояния жизни
        if health_rect.collidepoint(mouse_x, mouse_y):
            bush_health += 20
            if bush_health > 100:
                bush_health = 100

        # Проверка, была ли нажата кнопка внутри прямоугольника состояния жажды
        if thirst_rect.collidepoint(mouse_x, mouse_y):
            bush_thirst += 10
            if bush_thirst > 100:
                bush_thirst = 100

        # Проверка, была ли нажата кнопка внутри прямоугольника состояния удобрений
        if fertilizer_rect.collidepoint(mouse_x, mouse_y):
            bush_fertilizer += 10
            if bush_fertilizer > 100:
                bush_fertilizer = 100

        # Проверка, была ли нажата кнопка внутри прямоугольника состояния температуры
        if temperature_rect.collidepoint(mouse_x, mouse_y):
            bush_temperature += 5
            if bush_temperature > 40:
                bush_temperature = 40

    # Отображение состояния куста марихуаны
    window.fill(BLACK)

    # Отображение прямоугольников состояния куста
    pygame.draw.rect(window, WHITE, health_rect)
    pygame.draw.rect(window, WHITE, thirst_rect)
    pygame.draw.rect(window, WHITE, fertilizer_rect)
    pygame.draw.rect(window, WHITE, temperature_rect)

    # Отображение текущих значений состояния куста
    pygame.draw.rect(window, GREEN, (health_rect.x, health_rect.y, bush_health * 2, health_rect.height))
    pygame.draw.rect(window, RED, (thirst_rect.x, thirst_rect.y, bush_thirst * 2, thirst_rect.height))
    pygame.draw.rect(window, RED, (fertilizer_rect.x, fertilizer_rect.y, bush_fertilizer * 2, fertilizer_rect.height))
    pygame.draw.rect(window, WHITE, (temperature_rect.x, temperature_rect.y, (bush_temperature - 20) * 10, temperature_rect.height))

    # Отображение текста в полосках состояния
    font = pygame.font.Font(None, 20)
    health_text = font.render(str(bush_health), True, BLACK)
    thirst_text = font.render(str(bush_thirst), True, BLACK)
    fertilizer_text = font.render(str(bush_fertilizer), True, BLACK)
    temperature_text = font.render(str(bush_temperature), True, BLACK)

    window.blit(health_text, (health_rect.x + health_rect.width + 10, health_rect.y))
    window.blit(thirst_text, (thirst_rect.x + thirst_rect.width + 10, thirst_rect.y))
    window.blit(fertilizer_text, (fertilizer_rect.x + fertilizer_rect.width + 10, fertilizer_rect.y))
    window.blit(temperature_text, (temperature_rect.x + temperature_rect.width + 10, temperature_rect.y))

    # Обновление окна
    pygame.display.flip()

    # Задержка, чтобы не перегружать процессор
    time.sleep(0.1)
