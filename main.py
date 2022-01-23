"""
Name(s): Skye Papa, Emma Kwa
Name of Project: A Most Peculiar Morning
"""

"""
One quick thing! Emma and I initially made this repl on a different file, not knowing that we had to import the thingy from Github, so it may look like this was all done in one day--it was not. I'm copy-pasting all of our initial code below.
"""

import time
import random

def cardeath():
  lastwords = input("\nYou begin to run out fo school and far, far away from your problems. \"They can't catch me out here,\" You think to yourself. If you keep running, you'll be right back home--you just have to cross this last road and you'll be back home. You take a step into the street and a blaring \"HONK\" screams in your ear. A thud hits you and you flip over. A crack in your spine echos in your ear as you take your last breath. As you realize the end is near, you think what you want your last words to be. Any last words? ")
  print("\nTHE END. YOU GOT THE DEATH ENDING. You were tragically hit by a car while trying to cross the street. \n \nYour tombstone reads as follows:\n \n" + firstname, lastname)
  print(lastwords)

def fourthwall():
  print("\nAs you leave school you realize your fellow classmates and teacher are calling out your name. Desperate not to get an incomplete homework assignment, you continue running. \n \nAdrenaline pumps through your entire body and it’s only when you stop running and start to walk that you realize your bag and phone are still in the 1st period classroom. Despite the fear that suddenly takes over your mind, you don’t turn back.\n \nOnce you get home you sit down and fall asleep almost instantly succumbing to the exhaustion. \n \nYou have the weirdest dream. You keep reliving this day of your life, and it feels as if someone is controlling your every move. You keep waking up late but sometimes you leave right away rather than resting. Sometimes you stay in class and are embarrassed. Different realities of today flash through your mind, but it can’t be real right? No, no, it’s just a silly dream. \n \nTHE END. YOU GOT THE 4th WALL ENDING.")

def runaway():
  survive = random.randint(1,5)
  if survive == 3:
    cardeath()
  else:
    fourthwall()

def hwinc():
  print("\nYour teacher takes homework out of hands. He reads over your assignment, looking rather pleased until he sees the final question. He then asks you loudly, \"Why isn't your homework done", firstname + "?\" \n \nHow embarassing! The whole class now knows your secret, and that you turned in your assignment late. You've had a very bad start to your day. \n \nYour day continues on this trend of bad luck. At lunch you discover that you forgot your wallet at home in your rush to get to class, and are forced to eat school lunch while your friends go out for lunch without you. You stumble through all of your classes, having a rough time doing all of your work--still flustered after that dreadful first period.\n \nBy the time you get home, you're so exhausted that you sink into your bed as soon as you walk through the door. You think to yourself: \"At least its Friday.\" \n \n THE END. YOU GOT THE \"BAD DAY\" ENDING.")

def hwdone():
  print("\nYou managed to finish your homework just in time! Your teacher looks at you with an expression of approval as he flips your paper to see each question is answered in a complete and neat fashion. A wave of relif hits you as you let out a deep breath. That was a close call. \n \nYour day isn't too bad after that. You go out to lunch with your friends and tell them all about your morning. You have a couple of good laughs and get back to class in the knick of time. All goes well, and when you get home you find yourself ready to enjoy what will undoubtedly be a relaxing weekend. \n \nTHE END. YOU GOT THE \"GOOD DAY\" ENDING.")

def lateclass():
  print("\nYou rested at home too long! you find yourself having to rush to school! You ran the mile to school, but youre too late-- you've missed the morning bell and are late to class. \n \nYou barge into class disheveled. Your classmates look at you with judging glares. You think to yourself: \"I should've just left home early.\" \n \nYou see that your teacher is checking homework from each of your classmates. You frantically open your backpack to reach for your assignment, but as you pull it out you have a shocking realization: your homework is incomplete. The very last question is unanswered. Because you got to class late, you know you have no chance of finishing your assignment before your teacher gets to you. You begin to become overwhelmed with embarassment, as you know that your teache is going to see your incomplete assignment if you turn it in. \n \nThat's when it hits you: you could run away. \n \nYou dont want to embarass yourself with this incomplete assignment, but if you stay in class you'll have no other option. Leaving class means you dont need to turn in anything anymore! A foolproof plan.\n")
  staygo = input("Do you stay in class and turn in your incomplete assignment (S), or do you run out of school and make new plans for they day (R)? ")
  if staygo in ["s", "S", "stay"]:
    print("You realize that running away is a bad idea and decide to sit down in class and accept your fate.\n")
    hwinc()
  elif staygo in ["r", "R", "run away"]:
    runaway()
  else:
    print("Hmm... that wasnt an option.\n \n")
    time.sleep(2)
    lateclass()

