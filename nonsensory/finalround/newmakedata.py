import json
import os
import copy
import re

fold = 'TheWheelTypingList'
mus_ext = '.ogg'
txt_ext = '.jet'
prompts = os.listdir(fold)

with open(fold + txt_ext,encoding='utf-8') as f:
    content = json.load(f)["content"]

with open(fold + 'Tech' + txt_ext,encoding='utf-8') as f:
    content_tech = json.load(f)["content"]
##fields
fields_sample = {
    "HasIntroAudio":{
        "t":"B",
        "v":"false",
        "n":"HasIntroAudio"
        },
    "IntroAudio":{
        "t":"A",
        "v":"intro",
        "n":"IntroAudio"
        },
    "HasPromptAudio":{
        "t":"B",
        "v":"false",
        "n":"HasPromptAudio"
        },
    "PromptAudio":{
        "t":"A",
        "v":"prompt",
        "n":"PromptAudio"
        },
    "HasOutroAudio":{
        "t":"B",
        "v":"false",
        "n":"HasOutroAudio"
        },
    "OutroAudio":{
        "t":"A",
        "v":"outro",
        "n":"OutroAudio"
        },
    "HasFollowupAudio":{
        "t":"B",
        "v":"false",
        "n":"HasFollowupAudio"
        },
    "FollowupAudio":{
        "t":"A",
        "v":"followup",
        "n":"FollowupAudio"
        }
    }
clue_sample = {
    "HasClueAudio":{
        "t":"B",
        "v":"false",
        "n":"HasClueAudio"
        },
    "ClueAudio":{
        "t":"A",
        "v":"answers_X_hint",
        "n":"ClueAudio"
        }
    }
types = ["intro","prompt","outro","followup"]

## NEXT PART SHOULD NOT BE MODIFIED (jk lol)

for prompt in prompts:
    files = os.listdir(fold + '/' + prompt)
    c = {}
    for cont in content:
        if cont["id"] == prompt:
            c = cont
            break
    c_tech = {}
    for cont_tech in content_tech:
        if cont_tech["id"] == prompt:
            c_tech = cont_tech
            break
    answers = []
    for answer in c["answers"]:
        answers += [""]
    fields = copy.deepcopy(fields_sample)
    for file in files:
        file = file.replace(mus_ext,'')
        if file not in types:
            if file == 'data.jet':
                os.remove(fold + '/' + prompt + '/' + file)
            elif (re.match(r'answers_\d_hint',file) != None or re.match(r'answers_\d\d_hint',file) != None):
                ## в массив ответов перенесем хинт. его нужно будет отразить в дате
                answers[int(file.replace('answers_','').replace('_hint',''))] = c["answers"][int(file.replace('answers_','').replace('_hint',''))]["hint"]
            else:
                print(file)
                print(prompt)
                raise Exception
        else:
            fields["Has" + file.capitalize() + "Audio"]["v"] = "true"
            try:
                fields[file.capitalize() + "Audio"]["s"] = c[file]
            except KeyError:
                try:
                    fields[file.capitalize() + "Audio"]["s"] = c_tech[file]
                except KeyError:
                    raise Exception ##holy shit if that raises i don't know what to do anymore
    i = 0
    print(prompt,answers)
    for answer in answers:
        clue = copy.deepcopy(clue_sample)
        clue["HasClueAudio"]["n"] += str(i)
        clue["ClueAudio"]["n"] += str(i)
        clue["ClueAudio"]["v"] = "answers_" + str(i) + "_hint"
        if not (answer == ""):
            clue["HasClueAudio"]["v"] = "true"
            clue["ClueAudio"]["s"] = answer
        clue["HasClueAudio" + str(i)] = clue["HasClueAudio"]
        clue["ClueAudio" + str(i)] = clue["ClueAudio"]
        clue.pop("HasClueAudio")
        clue.pop("ClueAudio")
        fields.update(clue)
        i += 1
    fields = list(fields.values())
    n = open(fold + '/' + prompt + '/data' + txt_ext,'w',encoding='utf-8')
    n.write(json.dumps({"fields":fields},ensure_ascii=False,indent=2))
    n.close()
