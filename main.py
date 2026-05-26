"""
Battle with Jarvis
-------------------
Author: Pratiksha Mishra                               
GitHub: https://github.com/thepratikshamishra

Description:    
    A fun and interactive console-based Python game where the player
    competes against Jarvis (an AI opponent) in the classic
    Rock, Paper, Scissors challenge. Jarvis responds with witty,     
    emoji-filled messages, making each round engaging.                                    

Features:
    - Play Rock, Paper, Scissors with AI
    - Score tracking for both player and Jarvis
    - Fun, personality-rich responses
    - Option to quit anytime with final score display
"""
import random
def play_game():
  print("🤖 I’m Jarvis, your witty AI opponent. Think you can beat me? Let’s find out! 🚀")

  your_score=0
  Jarvis_score=0

  while True:
    Jarvis=random.choice(["stone","paper","scissor"])
    you=input("🤖 Jarvis: Your move, human! 🪨 Stone, 📄 Paper, or ✂️ Scissor? (type 'quit' to end): ").lower()

    if (you=="stone" or you=="paper" or you== "scissor"):
     print("🤖 Jarvis's choice is :", Jarvis)

    if you == "quit":
     print("🤖 Jarvis: Mission terminated. Until next time, commander! 🚀")
     break

    if (Jarvis==you):
      print("🤖 Jarvis: A tie? Impressive... but I expected no less from you.")

    elif (Jarvis=="stone" and you=="paper"):
      print("✅ Jarvis: Well played, human. I didn't see that coming.") 
      your_score+=1

    elif (Jarvis=="stone" and you=="scissor"):
       print("❌ Jarvis: Oh, that was too easy… try harder, human!") 
       Jarvis_score+=1

    elif (Jarvis=="paper" and you=="stone"):
       print("❌ Jarvis: Oh, that was too easy… try harder, human!")
       Jarvis_score+=1

    elif (Jarvis=="paper" and you=="scissor"): 
       print("✅ Jarvis: Well played, human. I didn't see that coming.")
       your_score+=1

    elif (Jarvis=="scissor" and you=="stone"):
       print("✅ Jarvis: Well played, human. I didn't see that coming.")
       your_score+=1
 
    elif (Jarvis=="scissor" and you=="paper"):
       print("❌ Jarvis: Oh, that was too easy… try harder, human!") 
       Jarvis_score+=1
    
    else:
     print("🤖 Jarvis: Uhh... that's not stone, paper, or scissor. Try again, genius. 😏") 

  print("YourScore=", your_score, "JarvisScore=", Jarvis_score)
 
  if (your_score>Jarvis_score):
   print("🏆 Jarvis: You’ve bested me, human. I bow to your superiority... for now. 🤖")
  elif(your_score==Jarvis_score):
   print("🤝 Jarvis: A perfect tie! Looks like we’re equally matched this time.")
  else:
   print("😎 Jarvis: Victory is mine! Better luck next time, human.")
     
play_game()     
