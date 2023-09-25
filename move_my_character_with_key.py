from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

def handle_events():
    global running, dir_x, dir_y

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT or event.key == SDLK_LEFT:
                dir_x = 0
            elif event.key == SDLK_DOWN or event.key == SDLK_UP:
                dir_y = 0

running = True
frame = 0
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2

dir_x = 0
dir_y = 0

while running:

    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 128, 128 * 15, 128, 128, x, y, 150, 150)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8

    if 64 < x + dir_x * 10 < TUK_WIDTH - 64 and 0 < y + dir_y * 10 < TUK_HEIGHT - 64:
        x += dir_x * 10
        y += dir_y * 10

    delay(0.03)

close_canvas()
