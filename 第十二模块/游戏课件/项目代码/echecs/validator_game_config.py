# coding=utf-8

"""
验证游戏配置文件是否有配置错误
"""

from game.mahjong.models.config.parse_config import parse_config_ins
from game.mahjong.constants.gamedefine import Act, CheckAgainType, CheckSelfActType, SystemActType, GangType, HuSettleParamType, SettleHuFan
from game.mahjong.constants.carddefine import CardType, HuType


class ValidatorConfig(object):

    def __init__(self):
        self.handler = {
            "max_player_num": self.validate_max_player_num,  # 一局游戏的玩家数
            "has_tong_pao": self.validate_has_tong_pao,  # 是否可以通炮胡
            "auto_act_list": self.validate_auto_act_list,  # 自動操作列表, 按優先級降序排列

            "check_against_check_list": self.validate_check_against_check_list,  # 出牌后检查其他玩家可进行的操作列表
            "draw_card_check_list": self.validate_draw_card_check_list,  # 摸牌后检查该玩家可进行的操作
            "draw_card_bu_hua": self.validate_draw_card_bu_hua,          # 摸牌时是否需要补花

            "player_act_step": self.validate_player_act_step,
            "draw_card_step": self.validate_draw_card_step,
            "start_game_sequence": self.validate_start_game_sequence,  # 游戏开始时序列动作执行顺序
            "player_act_hook": self.validate_player_act_hook,          # 玩家行为钩子

            "used_card_types": self.validate_used_card_types,  # 使用的麻将牌花色
            "used_hu_types": self.validate_used_hu_types,  # 使用的麻将胡牌类型
            "hu_fan_info": self.validate_hu_fan_info,  # 各牌型番数信息
            "mutex_list": self.validate_mutex_list,  # 互斥牌型

            "settle_gang_info": self.validate_settle_gang_info,
            "settle_fan_config": self.validate_settle_fan_config,
            "gen_zhuang_fan": self.validate_gen_zhuang_fan  # 跟庄的番数，默认和屁胡基础番数一样
        }

    def validator(self, config_path):
        config_json = parse_config_ins.parse(config_path)
        for k, v in config_json.items():
            if k not in self.handler.keys():
                print "parse key error:", k
            if not self.handler.get(k)(v):
                print "validator error:", k, v
                return
        print "validate %s success~" % config_path

    def validate_max_player_num(self, param):   # 一局游戏的玩家数
        return 0 < int(param) and 5 > int(param)

    def validate_has_tong_pao(self, param):    # 是否可以通炮胡
        return param in [0, 1]

    def validate_auto_act_list(self, param):   # 自動操作列表, 按優先級降序排列
        for act in param:
            if act not in Act.to_dict().values():
                return False
        return True

    def validate_check_against_check_list(self, param): # 出牌后检查其他玩家可进行的操作列表
        for check in param:
            if check not in CheckAgainType.to_dict().values():
                return False
        return True

    def validate_draw_card_check_list(self, param):  # 摸牌后检查该玩家可进行的操作
        for check in param:
            if check not in CheckSelfActType.to_dict().values():
                return False
        return True

    def validate_player_act_step(self, param):
        """
        todo:验证详情待完善, 暂时只做初步验证　
        """
        for act in param.keys():
            if act not in Act.to_dict().values():
                return False
        return True

    def validate_draw_card_step(self, param):
        """
        todo:验证详情待完善, 暂时只做初步验证　
        """
        return True if param else False

    def validate_draw_card_bu_hua(self, param):
        return param in [0, 1]

    def validate_start_game_sequence(self, param):    # 游戏开始时序列动作执行顺序
        for k, v in param.items():
            if k not in SystemActType.to_dict().values():
                return False
            if v.get("next", -1) not in SystemActType.to_dict().values() and 0 != v.get("next", -1):
                return False
            if 0 > v.get("interval", -1):
                return False
        return True

    def validate_player_act_hook(self, param):
        for k, v in param.items():
            if k not in Act.to_dict().values():
                return False
            for t in v:
                if t not in Act.to_dict().values():
                    return False
        return True

    def validate_used_card_types(self, param):      # 使用的麻将牌花色
        for t in param:
            if t not in CardType.all_type():
                return False
        return True

    def validate_used_hu_types(self, param):        # 使用的麻将胡牌类型
        types = HuType.to_dict().values()
        for k, v in param.items():
            if k not in types:
                return False
            for t in v:
                if t not in types:
                    return False
        return True

    def validate_hu_fan_info(self, param):  # 各牌型番数信息
        for k, v in param.items():
            if k not in HuType.to_dict().values():
                return False
            if 0 > v:
               return False
        return True

    def validate_mutex_list(self, param):   # 互斥牌型
        if not isinstance(param, list):
            return False
        for m in param:
            for t in m:
                if t not in HuType.to_dict().values():
                    return False
        return True

    def validate_settle_gang_info(self, param):
        for gang, fan in param.items():
            if gang not in GangType.to_dict().values() or 0 > fan:
                return False
        return True

    def validate_settle_fan_config(self, param):
        for k, v in param.items():
            if k not in HuSettleParamType.to_dict().values():
                return False
            for t, fan in v.items():
                if t not in SettleHuFan.to_dict().values() or 0 > fan:
                    return False
        return True

    def validate_gen_zhuang_fan(self, param):  # 跟庄的番数，默认和屁胡基础番数一样
        return 0 < param


if __name__ == "__main__":
    ValidatorConfig().validator("game_setting/default.json")
    ValidatorConfig().validator("game_setting/special/common.json")