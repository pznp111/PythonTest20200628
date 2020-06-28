This is a simple Redis-like implementation using python

Support the following commands:<br/>
get(key)   to get value by key<br/>
set(key)   to save key value pair<br/>
delete(key)   to delete value by key<br/>
mget(key1,key2,.....,keyn)   get multiple value by keys<br/>
mset(key1,value1,key2,value2,.....keyn,valuen)   set multiple value by keys<br/>
flush()   delete all<br/>



To start the project, first run:<br/>
open one terminal, run: python runServer.py<br/>
open another termial, run python runClient.py<br/>



Due to constrain of time, it support string and int only

prequisite to this implementation including the following libraries:
socket,<br/>
support python3.+ version<br/>


This is how this implementation works:
1. making use of python socket library to simulate client and server environment
2. server would need to start first with default host and port, data will be save to in-memory dict object
3. client would send data (command,value,key) in json format, converted to bytesarray due to socket requirement
4. server side receive data, process data and convert to json object and then call corresponding functions accordingly, and return result to client
5. client receive result return from server and display

some Trade-offs, consideration and constrains:
1. client side does not know what is the value format(string or int) return from server, thus I append '%', ':' on the first postion of the return message, client side would need to read the first character, truncate it and convert to string or int accordingly.
2. saving of data is purely in in-memory dict object, once server is stopped all data is lost
3. due to constrain of time, only support string and int object
4. due to time constrain of 2 hours, there is no implementation of error handling of: a. input type check, b.command format check, c. output check
