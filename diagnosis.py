import requests

POST_URL = "https://api.infermedica.com/v2/symptoms"

header = { "app_id" : "9cfcafae", "app_key" : "55b78a933718c8e68ba37f2f8d80b1a7"}
#mapping format: "": ["","",""],
translator = {"alcohol":["beer","liqour","drink"],"abdominal": ["stomach", "tummy", "belly"], "abnormal": ["weird","not normal","unusual","odd","irregular","strange"], "absent": ["gone","missing","lack"],"absence":["gone","missing","lack"],"after":["after"], "accelerated": ["increasing","speeding"], "achilles": ["achilles"], "aggravated":["annoyed","irritated"],"agitation":["pissed","angry","uncalm"], "agnosia": ["phobia","fear","trapped","embarrassed","unescapable"],
"breath": ["breath","inhale","exhale"],
"craving":["crave","want"],"chronic":["persistent","constant"],"caffine":["caffine","coffee"],"coughing":["coughing","cough"],
"distension": ["enlarged","inflated"], "defecation":["pooping","bathroom","shitting"],"decrease":["less","lowered"],
"exacerbating": ["worst","worsen"],"emotional":["emotion"],
"flare-ups": ["random"],"face":["face"],
"heartbeat":["heartbeat","heart","beating"],"heat":["humidity"],
"increasing": ["increase","raises"],
"menstrual":["period"], "meal":["dinner","lunch","breakfast","food"],"movement":["exercise","moving","running"],
"negative":["bad"],
"phobia":["fear","scared",""],"pain": ["hurts","stings","aches","painful"],"pregnancy":["pregnant"],
"removal": ["removal","surgery"], "reduced": ["lessen","weaken"],"reflex":["flexibility"],
"severe":["serious","awful","intense","agonizing","unbearable","intolerable"], "sharp":["acute","painful","stabbing"], "sex":["sexual","intercourse"], "stress":["stressed"],
"tolerance":["inadequate","unsatisfied"],"tumor":["mass","bulge","cancer"], "tendon":["tendon"],
"withdrawal":["quit",""]
}

#creating a dictionary of name by id and print out the symptom through the id
'''
medicalDict = dict()
r = requests.get(POST_URL, headers=header)
json = r.json()
for key in json:
	medicalDict[key["id"]] = key['name']
id = raw_input().encode("utf-8")
print(medicalDict[id])
'''

#translating the string input
def stringTranslate(symptom):
	original = symptom.lower().split()
	new = []
	for word in original:
		for key, value in translator.iteritems():
			if word in value:
				new.append(key)
			elif word == key:
				new.append(word)
	return(" ".join(new))

Translated_String = stringTranslate(raw_input()).capitalize()
print(Translated_String)
