import pickle
import pandas as pd
from sklearn import linear_model
import os




df = pd.read_csv('prices.csv')
y = df['Value'] 
X = df[['Rooms', 'Distance']]

lm = linear_model.LinearRegression()
lm.fit(X, y)
print(lm.predict([[15, 61]]))

# open a file, where you ant to store the data
file = open('model.pkl','wb')

# dump information to that file
pickle.dump(lm, file)

# close the file
file.close()


#pickle.dump(lm, open('model.pkl', 'wb'))
