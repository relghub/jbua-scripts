import os
from json import load, dumps
from pathlib import Path
from copy import deepcopy


t_dot = [
     (
         "Fix",
         {
             "category": str,
             "choices": list,
             "correctAnswer": str,
             "id": str,
             "question": str,
         },
     ),
     ("GeoImages", {"altTexts": list, "id": str, "name": str}),
     (
         "GeoQuestions",
         {
             "category": "",
             "choices": list,
             "correctAnswer": str,
             "id": str,
             "imageId": str,
             "question": str,
         },
     ),
     (
         "Hop",
         {
             "category": str,
             "choices": list,
             "correctAnswer": str,
             "decade": str,
             "id": str,
             "question": str,
         },
     ),
     (
         "Impostor",
         {"category": str, "id": str, "impostor": str, "name": str, "real": str},
     ),
     ("ImpostorImages", {"altText": str, "id": str, "name": str, "vamping": str}),
     (
         "ImpostorStatements",
         {"category": str, "id": str, "imageId": str, "impostor": str, "real": str},
     ),
     (
         "Loop",
         {
             "category": str,
             "choices": list,
             "correctAnswer": str,
             "id": str,
             "question": str,
         },
     ),
     (
         "Year",
         {
             "category": str,
             "contextClue": "",
             "difficulty": str,
             "future": bool,
             "hint": [],
             "id": str,
             "question": str,
             "range": str,
             "tethering": bool,
             "year": int,
         },
     ),
 ]


def replace_prompts(source, prompt_key, prompt_value, mode):
    if prompt_value is None:
        print(f"Value for {prompt_key} is not available.")
    else:
        for feeld in source["fields"]:
            if feeld.get("n") == prompt_key:
                if mode == "Hop" or mode == "ImpostorImages":
                    feeld["s"] = prompt_value
                else:
                    feeld["v"] = prompt_value


def make_folders(file_i):
    data = None
    marker = False
    fields = None
    fold = t_dot[file_i][0]
    fnames = str(Path(os.getcwd()).parents[0])+"\\trans\\TimeTrivia"+fold
    fnlist = os.listdir(fnames)
    curfn = fnlist[0]
    with open("../" + fold.lower() + "/base.txt", "r", encoding="utf-8") as qemu:
        lines = qemu.readlines()
    for line in lines:
        line = line.replace("\n", "")
        s = line.split(chr(9))

        if (s[1].isdigit()) and marker:
            m = open(fnames + "\\" + curfn + "\\data.jet", "w", encoding="utf-8")
            m.write(dumps({"fields": fields}, ensure_ascii=False, indent=1))
            m.close()
            data = None
            marker = False

        if s[3] == "0":
            continue

        if s[0] == "id":
            curfn = s[1]

        # humanmode = True

        translations = {}

        sd = deepcopy(s)
        if file_i == 5:
            sd.pop(0)
            sd.pop(2)
        else:
            sd.pop(0)
            sd.pop(2)
            sd.pop(2)
            sd.pop(2)
        if len(sd) == 2:
            original_text, translated_text = sd
            translations[original_text] = translated_text

        if data is None:
            with open(fnames + "\\" + curfn + "\\data.jet", "r", encoding="utf-8") as f:
                data = load(f)
                fields = data["fields"]
        for field in fields:
            match field["n"]:
                case "QuestionAudio":
                    replace_prompts(data, field["n"], translations.get(field["s" if file_i == 3 else "v"]), fold)
                    marker = True
                    break
                case "Vamping":
                    replace_prompts(data, field["n"], translations.get(field["s"]), fold)
                    marker = True
                    break

    m = open(fnames + "\\" + curfn + "\\data.jet", "w", encoding="utf-8")
    m.write(dumps({"fields": fields}, ensure_ascii=False, indent=1))
    m.close()
