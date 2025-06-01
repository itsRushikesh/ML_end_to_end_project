from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = FastAPI()
app = application
# Templates directory setup
templates = Jinja2Templates(directory="templates")



# Route: Home page - index.html
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Route: GET - show form | POST - process form
@app.route("/predictdata", methods=["GET", "POST"])
async def predict_datapoint(request: Request):
    if request.method == "GET":
        return templates.TemplateResponse("home.html", {"request": request})
    else:
        form = await request.form()
        try:
            data = CustomData(
                gender=form.get("gender"),
                race_ethnicity=form.get("ethnicity"),
                parental_level_of_education=form.get("parental_level_of_education"),
                lunch=form.get("lunch"),
                test_preparation_course=form.get("test_preparation_course"),
                reading_score=float(form.get("reading_score")), 
                writing_score=float(form.get("writing_score"))   
            )

            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline = PredictPipeline()
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            print("After Prediction")

            return templates.TemplateResponse("home.html", {
                "request": request,
                "results": results[0]
            })

        except Exception as e:
            return templates.TemplateResponse("home.html", {
                "request": request,
                "results": f"Error occurred: {str(e)}"
            })
