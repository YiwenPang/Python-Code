import os
import pygame  # 导入pygame库

CURRENT_PATH = os.path.dirname(__file__)#获得当前文件目录
RESOURCE_PATH = os.path.join(CURRENT_PATH, '..')#走到CURRENT_PATH获取的目录的上级目录
IMAGES_PATH = os.path.join(RESOURCE_PATH, 'images')#获得RESOURCE_PATH目录下的images
SOUNDS_PATH = os.path.join(RESOURCE_PATH, 'sounds')#获得RESOURCE_PATH目录下的sounds

NUMBER_IMAGES = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png"]#用图片替代分数数字

def get_image(image_name):#寻找图片
    return pygame.image.load(os.path.join(IMAGES_PATH, image_name)).convert_alpha()

def get_images(image_name_arr):#寻找多组图片
    return list(map(get_image, image_name_arr))

def get_sound(sound_name):#寻找音频
    return pygame.mixer.Sound(os.path.join(SOUNDS_PATH, sound_name))

def get_sounds(sound_name_arr):#寻找多组音频
    return list(map(get_sound, sound_name_arr))
