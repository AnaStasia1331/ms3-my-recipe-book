import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def get_homepage():
    return render_template("index.html")


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "course_name": request.form.get("course_name"),
            "ingredients": request.form.get("ingredients"),
            "steps": request.form.get("steps"),
            "preparation_time": request.form.get("preparation_time")
        }
        mongo.db.recipes.insert_one(recipe)
        return redirect(url_for("get_recipes", _anchor='allRecipes'))

    courses = mongo.db.courses.find()
    return render_template("add_recipe.html", courses=courses)



@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "course_name": request.form.get("course_name"),
            "ingredients": request.form.get("ingredients"),
            "steps": request.form.get("steps"),
            "preparation_time": request.form.get("preparation_time")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        return redirect(url_for("get_recipes", _anchor='allRecipes'))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    courses = mongo.db.courses.find()
    return render_template("edit_recipe.html", recipe=recipe, courses=courses)


@app.route("/view_recipe/<recipe_id>")
def view_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    # refer to https://stackoverflow.com/questions/28593235/get-referring-url-for-flask-request/28593313#28593313
    referrer = request.headers.get("Referer")
    return redirect(referrer)


@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("all_recipes.html", recipes=recipes)


@app.route("/course/<course>")
def get_course(course):
    recipes = list(mongo.db.recipes.find({"course_name": course.capitalize()}))
    return render_template("{}.html".format(course), recipes=recipes)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)