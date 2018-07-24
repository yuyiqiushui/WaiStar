import sys
import pygame
from settings import Settings
from ship import  Ship
import game_function as gf
def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 设置背景颜色
    bg_color = (119,119,119)
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        # 每次循环都会重绘屏幕
        gf.update_screen(ai_settings,screen,ship)
        ship.update()
        # 让最近绘制的屏幕可见
        pygame.display.flip()
run_game()