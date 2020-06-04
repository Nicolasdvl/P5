name = 'root'
password = ''
db = 'p5'
data_size = 5

uri = 'mysql+pymysql://'+name+':'+password+'@localhost/'+db
    
request = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&page_size='+str(data_size)+'&json=true'