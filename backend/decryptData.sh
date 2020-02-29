decryptName='../resources/msgstore-2020-02-26.1.db.crypt12'
cd decrypt
python3 decrypt12.py key $decryptName
python3 retriveChats.py
mv data1.txt ../data1.txt