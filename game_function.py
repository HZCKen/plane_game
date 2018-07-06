import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


# 按下
def check_keydown_events(event, ai_setting, screen, ship, bullet_list):
    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        ship.is_move_left = True
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        ship.is_move_right = True
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        ship.is_move_up = True
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        ship.is_move_down = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullet_list)


# 放开
def check_keyup_events(event, ship):
    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
        ship.is_move_left = False
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        ship.is_move_right = False
    elif event.key == pygame.K_w or event.key == pygame.K_UP:
        ship.is_move_up = False
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        ship.is_move_down = False


# 监听事件
def check_events(ai_setting, screen, ship, bullet_list, stats, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_setting, screen, ship, bullet_list)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            


# 发射子弹
def fire_bullet(ai_setting, screen, ship, bullet_list):
    new_bullet = Bullet(ai_setting, screen, ship)
    if len(bullet_list) < ai_setting.bullets_allowed:
        bullet_list.add(new_bullet)
        new_bullet.draw_bullet()


# 更新子弹
def update_bullets(bullet_list, alien_list, ai_setting, ship, screen):
    bullet_list.update()
    for bullet in bullet_list.copy():
        if bullet.rect.bottom <= 0:
            bullet_list.remove(bullet)

    check_bullet_alien_collisions(bullet_list, alien_list,  ai_setting, screen, ship)


#   判断子弹击中外星人
def check_bullet_alien_collisions(bullet_list, alien_list, ai_setting, screen, ship):
    # 返回2组重叠的字典，2个True代表删除碰撞的。
    collisions = pygame.sprite.groupcollide(bullet_list, alien_list, True, True)

    if len(alien_list) == 0:
        bullet_list.empty()
        create_alien_list(ai_setting, screen, ship, alien_list)


# 更新屏幕
def update_screen(ai_setting, screen, ship, alien_list, bullet_list, stats, play_button):
    screen.fill(ai_setting.backgrounColor)
    ship.show()
    ship.update()
    for alien in alien_list:
        alien.show()
    for bullet in bullet_list:
        bullet.draw_bullet()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.update()

# 计算一行有多少个外星人
def get_number_aliens_x(ai_setting, alien_width):
    availabel_space_x = ai_setting.screen_width - (2 * alien_width)
    number_aliens_x = int(availabel_space_x / (2 * alien_width))
    return number_aliens_x

# 计算可以显示多少行外星人
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

# 创建外星人
def create_alien(ai_setting, screen , alien_list, alien_number, row_number):
    alien = Alien(screen, ai_setting)
    alien_list.add(alien)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number



# 创建一堆外星人
def create_alien_list(ai_setting, screen, ship, alien_list):
    alien = Alien(screen, ai_setting)
    number_aliens_x = get_number_aliens_x(ai_setting, alien.rect.width)
    number_rows = get_number_rows(ai_setting, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_setting, screen, alien_list, alien_number, row_number)


# 边界处理
def check_fleet_edges(ai_setting, alien_list):
    for alien in alien_list:
        # print(alien.check_edges())
        if alien.check_edges():
            change_fleet_direction(ai_setting, alien_list)
            break


#  改变方向并下移
def change_fleet_direction(ai_setting, alien_list):
    for alien in alien_list:
        alien.rect.y += ai_setting.flect_drop_speed

    ai_setting.fleet_direction *= -1

# 更新外星人位置
def update_aliens(ai_setting, alien_list, ship, stats, screen, bullet_list):
    check_fleet_edges(ai_setting, alien_list)
    alien_list.update()

    if pygame.sprite.spritecollideany(ship, alien_list):
        ship_hit(ai_setting, stats, screen, ship, alien_list, bullet_list)


def ship_hit(ai_setting, stats, screen, ship, alien_list, bullet_list):
    alien_list.empty()
    bullet_list.empty()

    create_alien_list(ai_setting, screen, ship, alien_list)
    ship.center_ship()

    if stats.ship_life > 0:
        stats.ship_life -= 1
        print(stats.ship_life)
        sleep(0.5)
    else:
        stats.game_active = False



