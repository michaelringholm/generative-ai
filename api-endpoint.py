from flask import Flask, request, jsonify, render_template
import json
#import bloom_bot_module as model_bot
#import gpt2_bot_module as model_bot
import dialo_bot_module as model_bot

LLMModelInitDone=False
meta=any
appName="web-api"
app = Flask(appName, template_folder='html')
#@app.route('/api/endpoint', methods=['POST'])
@app.route('/api/generateResponse', methods=['POST'])
def generateResponse():
    print("generateResponse() called...")
    global LLMModelInitDone
    global meta
    data = request.json
    print("JSON Reuqest=",request.json)
    prompt=request.json["prompt"]
    llm=request.json["llm"]
    if(LLMModelInitDone==False):
        meta=model_bot.init()
        LLMModelInitDone=True
    #bloom_bot_module.askQuestions()

    print("---------------------------------------------------------------")
    generatedResponse=model_bot.generate_response(meta.tokenizer, prompt, meta.device, meta.model)
    print(jsonify(generatedResponse))
    response = {'message': 'Success', "generated_response": generatedResponse}
    return jsonify(response)

@app.route('/', methods=['GET'])
def index():
    print("index() called...")
    #data = request.json
    response = {'message': 'Success'}
    return render_template('index.html')

app.run()