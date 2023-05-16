from flask import Flask, request, jsonify, render_template
import bloom_bot_module
import json

LLMModelInitDone=False
meta=any
appName="web-api"
app = Flask(appName, template_folder='html')
#@app.route('/api/endpoint', methods=['POST'])
@app.route('/api/generateResponse', methods=['POST'])
def generateResponse():
    global LLMModelInitDone
    global meta
    data = request.json
    print("JSON Reuqest=",request.json)
    prompt=request.json["prompt"]
    llm=request.json["llm"]
    if(LLMModelInitDone==False):
        meta=bloom_bot_module.init()
        LLMModelInitDone=True
    #bloom_bot_module.askQuestions()

    print("---------------------------------------------------------------")
    generatedResponse=bloom_bot_module.generate_response(meta.tokenizer, prompt, meta.device, meta.model)
    print(jsonify(generatedResponse))
    response = {'message': 'Success', "generated_response": generatedResponse}
    return jsonify(response)

@app.route('/', methods=['GET'])
def index():
    #data = request.json
    response = {'message': 'Success'}
    return render_template('index.html')

app.run()