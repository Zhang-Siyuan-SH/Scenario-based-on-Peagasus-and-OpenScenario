# coding=utf-8
from PIL import Image
import cv2 as cv
import math

# 要用绝对路径，否则pywin32无法通过路径读取图片
IMG_SOURCE = "C:\\Users\\user\\Desktop\\Scenario-based-on-Peagasus-and-OpenScenario\\material_lib\\"
IMG_OUTPUT = "C:\\Users\\user\\Desktop\\Scenario-based-on-Peagasus-and-OpenScenario\\scenario_output\\img\\"


def line_generate(init_position, target_position, ego_w, object_w, object_h, object_target_h, save_path):
    img = cv.imread(save_path)
    if init_position[1] == target_position[1]:
        img = cv.arrowedLine(img, ((32 + ego_w // 4) * (init_position[0] - 1)+object_w//4, 34 * (init_position[1] - 1)+8
                                   + object_h//8),
                             ((32 + ego_w // 4) * (target_position[0] - 1), 34 * (target_position[1] - 1)+8
                              + object_target_h//8),
                             (0, 0, 0), 1, 8, 0, 0.15)
    else:
        pixel_x = range((32 + ego_w // 4) * (init_position[0] - 1) + object_w // 4, (32 + ego_w // 4) * (target_position[0] - 1))
        amplitude = abs((34 * (init_position[1] - 1)+8+object_h//8)-(34 * (target_position[1] - 1)+8
                                                                                + object_target_h//8))//2
        offset = ((34 * (init_position[1] - 1) + 8 + object_h // 8) + (
                    34 * (target_position[1] - 1) + 8 + object_target_h // 8)) // 2
        if init_position[1] < target_position[1]:
            pixel_y = [offset - math.trunc(amplitude * math.cos(math.pi/(((32 + ego_w // 4) * (target_position[0] - 1))
                                                                         - ((32 + ego_w // 4) * (init_position[0] - 1)
                                                                            + object_w // 4))*(x-((32 + ego_w // 4) * (init_position[0] - 1) + object_w // 4)))) for x in pixel_x]
        else:
            pixel_y = [offset + math.trunc(amplitude * math.cos(math.pi / (((32 + ego_w // 4) * (target_position[0] - 1))
                                                                           - ((32 + ego_w // 4) * (init_position[0] - 1)
                                                                              + object_w // 4)) * (x - ((32 + ego_w // 4) * (init_position[0] - 1) + object_w // 4)))) for x in pixel_x]
        for index_pixel in range(0, len(pixel_x)):
            if index_pixel+1 < (len(pixel_x)-1):
                img = cv.line(img, (pixel_x[index_pixel], pixel_y[index_pixel]), (pixel_x[index_pixel+1], pixel_y[index_pixel+1]),
                              (0, 0, 0), 1, 8)
            elif index_pixel+1 == (len(pixel_x)-1):
                img = cv.arrowedLine(img, (pixel_x[index_pixel], pixel_y[index_pixel]), (pixel_x[index_pixel+1], pixel_y[index_pixel+1]),
                                     (0, 0, 0), 1, 8, 0, 4)
            else:
                break
    cv.imwrite(save_path, img)


def base_generate(scenario_catalog, vehicle_position=[], lane="4lane.png"):
    if len(vehicle_position) == 0:
        path = IMG_SOURCE + lane
        img_init = cv.imread(path)
        img_init = cv.arrowedLine(img_init, (5, 5), (5, 20), (0, 0, 0), 1, 8, 0, 0.15)
        img_init = cv.arrowedLine(img_init, (5, 5), (20, 5), (0, 0, 0), 1, 8, 0, 0.15)
        save_path = IMG_OUTPUT + "initial.png"
        cv.imwrite(save_path, img_init)
        return save_path
    else:
        im = Image.open(IMG_SOURCE + lane)
        # 读取自车的初始位置和目标位置并显示在背景图片上
        im_ego = Image.open(IMG_SOURCE + "ego_car.png")
        im_ego_target = Image.open(IMG_SOURCE + "ego_car_target.png")
        ego_w, ego_h = im_ego.size
        ego_target_w, ego_target_h = im_ego.size
        im_ego = im_ego.resize((ego_w // 4, ego_h // 4))  # resize picture
        im_ego_target = im_ego_target.resize((ego_target_w // 4, ego_target_h // 4))  # resize picture
        im.paste(im_ego, (32 + ego_w // 4, 34 * (vehicle_position[0][1] - 1) + 8))
        # 上一句中32为车辆位置之间的横向间隔，34为车道宽度，8的作用是将车辆的图标放至车道中间
        im.paste(im_ego_target, ((32 + ego_w // 4) * 2, 34 * (vehicle_position[1][1] - 1) + 8))
        if scenario_catalog == "Car following":
            im_object = Image.open(IMG_SOURCE + "leading_car.png")
            im_object_target = Image.open(IMG_SOURCE + "object_car_target.png")
            object_w, object_h = im_object.size
            object_target_w, object_target_h = im_object_target.size
            im_object = im_object.resize((object_w // 4, object_h // 4))  # resize picture
            im_object_target = im_object_target.resize((object_target_w // 4, object_target_h // 4))  # resize picture
            im.paste(im_object,
                     ((32 + ego_w // 4) * (vehicle_position[2][0] - 1), 34 * (vehicle_position[2][1] - 1) + 8))
            im.paste(im_object_target,
                     ((32 + ego_w // 4) * (vehicle_position[3][0] - 1), 34 * (vehicle_position[3][1] - 1) + 8))
            # 上述两句中仍然用了ego_w，以保证所有车辆在图上的摆放位置统一
            save_path = IMG_OUTPUT + "CF_ego_{}{}_{}{}_target_{}{}_{}{}.png".format(vehicle_position[0][0],
                                                                                    vehicle_position[0][1],
                                                                                    vehicle_position[1][0],
                                                                                    vehicle_position[1][1],
                                                                                    vehicle_position[2][0],
                                                                                    vehicle_position[2][1],
                                                                                    vehicle_position[3][0],
                                                                                    vehicle_position[3][1])
            im.save(save_path)
            line_generate(vehicle_position[0], vehicle_position[1], ego_w, ego_w, ego_h, ego_target_h, save_path)
            line_generate(vehicle_position[2], vehicle_position[3], ego_w, object_w, object_h, object_target_h,
                          save_path)
            return save_path
        elif scenario_catalog == "Cut out":
            im_object = Image.open(IMG_SOURCE + "leading_car.png")
            im_object_target = Image.open(IMG_SOURCE + "object_car_target.png")
            object_w, object_h = im_object.size
            object_target_w, object_target_h = im_object_target.size
            im_object = im_object.resize((object_w // 4, object_h // 4))  # resize picture
            im_object_target = im_object_target.resize((object_target_w // 4, object_target_h // 4))  # resize picture
            im.paste(im_object,
                     ((32 + ego_w // 4) * (vehicle_position[2][0] - 1), 34 * (vehicle_position[2][1] - 1) + 8))
            im.paste(im_object_target,
                     ((32 + ego_w // 4) * (vehicle_position[3][0] - 1), 34 * (vehicle_position[3][1] - 1) + 8))
            save_path = IMG_OUTPUT + "CO_ego_{}{}_{}{}_target_{}{}_{}{}.png".format(vehicle_position[0][0],
                                                                                    vehicle_position[0][1],
                                                                                    vehicle_position[1][0],
                                                                                    vehicle_position[1][1],
                                                                                    vehicle_position[2][0],
                                                                                    vehicle_position[2][1],
                                                                                    vehicle_position[3][0],
                                                                                    vehicle_position[3][1])
            im.save(save_path)
            line_generate(vehicle_position[0], vehicle_position[1], ego_w, ego_w, ego_h, ego_target_h, save_path)
            line_generate(vehicle_position[2], vehicle_position[3], ego_w, object_w, object_h, object_target_h,
                          save_path)
            return save_path
        elif scenario_catalog == "Cut in":
            im_object = Image.open(IMG_SOURCE + "cut_in_car.png")
            im_object_target = Image.open(IMG_SOURCE + "object_car_target.png")
            object_w, object_h = im_object.size
            object_target_w, object_target_h = im_object_target.size
            im_object = im_object.resize((object_w // 4, object_h // 4))  # resize picture
            im_object_target = im_object_target.resize((object_target_w // 4, object_target_h // 4))  # resize picture
            im.paste(im_object,
                     ((32 + ego_w // 4) * (vehicle_position[2][0] - 1), 34 * (vehicle_position[2][1] - 1) + 8))
            im.paste(im_object_target,
                     ((32 + ego_w // 4) * (vehicle_position[3][0] - 1), 34 * (vehicle_position[3][1] - 1) + 8))
            save_path = IMG_OUTPUT + "CI_ego_{}{}_{}{}_target_{}{}_{}{}.png".format(vehicle_position[0][0],
                                                                                    vehicle_position[0][1],
                                                                                    vehicle_position[1][0],
                                                                                    vehicle_position[1][1],
                                                                                    vehicle_position[2][0],
                                                                                    vehicle_position[2][1],
                                                                                    vehicle_position[3][0],
                                                                                    vehicle_position[3][1])
            im.save(save_path)
            line_generate(vehicle_position[0], vehicle_position[1], ego_w, ego_w, ego_h, ego_target_h, save_path)
            line_generate(vehicle_position[2], vehicle_position[3], ego_w, object_w, object_h, object_target_h,
                          save_path)
            return save_path
        elif scenario_catalog == "Lane change":
            if (vehicle_position[2][0] > vehicle_position[0][0]) and \
                    (vehicle_position[2][1] == vehicle_position[0][1]):
                im_object = Image.open(IMG_SOURCE + "leading_car.png")
            else:
                im_object = Image.open(IMG_SOURCE + "object_car.png")
            im_object_target = Image.open(IMG_SOURCE + "object_car_target.png")
            object_w, object_h = im_object.size
            object_target_w, object_target_h = im_object_target.size
            im_object = im_object.resize((object_w // 4, object_h // 4))  # resize picture
            im_object_target = im_object_target.resize((object_target_w // 4, object_target_h // 4))  # resize picture
            im.paste(im_object,
                     ((32 + ego_w // 4) * (vehicle_position[2][0] - 1), 34 * (vehicle_position[2][1] - 1) + 8))
            im.paste(im_object_target,
                     ((32 + ego_w // 4) * (vehicle_position[3][0] - 1), 34 * (vehicle_position[3][1] - 1) + 8))
            save_path = IMG_OUTPUT + "LC_ego_{}{}_{}{}_target_{}{}_{}{}.png".format(vehicle_position[0][0],
                                                                                    vehicle_position[0][1],
                                                                                    vehicle_position[1][0],
                                                                                    vehicle_position[1][1],
                                                                                    vehicle_position[2][0],
                                                                                    vehicle_position[2][1],
                                                                                    vehicle_position[3][0],
                                                                                    vehicle_position[3][1])
            im.save(save_path)
            line_generate(vehicle_position[0], vehicle_position[1], ego_w, ego_w, ego_h, ego_target_h, save_path)
            line_generate(vehicle_position[2], vehicle_position[3], ego_w, object_w, object_h, object_target_h,
                          save_path)
            return save_path
        else:
            pass
