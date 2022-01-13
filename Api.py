import requests
import json

url = 'https://bellard.org/textsynth/api/v1/engines/gptj_6B/completions'

newHeaders = {
'Content-Type': 'application/json',
'Accept': '*/*'
    }

payload = {
"prompt": "In a shocking finding, scientist discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English.",
"seed": 0,
"stream": True,
"temperature": 1,
"top_k": 40,
"top_p": 0.9
}

response = requests.post(url, data=json.dumps(payload))

output = ''
texts = response.text.split("\n\n")
for line in texts:
    print(json.loads(line)['text'])
    output = str(json.loads(line)['text'])
    #output += json.loads(line)['text']
    
print(output)
