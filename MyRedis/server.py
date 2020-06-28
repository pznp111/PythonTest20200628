import socket
import json


class Server():
    def __init__(self, host='127.0.0.1', port=31337, max_clients=64):
        self._serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._serv.bind(('0.0.0.0', 8090))
        self._serv.listen(5)
        self._store = {}
        self._commandList = ['get','set','delete','flush','mget','mset']
        self.typeObj ={
            'string':'%',
            'int':':'
        }


    def run(self):
        """function to keep server class running, and wait for client to connect

        Args:

        Returns:

        """
        while True:
            conn, addr = self._serv.accept()
            from_client = ''
            while True:
                data = conn.recv(4096)
                if not data: break

                recdata = json.loads(data.decode("utf-8"))
                print ("received full data from client:",recdata)
                dict = data.decode("utf-8")
                dict = json.loads(dict)

                print("received command from client",dict["command"])

                if dict["command"] == 'get':
                    value = self.get(dict["key"])
                    if value == None:
                        conn.send(bytearray('NULL', 'utf-8'))
                    if isinstance(value, str):
                        if value != None:
                            temp = bytearray(self.typeObj['string']+value, 'utf-8')
                            conn.send(temp)
                        else:
                            conn.send(bytearray('NULL', 'utf-8'))
                    if isinstance(value,int):
                        if value != None:
                            temp = bytearray(self.typeObj['int'] + str(value), 'utf-8')
                            conn.send(temp)
                        else:
                            conn.send(bytearray('NULL', 'utf-8'))




                if dict["command"] == 'set':
                    ret = self.set(dict["key"],dict["value"])
                    conn.send(bytearray(json.dumps(ret), 'utf-8'))

                if dict["command"] == 'delete':
                    # print("before delete", self._store)
                    ret = self.delete(dict["key"])
                    # print("after delete",self._store)
                    conn.send(bytearray(json.dumps(self._store), 'utf-8'))

                if dict["command"] == 'flush':
                    self.flush()
                    conn.send(bytearray(json.dumps(self._store), 'utf-8'))

                if dict["command"] == 'mset':
                    group =dict['group']
                    for key, value in group.items() :
                        self.set(key, value)
                    conn.send(bytearray(json.dumps(self._store), 'utf-8'))

                if dict["command"] == 'mget':
                    group =dict['group']
                    list = []
                    for key in group:
                        list.append(self.get(key))
                    conn.send(bytearray(json.dumps(list), 'utf-8'))

            conn.close()

    def get(self,key):
        if key in self._store:
            return self._store[key]
        else:
            return None

    def set(self,key,value):
        self._store[key] = value
        return self._store

    def delete(self,key):
        if key in self._store:
            return self._store.pop(key)

        return self._store

    def flush(self):
        self._store = {}
        return self._store
