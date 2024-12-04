from .attacker import Attacker
from .ep_attacker import EPAttacker
from .sos_attacker import SOSAttacker
from .neuba_attacker import NeuBAAttacker
from .por_attacker import PORAttacker
from .lwp_attacker import LWPAttacker
from .lws_attacker import LWSAttacker
from .ripples_attacker import RIPPLESAttacker
from .OrderBkd import OrderBkd


ATTACKERS = {
    "base": Attacker,
    "ep": EPAttacker,
    "sos": SOSAttacker,
    "neuba": NeuBAAttacker,
    "por": PORAttacker,
    "lwp": LWPAttacker,
    'lws': LWSAttacker,
    'ripples': RIPPLESAttacker,
    "orderbkd": OrderBkd  # 添加 OrderBkd 攻击者
}


def load_attacker(config):
    # 获取攻击者名称并确保小写
    attacker_name = config["name"].lower()

    # 确保在 ATTACKERS 字典中存在该攻击者名称
    if attacker_name not in ATTACKERS:
        raise ValueError(f"Unknown attacker: {attacker_name}")

    # 删除构造函数不需要的参数，如 'name'
    if 'name' in config:
        del config['name']

    # 返回初始化后的攻击者对象，传递剩余的配置
    return ATTACKERS[attacker_name](**config)




