from flask import Flask, render_template, jsonify,request

import time
pre=time.time()
print('Loading data')
import predict
print('completed loading\n Firing server ....!!',time.time()-pre)
import simplejson as json

app = Flask(__name__)

@app.route('/next_word',methods=['POST'])
def next_wrd():
    req_data=request.get_json()
    context=' '.join(req_data['text'].split()[:4])
    return json.dumps(predict.predict(context,smoothing=1))


if __name__=="__main__":
    app.run()