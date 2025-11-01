from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def hello_world(request):
    """
    Hello World API view.
    """
    return Response({"message": "Hello, World!"})


import joblib
from django.conf import settings
import os

Model_PATH = os.path.join(settings.BASE_DIR, 'model.pkl')

try:
    model = joblib.load(Model_PATH)
    print(f"Model loaded successfully from {Model_PATH}")
except FileNotFoundError:
    print(f"Model file not found at {Model_PATH}")
    model = None
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@api_view(['POST'])
def predict_sales(request):
    if model is None:
        return Response({"error": "Model not loaded"}, status=500)
    try:
        data = request.data

        ad_spend_str = data.get('spend')
        if ad_spend_str is None:
            return Response({"error": "'Spend' parameter is required"}, status=400)
        
        ad_spend = float(ad_spend_str)

        prediction_input = [[ad_spend]]

        predicted_sales = model.predict(prediction_input)

        return Response({"predicted_sales": predicted_sales[0]})
    
    except ValueError:
        return Response({"error": "Invalid input for 'spend' must be a number"}, status=400)
    except Exception as e:
        return Response({"error": f"An error occurred: {str(e)}"}, status=500)