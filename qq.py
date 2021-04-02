import nltk
import os

#root = os.path.dirname(os.path.abspath(__file__))
#download_dir = os.path.join(root, 'nltk_data')
#os.chdir(download_dir)
nltk.data.path.append("./nltk_data")

def isq(sent):
    if sent.endswith('?'):
        return True
    elif sent[:sent.index(' ')] in ['is', 'does', 'what', 'when', 'where', 'who', 'why', 'what', 'how']:
        return True
    else:
        return False

def is_ques(text):
    textlist = nltk.tokenize.sent_tokenize(text)
    if sum([isq(sent) for sent in textlist]) > 0:
        return "True"
    else:
        return "False"

def entry(request):
    content_type = request.headers['content-type']

    if content_type == 'application/json':
        data = request.get_json(silent=True)
        if data and 'password' in data and 'text' in data:
            if data['password'] == 'yoboshu_isqv01':
                return is_ques(data['text'])
            else:
                return "Not Authorized"
        else:
            return "JSON is invalid, or missing a 'password' or 'text' property"
    else:
        return "Error"

from flask import Flask, request
app = Flask(__name__)
@app.route('/',methods = ['GET'])
def epic():
    return entry(request)

if __name__ == '__main__':
   app.run(debug = True)