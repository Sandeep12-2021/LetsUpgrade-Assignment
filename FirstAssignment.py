from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
import sklearn as sk
features =['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup',
       'Latitude', 'Longitude']

housing = fetch_california_housing(as_frame=True)

feature = housing.frame[features]
label = housing.frame['MedHouseVal']


x_train, x_test, y_train, y_test = sk.model_selection.train_test_split(feature,label,test_size=0.2,random_state=0)
model = RandomForestRegressor()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)

# print(y_pred," ",y_test)
print("Predicted values are:",y_pred)
print("Actual values are:",y_test)