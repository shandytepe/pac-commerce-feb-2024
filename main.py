from tabulate import tabulate
from math import sqrt

class Membership:
    
    # inisialisasi data
    data = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }
    
    # inisialisai attribute
    def __init__(self, username):
        self.username = username
        
    # method untuk menampilkan benefit membership
    def show_benefit(self):
        # init headers
        headers = ["Membership", "Discount", "Benefits"]
        
        # init data
        tables = [
                    ["Platinum", "15%", "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
                    ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
                    ["Silver", "8%", "Voucher Makanan"]
                ]
        
        print("Benefit PacCommerce Membership")
        print("")
        print(tabulate(tables, headers, tablefmt = "github"))
        
    # method untuk menampilkan requirements membership
    def show_requirements(self):
        # init headers
        headers = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]
        
        # init data
        tables = [
                    ["Platinum", 8, 15],
                    ["Gold", 6, 10],
                    ["Silver", 5, 7]
                ]
        
        print("Requirements PacCommerce Membership for each Tier")
        print("")
        print(tabulate(tables, headers, tablefmt = "github"))
        
    # method untuk melakukan prediksi membership
    # menggunakan euclidean distance
    def predict_membership(self, username, monthly_expense, monthly_income):
        
        # init parameter data
        parameter_data = [[8, 15], [6, 10], [5, 7]]
        
        # create empty list
        result_tmp = []
        
        for idx, _ in enumerate(parameter_data):
            euclidean_dist = round(sqrt((monthly_expense - parameter_data[idx][0])**2 + \
                                  (monthly_income - parameter_data[idx][1])**2), 2)
            
            result_tmp.append(euclidean_dist)
            
        dict_result = {
            "Platinum": result_tmp[0],
            "Gold": result_tmp[1],
            "Silver": result_tmp[2]
        }
        
        print(f"Hasil prediksi user {username} adalah berikut {dict_result}")
            
        # get minimum values from list
        get_min_distance = min(result_tmp)
        
        # iterate in dictionary data
        for key, value in dict_result.items():
            
            # compare with minimum data
            if get_min_distance == value:
                print(key)
                
                self.data[username] = key
    
    # method untuk menampilkan membership yang dimiliki
    # dari database yang dimiliki
    def get_membership(self, username):
        
        for key, value in self.data.items():
            if username == key:
                print(value)
                               
    # method untuk menghitung final price berdasarkan membership

    def calculate_price(self, username, list_harga):
        
        try:
            if username in self.data:
                
                membership = self.data.get(username)
                
                if membership == "Platinum":
                    total_harga = sum(list_harga) - (sum(list_harga) * 0.15)
                    return total_harga

                elif membership == "Gold":
                    total_harga = sum(list_harga) - (sum(list_harga) * 0.10)
                    return total_harga

                elif membership == "Silver":
                    total_harga = sum(list_harga) - (sum(list_harga) * 0.08)
                    return total_harga

                else:
                    raise Exception("Membership doesn't exist")
                    
            else:
                raise Exception("Membership tidak ada di database")
                
        except:
            raise Exception("Invalid process")
        
user_1 = Membership(username = "Shandy")

# check username
print(user_1.username)

# check benefit
print(user_1.show_benefit())

# predict membership
user_1.predict_membership(username = "Shandy",
                          monthly_expense = 5,
                          monthly_income = 20)