# To check that yml file is valid or not

import yaml
with open ('first.yml' , 'r') as file:
    try:
          print(yaml.safe_load(file))
    except yaml.YAMLError as exc:
         print(exc)






