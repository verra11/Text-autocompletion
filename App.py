from flask import Flask, render_template, jsonify,request

import time
print('Loading data')
import predict
import simplejson as json

app = Flask(__name__)

@app.route('/next_word',methods=['POST'])
def next_wrd():
    text=request.args.get('text')
    context=' '.join(text.split()[:4])
    return json.dumps(predict.predict(context,smoothing=1))


if __name__=="__main__":
    app.run()