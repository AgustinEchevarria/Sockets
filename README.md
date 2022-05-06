# Sockets
Manejo de sockets

Requisitos:
            socket, ssl
Pasos:
        1_ Importar ShadownSocket (from ShadownSocket import *)
        
Funciones:
          
          SearchIp(host) # Recive un string "Host" como parametro y retorna un string con el valor de ip;
          
          CreateTcpIpv4Sock(ip,port,adrr='127.0.0.1',t=10,portr=8080) # Ip(string) a conectar el socket - port(int) a conectar - addr(string) direccion local - portr(int) puerto local a utilizar - t(int) tiempo de espera de coneccion, si el plazo se cumple el socket se cierra, retorna un objeto socket conectado al ip y port especificados;
          
          Cifrate(soc,host) # soc(socket object) socket a cifrar - host(string) a conectar y cifrar, retorna un objeto socket cifrado con ssl;
          
          GetRequests(host,uri,cookie,others) # host(string) host a colocar en el encabezado Host - uri(string) path a hacer el request - cookie(string) cookie a utilizar (opcional) - others(string) agregue encabezados a su requests ('\r\nENCABEZADO: KEY'), retorna una peticion GET en una cadena string; 
          
          PostRequests(data,host,uri,content_type,user_agent,cookie,others) # data(string) data a enviar - host(string) host a colocar en el encabezado Host -uri(string) path a donde enviar el requests POST - content_type(string) tipo de contendido de data - user_agent(string) agente a colocar en el encabezado User-Agent - cookie(string) agregue cookies a su solicitud - others(string) la misma definicion, retorna una peticion POST en una cadena string;
          
          SandRData(data,soc,time) # data(string) data a enviar por el socket - soc(socket object) socket a utilizar - time(int) Tiempo de espera antes de cerrar el socket al recivir la informacion, retorna la respuesta del servidor ala solicitud(data) en una cadena de bytes;
          
        
Ejemplos:

        from ShadownSocket import *
        host = 'www.google.com'
        ip = SearchIp(host)
        port = 443
        soc = CreateTcpIpv4Sock(host,port)
        soc = Cifrate(soc,host)
        data = GetRequests(host,uri='/search',cookie='SESSION: 654sad684a4d6w81ad;',others='\r\nOtherHeader: KEY')
        data_recived = SandRData(data,soc)
        print(data_recive.decode())
