import keyboard
with open('LOG_text.txt') as f:
    count = (sum(1 for _ in f))

if (count >= 5):
    print (count)

if(keyboard._pressed_events('win')):
    print(count)
