import pickle
import json
import config1
import numpy as np
import pandas as pd

class DataScienceSalary():

    def __init__(self,work_year, experience_level,
                                          employment_type, job_title,
                                        salary, salary_currency, employee_residence,
                                        remote_ratio,company_location,company_size) :
       self.work_year = work_year
       self.experience_level= experience_level
       self.employment_type = employment_type
       self.job_title= job_title
       self.salary = salary
       self. salary_currency =  salary_currency
       self.employee_residence = employee_residence
       self.remote_ratio= remote_ratio
       self.company_location = company_location
       self.company_size = company_size

       

    def __load_model(self): # Private Method
        # Load Model File
        with open(config1.MODEL_FILE_PATH, 'rb') as f:
            self.model = pickle.load(f)
            # print('self.model >>',self.model)

        # Load Project Data artifacts/knn_reg_model.pkl
        with open(config1.JSON_FILE_PATH,'r') as f:
            self.project_data = json.load( f)
            # print("Project Data :",self.project_data)

        # Load Normal Scaler File
        # with open(r'artifacts\std_scalar.pkl', 'rb') as f:
        #     self.scaler = pickle.load(f)
            # print('self.scaler >>',self.scaler)

    def get_predicted_res(self): # Public Method
        self.__load_model()
        array = np.zeros((1,self.model.n_features_in_))
        array[0][0] = self.project_data['work_year'][self.work_year]
        array[0][1] = self.project_data['experience_level'][self.experience_level]
        array[0][2] = self.project_data['employment_type'][self.employment_type]

        # print(job_title)
        job_title ='job_title_' + self.job_title 
        index = self.project_data['Column Names'].index(job_title)
        array[0][index] = 1

        array[0][3] = self.salary

        # print(salary_currency)
        salary_currency='salary_currency_'+self.salary_currency
        index = self.project_data['Column Names'].index(salary_currency)
        array[0][index] = 1

        # print(employee_residence)
        employee_residence='employee_residence_'+self.employee_residence
        index = self.project_data['Column Names'].index(employee_residence)
        array[0][index] = 1

        array[0][4] = self.remote_ratio

        # print(company_location)
        company_location ='company_location_'+self.company_location 
        index =self.project_data['Column Names'].index(company_location)
        array[0][index] = 1

        array[0][5] = self.project_data['company_size'][self.company_size]

        


        # # print("Test Array is :",array)
        # scaled_test_array = self.scaler.fit_transform(array)  
        # test_df = pd.DataFrame(scaled_test_array,columns=self.model.feature_names_in_)  

        salary_res= np.around(self.model.predict(array)[0],3)
        # print("Predicted Charges :", predicted_res)
        return salary_res
    

if __name__ == '__main__':
    cls = DataScienceSalary('2020','EN','FT','Data Scientist',58000,'EUR', 'DE',50,'DE','L')
    print(cls.get_predicted_res())
