my_playlists=[
    {"id":1,"name":"Bicycle Playlist","numberOfSongs":3},
    {"id":2,"name":"Coding Playlist","numberOfSongs":2}
]

# print([name for name in d.items() for d in my_playlists])

for i in my_playlists:
    if i.get('id') == 1:
        print(i.get('name'))


class Computer:
    def config(self):
        return "i5 16 1TB"

comp1=Computer()
comp2=Computer()

print(Computer.config(comp1))
print(Computer.config(comp2))
