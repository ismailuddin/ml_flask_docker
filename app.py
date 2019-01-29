from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import Form, FloatField, validators
from sklearn.externals import joblib
import numpy as np


app = Flask(__name__)
# Required for FlaskForm to work
app.config['SECRET_KEY'] = 'xRLc01ve5Hiycc9DbRk99QC9znuRkMN1'


class MLModel:
    """
    This class loads the saved model from sklearn, and provides a predict
    function which handles all the necessary data transformations.
    """
    def __init__(self):
        self.model = joblib.load('models/Iris_SVC.joblib')

    def predict(self, sepal_length: float, sepal_width: float, 
                petal_length: float, petal_width: float) -> str:
        """
        This function calls the `.predict()` function on the ML model, but 
        crucially, transforms the input data into the correct format.

        Returns:
            str: Predicted species
        """
        species = self.model.predict(
            np.array([
                [
                    sepal_length,
                    sepal_width,
                    petal_length,
                    petal_width
                ]
            ])
        )[0]
        return str(species)

ml_model = MLModel()


class IrisForm(FlaskForm):
    """
    This class setups the code to generate and handle a HTML form
    """

    sepal_length = FloatField(
        'Sepal length', [validators.NumberRange(min=0, max=20)]
    )
    sepal_width = FloatField(
        'Sepal width', [validators.NumberRange(min=0, max=20)]
    )
    petal_length = FloatField(
        'Petal length', [validators.NumberRange(min=0, max=20)]
    )
    petal_width = FloatField(
        'Sepal width', [validators.NumberRange(min=0, max=20)]
    )


@app.route("/", methods=['GET', 'POST'])
def main():
    """
    This function is called whenever we navigate to http://localhost:5000/
    """
    form = IrisForm()
    # If a validated form is detected being submitted
    if form.validate_on_submit():
        species = ml_model.predict(
            form.sepal_length.data,
            form.sepal_width.data,
            form.petal_length.data,
            form.petal_width.data
        )
        # Redirect to a different template where can inject the predicted 
        # species
        return render_template('species.html', species=species)
    # Otherwise, simply load the main page
    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
