from firebird.driver import connect, driver_config, DatabaseError

driver_config.server_defaults.host.value = 'localhost'

try:
    driver_config.server_defaults.user.value = 'SYSDBA'
    driver_config.server_defaults.password.value = 'masterkey'
    
    conn = connect("C:/Users/JULIANA/Desktop/FIREBIRD_PY")
    print('Conexão estabelecida')
except DatabaseError as e:
    print(f'Erro de conexão')
finally: 
    conn.close
