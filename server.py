from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from forms import rowForm
import csv
import pandas as pd
import string


app = Flask(__name__)
app.secret_key = "forNow100X"


@app.route('/')
def index():
    myform = rowForm()
    return render_template('index.html', x=myform)


@app.route('/input', methods=['GET', 'POST'])
def input():
    myForm = rowForm()
    #x = request.form("field1")
    output = request.form.get("x")
    rowValue = int(output)
    review = pd.read_csv("C:/Users/mpink/Onedrive/Desktop/New_Folder/Actual_Website/Export1.csv")
    review2 = pd.read_csv("C:/Users/mpink/Onedrive/Desktop/New_Folder/Actual_Website/Cleaned_million1.csv")
    review3 = pd.read_csv("C:/Users/mpink/OneDrive/Desktop/New_Folder/Actual_Website/sentiment.csv")
    actualReview = review["reviewText"]
    actualReview2 = review2["reviewText"]
    actualReview3 = review3["prediction"]
    ##flash("The data to be printed is: " + output)
    #print("The data to be printed is: ", x)
    ##return redirect(url_for("index"))
    return render_template("aftersubmit.html", text = output, text2 = actualReview[rowValue], text3 = actualReview2[rowValue], text4 = actualReview3[rowValue])


if __name__ == '__main__':
    app.run(debug=True)
