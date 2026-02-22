import json
import os
#os.mkdir("ApplyYourselfInterviewQuestion")
with open('SurveyBombQuestions.jet','r',encoding='utf-8') as f:
    content = json.load(f)
content = content["content"]
for item in content:
    
    os.makedirs("SurveyBombQuestions/" + item["id"], exist_ok=True)
    with open('SurveyBombQuestions/' + item["id"] + '/data.jet','r',encoding='utf-8') as f:
        data = json.load(f)
    fields = data["fields"]
    question = item["question"]
    fields[3]["s"] = question

    m = open("SurveyBombQuestions/" + item["id"] + "/data.jet","w",encoding="utf-8")
    m.write(json.dumps({"fields":fields},ensure_ascii=False,indent=1))
    m.close()