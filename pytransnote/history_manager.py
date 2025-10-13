import json

class history_manager_class():
    def __init__(self):
        self.history_list=list()
        self.max_id=0


    def read_and_load_data(self):
        try:
            with open("history.json", "r",encoding='utf8') as file:
                data = json.load(file)
                if isinstance(data, list):
                    self.history_list.extend(data)
                    ## if the input as in list containing a lot of dicts 
                    ## extend all the indexes one by one
                else:
                    self.history_list.append(data)
                m_id=[item.get("ID",0) for item in self.history_list]
                self.max_id=max(m_id,default=0)

                return True
        except (FileNotFoundError, json.JSONDecodeError):
            self.history_list = []
            return False


    def save_data(self):
        with open("history.json","w") as file:
            json.dump(self.history_list,file,indent=4)
            ## at program end we simply dump entire file into the json file


