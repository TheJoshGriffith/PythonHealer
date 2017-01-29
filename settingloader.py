import json
from pprint import pprint
from healrule import HEALRULE_ITEM, HEALRULE_SPELL, HealRule

def LoadJsonHealRules(filename):
    with open(filename) as contents:
        content = json.load(contents)
        if content["healrules"] != None:
            healRules = []
            i = 0
            for hr in content["healrules"]:
                healRules.insert(0, HealRule(hr["minhp"], hr["maxhp"], hr["minmp"], hr["maxmp"], hr["hotkey"], eval(hr["type"]), hr["percent"]))
                i += 1
        pprint(healRules)
        return healRules