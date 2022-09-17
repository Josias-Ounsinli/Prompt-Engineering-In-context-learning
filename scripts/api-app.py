import sys
import os
import pandas as pd
import cohere
from flask import Flask, request, jsonify, render_template

sys.path.append(os.path.abspath(os.path.join('../scripts')))
from apis import cohere_api

apikey = cohere_api['apikey']

# cohere class instance
co = cohere.Client(apikey)

# create an instance of the Flask class
app = Flask(__name__)

# job descriptions data

# Breaking news data
import load_data
bnewsdf = load_data.load_excel_file('data/Example_data.xlsx', './', 'Sv1')
data_use = bnewsdf[['Domain', 'Title', "Description", 'Body', 'Analyst_Average_Score']]

bnews_items_list = []
for i in range(len(data_use)):
    bnews_items = {}
    for j in range(len(data_use.iloc[i].index)):
        bnews_items[data_use.iloc[i].index[j]] = data_use.iloc[i][j]
    bnews_items_list.append(bnews_items)

def score_classify(x):
    if x < 0:
        result = 'Error: Negative score'
    elif x >= 0 and x < 4:
        result = 'Not relevant news'
    elif x < 7:
        result = 'Relevant news'
    elif x <= 10:
        result = 'Very relevant news'
    else:
        result = 'Error: Score greater than 10'
    return result

bnews_pred = []

@app.route('/main')
def index():
    """Render the index page."""
    # Main page
    return jsonify({
                "status": "success",
                "message": "Welcome to this app of job description entity extraction (/jdentities ) and scoring breaking news (/bnewscore )!"
             })

### First endpoint: /endpoint

@app.route('/jdentities', methods=['GET', 'POST'])
def jdentities_route():
    """job description entities route."""
    if request.method == 'GET':
        return jsonify({"status": "success", "message": "Get item!"})
    elif request.method == 'POST':        
        return jsonify({"status": "sucess", "message": "Post Route for items!"})


### Second endpoint: /bnewscore

@app.route('/bnewscore', methods=['GET', 'POST'])
def bnewscore_route():
    """breaking news scores route."""
    if request.method == 'GET':
        return jsonify({"status": "success", "message": "Get item!", "bnews": bnews_items_list, "bnews predicted": bnews_pred})
    elif request.method == 'POST':
        Domain = request.get_json()['Domain']
        Title = request.get_json()['Title']
        Body = request.get_json()['Body']
        Description = request.get_json()['Description']
        
        # construct prompt to predice
        toPredict = f"Domain: {Domain}\nTitle: {Title}\nBody: {Body}\nDescription: {Description}\nAnalyst_Average_Score:"
        prompt = f"Domain: {bnews_items_list[7]['Domain']}\nTitle: {bnews_items_list[7]['Title']}\nBody: {bnews_items_list[7]['Body']}\nDescription: {bnews_items_list[7]['Description']}\nAnalyst_Average_Score: {bnews_items_list[7]['Analyst_Average_Score']}\n----\n"
        prompt += toPredict
        
        response = co.generate(
        model='xlarge',
        prompt= prompt,
        max_tokens=50,
        temperature=0.9,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=["----"],
        return_likelihoods='NONE')
        predicted_score = response.generations[0].text
        predicted_class = score_classify(float(predicted_score[0:5]))
        predicted_score = float(predicted_score[0:5])

        bnews_pred.append({"Domain": request.get_json()['Domain'],
        "Title": request.get_json()['Title'], "Body": request.get_json()['Body'],
        "Description": request.get_json()['Description'],
        "Analyst_Average_Score": predicted_score,
        "Classification": predicted_class})

        return jsonify({"status": "sucess", "message": "Post Route for items!", "Prompt": prompt, "Prediction": predicted_score, "Classification": predicted_class})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', debug=True, port=port)