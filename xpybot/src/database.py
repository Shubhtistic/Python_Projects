import json
from pathlib import Path as pt
import sys

class Json_DB:
    def __init__(self,filename:str =".processed_retweets.json"):
        self._filepath=pt(filename)
        self._processed_ids=set()
        # set gives us very fast lookup, o(1) on average
        self._load()
        # call the load function on object creation
    def _load(self):
        try:
            if(self._filepath.exists()):
                with open(self._filepath,'r',encoding='utf-8') as fl:
                    loaded_data=json.load(fl)
                    if(isinstance(loaded_data,list)):
                        self._processed_ids.update(str(item) for item in loaded_data)
                    else:
                        self._processed_ids=set()
                        print(f"Warning: Expected a list in {self._filepath}, but found {type(loaded_data)}. Starting fresh.", file=sys.stderr)
                    # In print(..., file=sys.stderr), file tells Python where to send the output
                    #sys.stderr means the message goes to the error/warning stream instead of normal output
        except json.JSONDecodeError:
            
            # case when file exists but the json format is not of proper format
            print(f"Warning: Error decoding JSON from {self._filepath}. Starting fresh.", file=sys.stderr)
            self._processed_ids = set() # start with empty set
            
        except Exception as e:
            # catch any other unexpected file reading errors
            print(f"Error loading data from {self._filepath}: {e}", file=sys.stderr)
            self._processed_ids = set() 
    def _save(self):
        try:
            with open(self._filepath,'w',encoding='utf-8') as fl:
                ids_list=list(self._processed_ids)
                # json has no data strcure like set 
                # so lets use list 
                json.dump(ids_list,fl,indent=4,ensure_ascii=False)
        except Exception as e:
            # catch any unexpected file writing errors.
            print(f"Error saving data to {self._filepath}: {e}", file=sys.stderr)
    def add_processed_id(self,tweet_id):
        # adding an inviual id to processed_ids set
        str_id=str(tweet_id)
        self._processed_ids.add(str_id)
        # call the save method
        self._save()
    def is_processed(self,tweet_id)->bool:
        str_id=str(tweet_id)
        return str_id in self._processed_ids