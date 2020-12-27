from flask import Flask, render_template, request, redirect, url_for, flash
# from flask_script import Manager, Command, Shell
from forms import ItemInsertForm
from forms import ItemRemoveForm
import requests
import pandas as pd
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a really really really really long secret key'


@app.route('/insert/', methods=['get', 'post'])
def insert():
    form = ItemInsertForm()
    # resp = requests.get("https://ksl-classifieds.herokuapp.com/api/keywords")
    # keywords = resp.json().get("keywords")
    if form.validate_on_submit():

        # df = pd.read_csv('keywords.csv')

        item_name = form.item_name.data
        minimum = form.minimum.data
        maximum = form.maximum.data
        print(item_name)
        print(minimum)
        print(maximum)
        print("\nData received. Now redirecting ...")
        endpoint = "https://ksl-classifieds.herokuapp.com/api/add-keyword"
        data = {"item_name": item_name,
                "minimum_price": minimum, "maximum_price": maximum}
        resp = requests.post(endpoint, json=data)

        if resp.status_code == 200:
            flash(f"{item_name} successfully added to the database")
            print("Data added successfully")
            return redirect(url_for('insert'))

        # found = df[df['Item'].str.contains(item_name)]
        # isFound = found['Item'].count()
        # print(isFound)

        # if(isFound==0):
        #     print ("Unique Item Name")
        #     new_item = {'Item':item_name, 'Minimum': minimum, 'Maximum': maximum}
        #     print (new_item)
        #     new_df = df
        #     new_df = new_df.append(new_item, ignore_index=True)
        #     new_df.reset_index(drop=True, inplace=True)
        #     new_df.to_csv('keywords.csv', index=False)
        #     print ("Successfully inserted Item - ", item_name)
        else:
            print("Something went wrong")
            return render_template('add-item.html', form=form)

    return render_template('add-item.html', form=form)


@app.route('/delete/', methods=['get', 'post'])
def delete():
    # form = ItemRemoveForm()
    resp = requests.get("https://ksl-classifieds.herokuapp.com/api/keywords")
    keywords = resp.json().get("keywords")

    return render_template('remove-keyword.html', keywords=keywords)

    # if form.validate_on_submit():

    #     df = pd.read_csv('keywords.csv')

    #     item_name = form.remove_item_name.data

    #     print(item_name)

    # print("\nData received. Now Searching for removal ...")

    # endpoint = f"https://ksl-classifieds.herokuapp.com/api/keywords/delete/{item_name}"
    # resp = requests.post(endpoint)
    # if resp.status_code == 200:
    #     flash(f"{item_name} successfully deleted from the database")
    #     return redirect(url_for('delete'))
    # found = df[df['Item'].str.contains(item_name)]
    # isFound = found['Item'].count()
    # print(isFound)

    # if(isFound != 0):
    #     print("Item found")
    #     new_df = df
    #     new_df = new_df[new_df.Item != item_name]
    #     new_df.reset_index(drop=True, inplace=True)
    #     new_df.to_csv('keywords.csv', index=False)
    #     print("Successfully Deleted Item - ", item_name)
    # else:
    #     print("Not found")

    # return render_template('delete.html', form=form)


@app.route("/remove/")
def remove_keyword():
    # endpoint = f"https://ksl-classifieds.herokuapp.com/api/keywords/delete/{item_name}"
    # resp = requests.post(endpoint)
    # if resp.status_code == 200:
    #     flash(f"{item_name} successfully deleted from the database")
    #     return redirect(url_for('delete'))
    return render_template("remove-keyword.html")


@app.route('/', methods=["POST", "GET"])
def index():
    url_endpoint = "https://ksl-classifieds.herokuapp.com/api/products"
    resp = requests.get(url_endpoint)
    if resp.status_code == 200:
        products = resp.json().get("products")
        return render_template('index.html', products=products)

    # return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
