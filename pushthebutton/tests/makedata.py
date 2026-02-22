import json
import os
from copy import deepcopy

marker = False
fields = None
data = None
fold = "PushTheButtonWritingTests"
er = 57777

with open("base.txt", "r", encoding="utf-8") as qemu:
    lines = qemu.readlines()


def replace_prompts(source, prompt_key, prompt_value):
    if prompt_value is None:
        print(f"Value for {prompt_key} is not available.")
    else:
        for feeld in source["fields"]:
            if feeld.get("n") == prompt_key:
                print(f"Value for {prompt_key} has been replaced.")
                if prompt_key != "HumanPromptAudio":
                    feeld["v"] = prompt_value
                else:
                    feeld["s"] = prompt_value


for line in lines:
    line = line.replace("\n", "")
    s = line.split(chr(9))

    if (s[0].isdigit() or s[1].startswith("PushTheButton")) and marker:
        m = open(fold + "/" + er + "/data.jet", "w", encoding="utf-8")
        m.write(json.dumps({"fields": fields}, ensure_ascii=False, indent=1))
        m.close()
        data = None
        marker = False
    
    if s[1].startswith("PushTheButton"):
        fold = s[1]
        os.makedirs(fold, exist_ok=True)
        continue

    if s[0].isdigit():
        er = s[0]

    # humanmode = True

    translations = {}

    sd = deepcopy(s)
    sd.pop(0)
    if len(sd) == 2:
        original_text, translated_text = sd
        translations[original_text] = translated_text

    os.makedirs(fold + "/" + er, exist_ok=True)
    if data is None:
        with open(fold + "/" + er + "/data.jet", "r", encoding="utf-8") as f:
            data = json.load(f)
            fields = data["fields"]
    for field in fields:
        match field["n"]:
            case u if u.startswith("AlienPromptText"):
                replace_prompts(data, field["n"], translations.get(field["v"]))
            case "HumanPromptText" if not marker:
                replace_prompts(data, "HumanPromptText", translations.get(field["v"]))
                marker = True
            case "HumanPromptAudio":
                replace_prompts(data, "HumanPromptAudio", translations.get(field["s"]))
                break

m = open(fold + "/" + er + "/data.jet", "w", encoding="utf-8")
m.write(json.dumps({"fields": fields}, ensure_ascii=False, indent=1))
m.close()