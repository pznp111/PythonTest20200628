import socket
import json



class Client(object):
    def __init__(self, host='127.0.0.1', port=31337):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect(('0.0.0.0', 8090))
        self._commandList = ['get','set','delete']

    def close(self):
        self._client.close()

    def get_com(self,command,key):
        """function to execute 'get' command, only support string and int due to contrain of implementation of time in the return type
        first position in the bytesarray is used to indicate if return result is string(%) or int(:)

        Args:
            command : get
            key: key to get result

        Returns:
            value based on the key
        """
        jsonObj = json.dumps({'command': command,'key':key})
        self._client.sendall(bytearray(jsonObj, 'utf-8'))
        from_server = self._client.recv(4096).decode("utf-8")
        # print("receive",from_server)
        if from_server == 'NULL':
            return None
        else:
            str = from_server
            if from_server[0] == '%': #string
                return str[1:]
            elif from_server[0] == ':': #int
                return int(from_server[1:])

    def delete_com(self,command,key):
        """function to execute 'delete'

        Args:
            command : delete
            key: key to delete result

        Returns:
            full obj after delete
        """
        jsonObj = json.dumps({'command': command,'key':key})
        self._client.sendall(bytearray(jsonObj, 'utf-8'))
        from_server = self._client.recv(4096)


    # def mget_com(self, command, keylist):
    #     jsonObj = json.dumps({'command': command, 'key': key})
    #     self._client.sendall(bytearray(jsonObj, 'utf-8'))
    #     from_server = self._client.recv(4096)
    #     #
    #     print(from_server)

    def set_com(self,command,key,value):
        """function to execute 'get'

        Args:
            command : get
            key: key to get result
            value: value to the key

        Returns:
            full obj after set
        """
        jsonObj = json.dumps({'command': command,'key':key,'value':value})
        self._client.sendall(bytearray(jsonObj, 'utf-8'))
        from_server = self._client.recv(4096)
        # print (from_server)

    def flush_com(self):
        """function to execute 'flush'

        Returns:
            full obj after set, which is empty
        """
        jsonObj = json.dumps({'command': command})
        self._client.sendall(bytearray(jsonObj, 'utf-8'))
        from_server = self._client.recv(4096)
        print(from_server)


    # def execute(self, command,key,value):
    #     print()
    #     if(command in self._commandList):
    #         print()
    #     else:
    #         print("invalid command")


    def get(self, key):
        return self.get_com('get', key)

    def set(self, key, value):
        return self.set_com('set', key, value)

    def delete(self, key):
        return self.delete_com('delete', key)

    def flush(self):
         return self.flush_com('flush')

    def mget(self, *keys):
        return [self.get_com('get', key) for key in keys]

    def mset(self, *items):
        data = zip(items[::2], items[1::2])
        for key, value in data:
            self.set_com('set', key, value)
        return
        # return [self.get_com('get', key) for key in keys]

