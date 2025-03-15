import json
# from song import Song

# # Open and read the JSON file
# with open('song.json', 'r') as file:
#     data = json.load(file)
# print(data)

var1 = 'abcdefghi'
json_file = "Some/file/path"

# f = open("song.json","a")
# # print(f.read())
# f.write("{Now the file has more content!:p}")
# # f.close()
# #open and read the file after the appending:
# f = open("song.json", "r")
# print(f.read())




# with open('song.json', 'r+') as f:
#     json_data = json.load(f)
#     # print(json_data)
#     # for k in json_data['subjects']:
#     json_data[0]['lyrics'] = var1
#     f.seek(0)
    
#     f.write(json.dumps(json_data, indent=2))
#     f.truncate()

# def writeToFile():
#     lyrics = input( "enter lyrics: " )
#     artist = input("enter artist name: ")
#     songObj = Song(lyrics, artist)
#     print(vars(songObj))
#     data = []
#     with open('testWrite.json') as file:
#         data = json.load(file)
#         data.append(vars(songObj))
#         print(data)
#     with open('testWrite.json', 'w') as file:
#         json.dump(data, file) 

# ctr = "y"
# while (ctr=="y"):
#     writeToFile()
#     ctr = input("continue? y/n?")


with open('song.json', 'r') as file:
    data = json.load(file)

# key to remove
key_to_remove = "topics"
print(type(key_to_remove))
# checking if the key exists before removing
if key_to_remove in data:
    print(type(key_to_remove))
    removed_value = data.pop(key_to_remove)
    print(type(removed_value))
    # print("Removed key '{key_to_remove}' with value: {removed_value}")

# saving the updated JSON data back to the file
with open('song.json', 'w') as file:
    json.dump(data, file, indent=2)
