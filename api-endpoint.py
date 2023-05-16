from flask import Flask, request, jsonify, render_template
import bloom_bot_module
import json

appName="web-api"
app = Flask(appName, template_folder='html')
#@app.route('/api/endpoint', methods=['POST'])
@app.route('/api/generateResponse', methods=['POST'])
def generateResponse():
    data = request.json
    meta=bloom_bot_module.init()
    #bloom_bot_module.askQuestions()
    print("Welcome to Bloom chat [using:", meta.model_name, "]")
    print("MODEL:", meta.model)
    print("DEVICE:", meta.device)
    print("MODEL_NAME:", meta.model_name)
    print("---------------------------------------------------------------")
    input_text = "In 30 words explain quantum physics?"
    generatedResponse=bloom_bot_module.generate_response(meta.tokenizer, input_text, meta.device, meta.model)
    print("---------------------------------------------------------------")
    input_text = "In max 50 words explain the rules of football as we know it in Europe?"
    bloom_bot_module.generate_response(meta.tokenizer, input_text, meta.device, meta.model)
    print("---------------------------------------------------------------")
    input_text = "In 20 words explain cloud computing?"
    bloom_bot_module.generate_response (meta.tokenizer, input_text, meta.device, meta.model)
    input_text = "In 20 words advise me how to make my teenage at home clean her room?"
    bloom_bot_module.generate_response(meta.tokenizer, input_text, meta.device, meta.model)
    input_text = "Create a short story, max 200 words, about a bear, a fox, and them playing football? The fox was evil."
    bloom_bot_module.generate_response(meta.tokenizer, input_text, meta.device, meta.model)
    response = {'message': 'Success', "response": generatedResponse}
    return jsonify(response)

@app.route('/', methods=['GET'])
def index():
    #data = request.json
    response = {'message': 'Success'}
    return render_template('index.html')

app.run()