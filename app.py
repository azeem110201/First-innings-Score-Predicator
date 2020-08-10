from flask import Flask,render_template,request
import pickle
import numpy as np

filename = 'first-innings-score-rfr-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def predict_method():

    temp = list()

    if request.method == 'POST':

        venue = request.form['venue']
        if venue == 'Brabourne Stadium':
            temp.append(2)
        elif venue == 'Himachal Pradesh Cricket Association Stadium':
            temp.append(11)
        elif venue == 'M Chinnaswamy Stadium':
            temp.append(15)
        elif venue == 'Saurashtra Cricket Association Stadium':
            temp.append(26)
        elif venue == 'Maharashtra Cricket Association Stadium':
            temp.append(17)
        elif venue == 'Barabati Stadium':
            temp.append(1)
        elif venue == 'MA Chidambaram Stadium, Chepauk':
            temp.append(16)
        elif venue == 'Punjab Cricket Association IS Bindra Stadium, Mohali':
            temp.append(22)
        elif venue == 'Feroz Shah Kotla':
            temp.append(9)          
        elif venue == 'Wankhede Stadium':
            temp.append(35)
        elif venue == 'Punjab Cricket Association Stadium, Mohali':
            temp.append(23)           
        elif venue == 'Sardar Patel Stadium, Motera':
            temp.append(25)
        elif venue == 'Green Park':
            temp.append(10)

        elif venue == 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
            temp.append(6)
        elif venue == "St George's Park":
            temp.append(31) 
        elif venue == 'Holkar Cricket Stadium':
            temp.append(12) 
        elif venue == 'Sharjah Cricket Stadium':
            temp.append(29) 
        elif venue == 'De Beers Diamond Oval':
            temp.append(4) 
        elif venue == 'Rajiv Gandhi International Stadium, Uppal':
            temp.append(24) 
        elif venue == 'Eden Gardens':
            temp.append(8)         
        elif venue == 'Sawai Mansingh Stadium':
            temp.append(27) 
        elif venue == 'SuperSport Park':
            temp.append(33)        
        elif venue == 'Kingsmead':
            temp.append(14) 
        elif venue == 'Sheikh Zayed Stadium':
            temp.append(30)     

        elif venue == 'Nehru Stadium':
            temp.append(18) 
        elif venue == "Vidarbha Cricket Association Stadium, Jamtha":
            temp.append(34) 
        elif venue == 'Dubai International Cricket Stadium':
            temp.append(7) 
        elif venue == 'JSCA International Stadium Complex':
            temp.append(13) 
        elif venue == 'Subrata Roy Sahara Stadium':
            temp.append(32)
        elif venue == 'Dr DY Patil Sports Academy':
            temp.append(5) 
        elif venue == 'Buffalo Park':
            temp.append(3)             
        elif venue == 'Shaheed Veer Narayan Singh International Stadium':
            temp.append(28) 
        elif venue == 'Newlands':
            temp.append(20)        
        elif venue == 'New Wanderers Stadium':
            temp.append(19) 
        elif venue == 'OUTsurance Oval':
            temp.append(21)
        else:
            temp.append(36)


        bat_team = request.form['bat_team']

        if bat_team == 'Chennai Super Kings':
            temp.append(1) 
        elif bat_team == "Deccan Chargers":
            temp.append(2) 
        elif bat_team == 'Delhi Daredevils':
            temp.append(3) 
        elif bat_team == 'Gujarat Lions':
            temp.append(4) 
        elif bat_team == 'Kings XI Punjab':
            temp.append(5) 
        elif bat_team == 'Kochi Tuskers Kerala':
            temp.append(6) 
        elif bat_team == 'Kolkata Knight Riders':
            temp.append(7)          
        elif bat_team == 'Mumbai Indians':
            temp.append(8) 
        elif bat_team == 'Pune Warriors':
            temp.append(9)           
        elif bat_team == 'Rajasthan Royals':
            temp.append(10) 
        elif bat_team == 'Rising Pune Supergiant':
            temp.append(11) 
        elif bat_team == 'Rising Pune Supergiants':
            temp.append(12)        
        elif bat_team == 'Royal Challengers Bangalore':
            temp.append(13) 
        elif bat_team == 'Sunrisers Hyderabad':
            temp.append(14) 
        else:
            temp.append(15) 

        bowl_team = request.form['bowl_team']

        if bowl_team == 'Chennai Super Kings':
            temp.append(1) 
        elif bowl_team == "Deccan Chargers":
            temp.append(2) 
        elif bowl_team == 'Delhi Daredevils':
            temp.append(3) 
        elif bowl_team == 'Gujarat Lions':
            temp.append(4) 
        elif bowl_team == 'Kings XI Punjab':
            temp.append(5) 
        elif bowl_team == 'Kochi Tuskers Kerala':
            temp.append(6) 
        elif bowl_team == 'Kolkata Knight Riders':
            temp.append(7)         
        elif bowl_team == 'Mumbai Indians':
            temp.append(8) 
        elif bowl_team == 'Pune Warriors':
            temp.append(9)             
        elif bowl_team == 'Rajasthan Royals':
            temp.append(10) 
        elif bowl_team == 'Rising Pune Supergiant':
            temp.append(11) 
        elif bowl_team == 'Rising Pune Supergiants':
            temp.append(12)            
        elif bowl_team == 'Royal Challengers Bangalore':
            temp.append(13) 
        elif bowl_team == 'Sunrisers Hyderabad':
            temp.append(14)    
        else:
            temp.append(15) 


        runs = float(request.form['runs'])
        wickets = float(request.form['wickets'])
        overs = float(request.form['overs'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])    

        temp = temp + [runs, wickets,overs, runs_in_prev_5, wickets_in_prev_5]
        
        data = np.array([temp])
        my_prediction = float(regressor.predict(data)[0])
        

        return render_template('results.html',lower_limit=my_prediction - 5,upper_limit=my_prediction + 10)

@app.route('/github')
def github():
    return render_template('github.html')    

@app.route('/linkedIn')
def linkedIn():
    return render_template('linkedIn.html')      


if __name__ == '__main__':
    app.run(debug=True)