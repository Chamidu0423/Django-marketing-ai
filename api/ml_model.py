from sklearn.linear_model import LinearRegression
import joblib

def train_and_save_model():
    print("Training model...")

    #Fake Historical Data
    # X = Ad spend 
    X = [[50], [60], [70], [80], [100]]
    # y = Sales
    Y = [500, 610, 690, 820, 1010]

    model = LinearRegression()

    model.fit(X, Y)

    joblib.dump(model, 'model.pkl')

    print("Model trained and saved as model.pkl")

if __name__ == "__main__":
    train_and_save_model()