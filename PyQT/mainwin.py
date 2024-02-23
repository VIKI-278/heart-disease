import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox,QApplication,QWidget
from PySide6.QtGui import QGuiApplication
from ui_mainwin import Ui_mainwin
from sklearn.naive_bayes import GaussianNB 
from joblib import load
import numpy as np
import warnings
from sklearn.exceptions import InconsistentVersionWarning

# Suppress warnings
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)


warnings.filterwarnings("ignore", message="X does not have valid feature names, but GaussianNB was fitted with feature names")


class MainUI(QWidget, Ui_mainwin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Heart Disease prediction")
        self.sex.addItems(['Male','Female'])
        self.chestpain.addItems(['Typical Angina','Atypical Angina','Non-Anginal Pain',"Asymptomatic"])
        self.fastbs.addItems(['High','Low'])
        self.restingecg.addItems(['normal','ST','LVH'])
        self.angina.addItems(['Yes','No'])
        self.stslope.addItems(['up','down','flat'])
        self.pushButton.clicked.connect(self.pred_clicked) #what happens when prdict button is clicked

    def pred_clicked(self):
        input_fields = {
            "Age": self.age,
            "Restingbp": self.restingbp,
            "Cholestrol": self.cholestrol,
            "Maxheartrate": self.maxheartrate,
            "Oldpeak": self.oldpeak
        }

        #check for empty data inputs and has correct data type
        empty_fields = [name for name, field in input_fields.items() if (field.toPlainText() == "" or (not field.toPlainText().isnumeric()))] 

        if empty_fields:
            field_names = empty_fields[0]
            ret = QMessageBox.critical(self, "Input error", f"{field_names} cannot be blank/have alphabets", QMessageBox.Ok)
        

        else:
            self.predict()
            
    def predict(self):
        #data pre processing
        age = int(self.age.toPlainText())
        sex = str(self.sex.currentText())
        chestpaintype = str(self.chestpain.currentText())
        restingbp = int(self.restingbp.toPlainText())
        cholestrol = int(self.cholestrol.toPlainText())
        fastingbs = str(self.fastbs.currentText())
        restingecg = str(self.restingecg.currentText())
        maxHR = int(self.maxheartrate.toPlainText())
        excerciseangina =str(self.angina.currentText())
        oldpeak = int(self.oldpeak.toPlainText())
        st_slope = str(self.stslope.currentText())

        if sex == "Male":
            sex_M = 1
        else:
            sex_M = 0
        if chestpaintype == 'Atypical Angina':
            chestpaintype_ATA = 1 
            chestpaintype_NAP = 0
            chestpaintype_TA =0
        elif chestpaintype == 'Non-Anginal Pain':
            chestpaintype_ATA = 0
            chestpaintype_NAP = 1
            chestpaintype_TA = 0
        elif chestpaintype == 'Typical Angina':
            chestpaintype_ATA = 0 
            chestpaintype_NAP = 0
            chestpaintype_TA = 1
        else :
            chestpaintype_ATA = 0 
            chestpaintype_NAP = 0
            chestpaintype_TA = 0

        if restingecg == 'normal': 
            restingecg_normal = 1
            restingecg_st = 0
        elif restingecg == 'ST': 
            restingecg_normal = 0
            restingecg_st = 1
        else:
            restingecg_normal = 0
            restingecg_st = 0

        if fastingbs == 'High':
            fbs = 1
        else: fbs=0
        if excerciseangina == 'YES':
            exang = 1
        else:
            exang =0
        
        if st_slope ==  'up':  
            st_slope_flat = 0
            st_slope_up = 1
        elif st_slope ==  'flat':
            st_slope_flat = 1
            st_slope_up = 0
        else:
            st_slope_flat = 0
            st_slope_up = 0

        #final Data array

        data = np.array([[age,restingbp,cholestrol,int(fbs),maxHR,oldpeak,int(sex_M),int(chestpaintype_ATA),int(chestpaintype_NAP),
                          int(chestpaintype_TA),int(restingecg_normal),int(restingecg_st),int(exang),int(st_slope_flat),int(st_slope_up)]])
        
        #Load the exported model

        loaded_model = load(r"C:\Users\Admin\Desktop\DSBA\Others\Portfolio prjt\Heart disease\ML\heartmodel.joblib") # change this to your path

        res = loaded_model.predict(data)[0]
        if res == 0:
            res_prob = round(loaded_model.predict_proba(data)[0][0] * 100,2) 
            ret = QMessageBox.information(self, "Positive", f"it is {res_prob} % possible that u have a heart disease", QMessageBox.Ok)
        else:
             res_prob = round(loaded_model.predict_proba(data)[0][1] * 100,2)
             ret = QMessageBox.information(self, "Negative", f"it is {res_prob} % possible that u don't have a heart disease", QMessageBox.Ok)

        
        




        
 

        