from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime
import pandas as pd
from homeharvest import scrape_property  # Assuming you have a module named homeharvest.py

app = Flask(__name__, template_folder='templates')

###INSTALL FLASK, HOMEHARVEST AND PANDAS BEFORE STARTING

@app.route("/")
def home():
    # Redirect to the search page when accessing the root URL
    return redirect(url_for("search"))

@app.route("/search", methods=["POST", "GET"])
def search():
    # List of available listing types
    listingTypeList = ['for_sale', 'for_rent', 'pending'] 

    if request.method == "POST":
        # Get form data
        location = request.form["location"]
        days = request.form["days"]
        listingType = request.form["listingType"]

        # Generate filename based on current timestamp
        current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"HomeHarvest_{current_timestamp}.csv"

        # Scraping properties based on form data
        properties: pd.DataFrame = scrape_property(
            location= location,
            listing_type= listingType, # for_sale / sold
            past_days= days
        )

        # Export scraped properties to CSV
        properties.to_csv(filename, index=False)

        # Render the result template with form data and filename
        return render_template("result.html", location=location, days=days, listingType=listingType, filename=filename, properties=properties)
    
    else:
        # Render the search page with the list of available listing types
        return render_template("search.html", listingTypeList=listingTypeList)

@app.route("/result")
def show_result(location, days, listingType, filename):
    return render_template("result.html", location=location, days=days, listingType=listingType, filename=filename)

if __name__ == "__main__":
    app.run(debug=True)
