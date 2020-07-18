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
            scenario_catalog = "Lane change"
            if self.object_init[1] != self.object_target[1]:
                if self.object_init[1] != self.ego_init[1]:
                    scenario_name = "Ego car is lane changing with side object car changes lane"
                else:
                    if self.object_init[0] > self.ego_init[0]:
                        scenario_name = "Ego car is lane changing with behind object car changes lane"
                    else:
                        scenario_name = "Ego car is lane changing with leading object car changes lane"
            else:
                if self.object_init[1] == self.ego_init[1]:
                    scenario_name = "Ego car is lane changing with leading object car free driving in lane%d" % \
                                    self.object_init[1]
                else:
                    scenario_name = "Ego car is lane changing with side object car free driving in lane%d" % \
                                    self.object_init[1]
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
            scenario_description = a + b + c + d + e + f
            ego_status, target_status = self.level_four(self.ego_init[1])
            g = "4.1.3 Object action:Lane change to lane%d\n" % self.ego_target[1]
            h = "\n"
            if self.object_init[0] > self.ego_init[0]:
                i = "4.2.2 Object position:Lane=%d,in front of the ego car\n" % self.object_init[1]
            elif self.object_init[0] < self.ego_init[0]:
                i = "4.2.2 Object position:Lane=%d,behind the ego car\n" % self.object_init[1]
            else:
                i = "4.2.2 Object position:Lane=%d,parallel to the ego car\n" % self.object_init[1]
            if self.object_init[1] == self.object_target[1]:
                j = "4.2.3 Object action:Lane keeping"
            else:
                j = "4.2.3 Object action:Lane change to lane%d" % self.object_target[1]
            objects = ego_status + g + h + target_status + i + j
            scenario_type, road_level, infrastructure, environment = self.fixed_content()
            description = [scenario_catalog, scenario_type, scenario_name, scenario_description, road_level,
                           infrastructure, objects, environment, "LC"]
            return description
        else:
            if (self.object_init[1] == self.ego_init[1] and
                    self.object_init[0] > self.ego_init[0] and
                    self.object_target[1] != self.object_init[1]):
                scenario_catalog = "Cut out"
                scenario_name = "Ego car is free driving with leading object car cuts out"
                a = "1 Start situation\n"
                b = "Ego car drives on a straight motorway on sunny afternoon in lane%d\n" % self.ego_init[1]
                c = "Object car drives in front of ego car in lane%d\n\n" % self.object_init[1]
                d = "2 Evolution\n"
                e = "Object car changes to lane%d" % self.object_target[1]
                scenario_description = a + b + c + d + e
                ego_status, target_status = self.level_four(self.ego_init[1])
                g = "\n"
                h = "4.2.2 Object position:Lane=%d,in front of the ego car\n" % self.object_init[1]
                i = "4.2.3 Object action:Lane change to lane%d" % self.object_target[1]
                objects = ego_status + g + target_status + h + i
                scenario_type, road_level, infrastructure, environment = self.fixed_content()
                description = [scenario_catalog, scenario_type, scenario_name, scenario_description, road_level,
                               infrastructure, objects, environment, "CO"]
                return description
            elif (self.object_init[1] == self.ego_init[1] and
                  self.object_init[0] > self.ego_init[0] and
                  self.object_target[1] == self.object_init[1]):
                scenario_catalog = "Car following"
                scenario_name = "Ego car is free driving with leading object car free driving in lane%d" % \
                                self.object_target[1]
                a = "1 Start situation\n"
                b = "Ego car drives on a straight motorway on sunny afternoon in lane%d\n" % self.ego_init[1]
                c = "Object car drives in front of ego car in lane%d\n\n" % self.object_init[1]
                d = "2 Evolution\n"
                e = "Ego car follows object car\n"
                f = "Object car drives in lane%d" % self.object_target[1]
                scenario_description = a + b + c + d + e + f
                ego_status, target_status = self.level_four(self.ego_init[1])
                g = "\n"
                h = "4.2.2 Object position:Lane=%d,in front of the ego car\n" % self.object_init[1]
                i = "4.2.3 Object action:Lane keeping"
                objects = ego_status + g + target_status + h + i
                scenario_type, road_level, infrastructure, environment = self.fixed_content()
                description = [scenario_catalog, scenario_type, scenario_name, scenario_description, road_level,
                               infrastructure, objects, environment, "CF"]
                return description
            elif (self.object_init[1] != self.ego_init[1] and
                  self.object_init[0] >= self.ego_init[0] and
                  (self.object_target[1] == self.ego_init[1] or
                   ((self.object_init[1] - self.ego_target[1]) *
                    (self.object_target[1] - self.ego_target[1]) < 0))):
                scenario_catalog = "Cut in"
                scenario_name = "Ego car is free driving with side object car cuts in"
                a = "1 Start situation\n"
                b = "Ego car drives on a straight motorway on sunny afternoon in lane%d\n" % self.ego_init[1]
                c = "Object car drives in lane%d\n\n" % self.object_init[1]
                d = "2 Evolution\n"
                e = "Ego car is driving free in its lane\n"
                f = "Object car cuts in"
                scenario_description = a + b + c + d + e + f
                ego_status, target_status = self.level_four(self.ego_init[1])
                g = "\n"
                h = "4.2.2 Object position:Lane=%d\n" % self.object_init[1]
                i = "4.2.3 Object action:Lane change to lane%d" % self.object_target[1]
                objects = ego_status + g + target_status + h + i
                scenario_type, road_level, infrastructure, environment = self.fixed_content()
                description = [scenario_catalog, scenario_type, scenario_name, scenario_description, road_level,
                               infrastructure, objects, environment, "CI"]
                return description
            else:
                print(u"无效的场景定义")

    @staticmethod
    def level_four(ego_line):
        a = "4.1 Ego_car\n"
        b = "4.1.1 Object class:Tiguan L\n"
        c = "4.1.2 Object position:lane=%d\n" % ego_line
        d = "4.2 Object_car\n"
        e = "4.2.1 Object class:sedan\n"
        ego_status = a + b + c
        target_status = d + e
        return ego_status, target_status

    @staticmethod
    def fixed_content():
        scenario_type = "Base Scenario"
        road_level = "1.1 General\nArea:China\n\n1.2 Layout\nRoad type:motorway\n\n1.3 Geometry\nFlat\nElongated road"
        infrastructure = "2.1 Infrastructure\nMedian barrier: hard\nRoadside barrier: hard\n\n2.2 Lane " \
                         "marking\nClearness: clear "
        environment = "5.1 Environment\nSeason: summer\nTime of day: afternoon\nWeather: sunny\nLighting: sun " \
                      "shiny\n\n5.2 Road condition\nRoad influence: dry\nRoadway friction value: normal "
        return scenario_type, road_level, infrastructure, environment


if __name__ == "__main__":
    sce = ScenarioClass(2, [1, 2], [2, 3])
    dev = sce.catalog()
    print(dev)
