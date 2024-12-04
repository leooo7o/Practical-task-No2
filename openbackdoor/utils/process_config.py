import os


def set_config(config: dict):
    """
    Set the config of the attacker.
    """
    # 获取 poisoner 配置项，如果没有则默认为空字典
    poisoner = config.get('poisoner', {})

    # 获取 label_dirty 和 label_consistency 配置项，如果没有则默认为 False
    label_dirty = poisoner.get('label_dirty', False)
    label_consistency = poisoner.get('label_consistency', False)

    # 根据 label_dirty 和 label_consistency 设置 poison_setting
    if label_consistency:
        config['attacker']['poisoner']['poison_setting'] = 'clean'
    elif label_dirty:
        config['attacker']['poisoner']['poison_setting'] = 'dirty'
    else:
        config['attacker']['poisoner']['poison_setting'] = 'mix'

    # 获取 poisoner 配置项中的参数
    poisoner_name = poisoner.get('name', 'orderbkd')  # 默认为 'orderbkd'
    poison_setting = config['attacker']['poisoner']['poison_setting']
    poison_rate = poisoner.get('poison_rate', 0.1)  # 默认为 0.1
    target_label = poisoner.get('target_label', 1)  # 默认为 1
    poison_dataset = config.get('poison_dataset', {}).get('name', 'hsol')  # 默认为 'hsol'

    # 计算并设置毒化数据的路径
    poison_data_basepath = os.path.join('poison_data',
                                        poison_dataset, str(target_label), poisoner_name)
    config['attacker']['poisoner']['poison_data_basepath'] = poison_data_basepath

    # 设置毒化数据路径
    config['attacker']['poisoner']['poisoned_data_path'] = os.path.join(poison_data_basepath, poison_setting,
                                                                        str(poison_rate))

    # 获取是否需要加载的配置项
    load = poisoner.get('load', False)

    # 设置 target_dataset 和 poison_dataset 的加载路径
    clean_data_basepath = config['attacker']['poisoner']['poison_data_basepath']
    config['target_dataset']['load'] = load
    config['target_dataset']['clean_data_basepath'] = os.path.join('poison_data',
                                                                   config["target_dataset"]["name"],
                                                                   str(target_label), poison_setting, poisoner_name)

    config['poison_dataset']['load'] = load
    config['poison_dataset']['clean_data_basepath'] = os.path.join('poison_data',
                                                                   config["poison_dataset"]["name"],
                                                                   str(target_label), poison_setting, poisoner_name)

    return config
