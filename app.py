from flask import Flask, render_template
app = Flask(__name__)
PRODUCTS = [
    {"id":1,"category":"Farm","pest":"Fall Armyworm","chemical":"Escort 19EC","use":"Maize armyworm kills in 48hrs","price":850,"image":"🌽"},
    {"id":2,"category":"Farm","pest":"Aphids / Thrips","chemical":"Taurus 5%","use":"Vegetables, tomatoes, beans","price":450,"image":"🍅"},
    {"id":3,"category":"Farm","pest":"Tuta Absoluta","chemical":"Belt 480SC","use":"Tomato leafminer","price":1200,"image":"🍅"},
    {"id":4,"category":"Public Health","pest":"Mosquitoes","chemical":"Icon 10CS","use":"IRS spray 6 months WHO approved","price":950,"image":"🦟"},
    {"id":5,"category":"Public Health","pest":"Cockroaches","chemical":"Goliath Gel","use":"Kitchen gel kills colony","price":1250,"image":"🪳"},
    {"id":6,"category":"Public Health","pest":"Bedbugs","chemical":"Bedlam 200SL","use":"Spray beds 100 percent kill","price":1100,"image":"🛏️"},
    {"id":7,"category":"Public Health","pest":"Rats / Mice","chemical":"Ratimor","use":"Rat bait 1 feed kill","price":350,"image":"🐀"},
    {"id":8,"category":"Public Health","pest":"Houseflies","chemical":"Agita 10WG","use":"Fly bait dairy safe","price":800,"image":"🪰"},
]
@app.route('/')
def home():
    return render_template('index.html', products=PRODUCTS)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
