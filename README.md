# egrowr
eGrowr Python monitoring script

https://egrowr.com/

If you have this hydroponic monitoring device and want to use personal/custom python script to interact with, here you go.
The original script available on their website is originating from this code since I wrote it for me/them. https://egrowr.com/support/download/egrowrCollector.rar

Feel free to use and modify it according to your needs.

Requirements: Python3

Usage: python3 egrowrCollector.py [EGROWR_IP]

Example: python3 egrowrCollector.py 192.168.1.25

Output format: JSON

Example: {"egrowr_1011123456":{"Air_Temperature":17.6,"Air_Humidity":59.8,"Water_Temperature":16.8,"Water_EC":0.62,"Water_pH":7.88,"Light_intensity":44.5,"Uptime":840822,"Writes_on_flash":47}}
