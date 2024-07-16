#%%
name = "Akash"
print(name)
age = 17
print(age)
height = 1.75
print(height)
print(age + height)
print(age * height)
print(height/age)

intro = name + " " + str(age)
print(intro.upper)
print(intro.lower)
print(intro.title)
print(intro.swapcase)

hobbies = ["basketball", "gym", "reading"]
print(hobbies)

hobbies.append("coding")
hobbies.pop(0)
hobbies.reverse
hobbies.sort

#%%
profile = {
    "First": name,
    "Age": age,
    "Height": height,
    "Hobbies" : hobbies, 
}

profile['favorite_color'] = 'purple'
print(profile)
del profile['Height']
print(profile)
profile['Age'] +=1
print(profile)
 # %%
