from client import Client

print("*******************************************")
client = Client()
client.set("1","my")
client.get("1")
client.set(2,"my2")
print("get key str 2",client.get("2"))
print("get key int 2",client.get(2))
client.delete("1")
client.mset("3","my3","4","my4",5,876)
print("mget",client.mget("3","4",5,"100"))
client.set(5,888)
print("get key 5",client.get(5))
