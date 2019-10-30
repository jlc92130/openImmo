
import mysql.connector
import csv

# creation of table dvf in the database named vf (vf has been manualy created in Mysql)
try:
    conn = mysql.connector.connect(host="localhost",
    user="root", password="", 
    database="vf")
    
    
    mySql_create = """
    CREATE TABLE IF NOT EXISTS dvf (
    id int(9) NOT NULL,
    date_mutation varchar(100) DEFAULT NULL,
    valeur_fonciere varchar(100) DEFAULT NULL,
    adresse_numero varchar(100) DEFAULT NULL,
    adresse_nom_voie varchar(100) DEFAULT NULL,
    code_postal INT(6),
    nom_commune varchar(100),
    type_local varchar(100),
    surface_reelle_bati varchar(100),
    longitude varchar(100),
    latitude varchar(100),
    PRIMARY KEY (id) ) """

    cursor = conn.cursor()
    resultat = cursor.execute(mySql_create)

# fetch table vf from csv file
 
    csv_data = csv.reader('C:\wamp64\www\jl\ReactNative\creation_bdd\full.csv')
    for row in csv_data:    
        cursor.execute('''INSERT INTO vf(id, date_mutation, valeur_fonciere, adresse_numero, adresse_nom_voie, code_postal, nom_commune, type_local, surface_reelle_bati, longitude,latitude)
        VALUES (row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9], row[10]) ''')   
        
      # cur = conn.cursor()
      # cur.executemany(sql_statement,[(row['id'],row['date_mutation'],row['valeur_fonciere'],row['adresse_numero'],
      # row['adresse_nom_voie'],row['code_postal'],row['nom_commune'],row['type_local'],row['surface_reelle_bati'],row['longitude'],row['latitude'])])
conn.commit()
   
