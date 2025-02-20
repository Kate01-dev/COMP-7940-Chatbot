import configparser
config = configparser.ConfigParser()
config.read('7940_lab3/config.ini')

# print 
# Check if the 'TELEGRAM' section exists
if 'TELEGRAM' in config:
    print(config.get('TELEGRAM', 'ACCESS_TOKEN'))
else:
    print("Section 'TELEGRAM' not found in the config file.")