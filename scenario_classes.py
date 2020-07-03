# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")  # 加完以后raise的信息可以正常输出


class ScenarioClass(object):
    def __init__(self, e_target_lane, o_init_position, o_target_position):
        self.ego_init = [2, 2]
        self.ego_target = [3, e_target_lane]
        self.object_init = o_init_position
        self.object_target = o_target_position

    def catalog(self):
        # 限制车道和位置的范围在[1,4]，目标车辆的目标位置应大于其初始位置，目标车辆初始位置不应等于本车的初始位置
        positions = self.ego_target + self.object_init + self.object_target
        for position in positions:
            if (position not in range(1, 5) or
                    self.object_target[0] <= self.object_init[0] or
                    self.object_init == self.ego_init):
                ex = Exception(u"车道或位置选择不合理")
                raise ex
        if self.ego_target[1] != self.ego_init[1]:
            a = "1 Start situation\n"
            b = "Ego car drives on a straight motorway on sunny afternoon in lane%d\n" % self.ego_init[1]
            if self.object_init[1] != self.ego_init[1]:
                c = "Object car drives in lane%d\n\n" % self.object_init[1]
            else:
                if self.object_init[0] > self.ego_init[0]:
                    c = "Object car drives in front of ego car in lane%d\n\n" % self.object_init[1]
                else:
                    c = "Object car drives behind ego car in lane%d\n\n" % self.object_init[1]
            d = "2 Evolution\n"
            e = "Ego car changes to lane%d\n" % self.ego_target[1]
            if self.object_init[1] != self.object_target[1]:
                f = "Object car changes to lane%d" % self.object_target[1]
            else:
                f = "Object car drivers in lane%d" % self.object_target[1]
            print(a+b+c+d+e+f)
        else:
            if (self.object_init[1] == self.ego_init[1] and
                    self.object_init[0] > self.ego_init[0] and
                    self.object_target[1] != self.object_init[1]):
                a = "1 Start situation\n"
                b = "Ego car drives on a straight motorway on sunny afternoon in lane%d\n" % self.ego_init[1]
                c = "Object car drives in front of ego car in lane%d\n\n" % self.object_init[1]
                d = "2 Evolution\n"
                e = "Object car changes to lane%d" % self.object_target[1]
                print(a + b + c + d + e)
            elif (self.object_init[1] == self.ego_init[1] and
                    self.object_init[0] > self.ego_init[0] and
                    self.object_target[1] == self.object_init[1]):
                a = "1 Start situation\n"
                b = "Ego car drives on a straight motorway on sunny afternoon in lane%d\n" % self.ego_init[1]
                c = "Object car drives in front of ego car in lane%d\n\n" % self.object_init[1]
                d = "2 Evolution\n"
                e = "Ego car follows object car\n"
                f = "Object car drives in lane%d" % self.object_target[1]
                print(a + b + c + d + e + f)
            elif (self.object_init[1] != self.ego_init[1] and
                    self.object_init[0] >= self.ego_init[0] and
                  (self.object_target[1] == self.ego_init[1] or
                   ((self.object_init[1]-self.ego_target[1]) *
                    (self.object_target[1]-self.ego_target[1]) < 0))):
                a = "1 Start situation\n"
                b = "Ego car drives on a straight motorway on sunny afternoon in lane%d\n" % self.ego_init[1]
                c = "Object car drives in lane%d\n\n" % self.object_init[1]
                d = "2 Evolution\n"
                e = "Ego car is driving free in its lane\n"
                f = "Object car cuts in"
                print(a + b + c + d + e + f)
            else:
                print(u"无效的场景定义")