def ontimeclass():
  print("\nYou walk a mile to school and make it to class just in time-- the bell ringing as soon as you sit down. \n \nYour teacher then starts the class. He goes around asking each of the students in class to show him their homework, which was due at the start of class. You panic-- remembering you hand't finished the final question on the worksheet!\n \n You think to yourself: \"Chances are, I can scribble out an answer to this last question before he gets to my desk.\" The teacher has already started to collect assignments. You're running out of time!\n \n You can take a chance and do the last question of your homework, which risks you getting caught doing your work in class, or you can turn in your unfinished assignment.\n")
  homework = input("Do you finish your homework in class (F), or do you turn in what you have (T)? ")
  if homework in ["f", "F", "finish"]:
    caught = random.randint(0,1)
    if caught == 0:
      print("\nYour teacher saw you completing your homework in class and walked over to your desk! He grabs the incomplete assignment from your hands and you are embarassed in front of the entire class.\n")
      hwinc()
    else:
      hwdone()
  elif homework in ["t", "T", "turn in"]:
    hwinc()
  else:
    print("Hmm... that wasnt an option.\n \n")
    time.sleep(2)
    ontimeclass()  

def leave():
  print("\nYou decide its probably not worth it to risk being late and head out of your house straight away. \n")
  ontimeclass()

def relax():
  tardy = random.randint(0,1)
  if tardy == 0:
    lateclass()
  else:
    print("Your rest at home has been satisfactory and you manage to walk to school without a care in the world. You think to yourself: I can't believe I got ready so quickly! \n")
    ontimeclass()

def sleepin():
  print("\nYou wake up feeling well rested. \n \nYou don't have school this morning, do you? No. You couldn't. It's 7:35. Your alarm is supposed to go off at 7:00. You'd have school in 30 minutes then, and 15 of those 30 minutes would be spent walking to school. But lucky for you, you don't have school- it's Friday. \n \nWait- it's Friday? You have school! \n \nYou have 15 minutes to get showered, dressed, fed, and ready for school. \n \nYou rush to the bathroom to shower, moving faster than you have in your entire life. You shower in 8 minutes, get dressed in 3, and find a granola bar to eat on your way to school. \n \nYou have 4 extra minutes to spare before you have to get out of your house. You can leave now, taking no risks about getting to school on time, or you can relax for the next 4 minutes and boost your confidence. \n")
  intro = input("Do you leave now (N), or do you relax a bit (R)? ")
  print()
  if intro in ["n", "N", "leave", "leave now"]:
    leave()
  elif intro in ["r", "R", "relax"]:
    relax()
  else:
    print("Hmm... that wasnt an option.\n \n")
    time.sleep(2)
    sleepin()

def wakeup():
  print("You check your clock It's 6:15 AM, 45 minutes before your alarm is supposed to go off, but you dont care.\n \nYou take this extra time to get ready for school today, as you realize that it's a Friday. You take a nice, warm shower and make a fruit and yogurt parfait to eat for breakfast. You clean your room, put on your favorite shirt, and are filled with a sense of inner peace--feeling that you can finally move at yout own pace in the morning for once.\n")
  pinch = input("This day feels too good to be true. A little TOO good to be true.\n \nYou wonder: \"Is this really happening?\" \n \nThis feels crazy. Unreal. You wonder if you should pinch yourself to see if you're really awake at all, but at the same time, you dont want this dream to end.\n \nDo you pinch yourself and risk getting woken up out of your dream (P), or do you go with the flow and accept your strangely good start to a day (G)? ")
  if pinch in ["p", "P", "pinch"]:
    dream = random.randint(0,1)
    if dream == 0:
      print("\nYou pinch yourself, but you feel no pain. Weird.\n \nAll of a sudden, you feel yourself beginning to drift out of reality. Oh no, you were totally dreaming. You bid your fantasy reality goodbye as you begin to regain a true conciousness.\n")
      sleepin()
    else:
      print("\nOuch, that pinch hurt. Nothing happened either.\n \nHuh, I guess this day is really happening.")
      ontimeclass ()
  elif pinch in ["g", "G", "go with the flow"]:
    print("\nNope! You are not pinching yourself today, and you decide to accept your good reality that you are currently living in.")
    ontimeclass ()
  else:
    print("Hmm... that wasnt an option.\n \n")
    time.sleep(2)
    wakeup()

def start():
  sleep = input("\nYou feel a faint ringing in your left ear, and although you try to ignore it--it wakes you up. \n \nIt's still dark out, but its winter--so who knows what time it is. Although you try to fall back asleep, nothing is working. You find that it may be in your best interest to just start your day now, as you feel that there is no hope in falling back asleep. \n \nJust as you get ready to start your morning, the ringing dissapears. \"I can sleep again!\" you think to yourself. But then, you remember that you can still get up and start your morning. \n \nDo you decide to sleep in and get some extra rest (S) or get up now and start your day (G)? ")
  if sleep in ["s", "S", "sleep", "sleep in"]:
    sleepin()
  elif sleep in ["g", "G", "get up", "get up now"]:
    wakeup()
  else:
    print("Hmm... that wasnt an option.\n \n")
    time.sleep(2)
    start()

firstname = input("What is your first name: ")
lastname = input("What is your last name: ")

start()