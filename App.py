from flask import Flask, render_template, jsonify,request

import time
print('Loading data')
import predict
import simplejson as json

app = Flask(__name__)

@app.route('/output',methods=['POST', 'GET'])
def pred():
    text=str(request.args.get('text'))
    action=str(request.args.get('type'))
    context=' '.join(text.split()[-3:])
    current_word=context.split()[-1]

    if action == 'correct':
        return json.dumps(predict.crct_word(current_word))
    elif action == 'complete':
        return json.dumps(predict.predict_now(context,current_word))
    else:
        return json.dumps(predict.predict(context,smoothing=1))

if __name__=="__main__":
	app.run()