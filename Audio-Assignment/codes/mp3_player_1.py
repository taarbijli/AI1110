import random 
import pygame

pygame.mixer.init()

rand_array=random.sample(range(1,21),k=20)
file=[]
for i in rand_array:
    file.append(f"VF{rand_array[i-1]}.mp3")

for i in file:
    print("Song playing currently:",i)
    pygame.mixer.music.load(f"audio/{i}")
    pygame.mixer.music.play()
    
    x=input("Press n to change song")
    if x=='n':
        pygame.mixer.music.stop()
else:
    print("Hope you enjoyed the playlist!")

