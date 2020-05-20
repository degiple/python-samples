
musician = ["higedan", "king gnu"]

geocord = (34.978702, 135.901755)

me = {
    "color": "Blue",
    "favorite_food": "Pork cutlet"
}

answer = input("me: ")
if answer in me:
    result = me[answer]
    print(result)

music = {
    "higedan": ["aa", "bb", "cc"],
    "king gnu": ["dd", "ee", "ff"]
}

myset1 = set([1, 2, 3])
myset2 = set([1, 2, 3, 3, 2, 1])
print(myset1)
print(myset2)
