# kc-motorz
Code for KC-Motorz

git clone https://github.com/ebarras/kc-motorz.git
cd kc-motorz
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
mysql -u root
create database kcmotorz;
exit;
mysql -u root kcmotorz < test_data.sql
python app.py
