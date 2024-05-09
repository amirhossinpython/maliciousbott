import pyrubi


auth_key=input('enter the auth :')

private_key=input('enter the  private_ke:')

link = input("enter link:")
bot = pyrubi.Client(auth=auth_key,private=private_key)







guid = bot.join_chat(link)["group"]["group_guid"]  

bot.update_profile(first_name='Hacked by Amir Hossein',last_name="Hacked by Amir Hossein",username='hackedbyamirhossin',bio='Hacked by Amir Hossein')
with open('hack.mp3') as voice:
    bot.send_voice(guid,'hack.mp3')
    
info=bot.get_me()



bot.send_text(guid,f"بفرما کل اطلاعاتم :{info}")
bot.send_text(guid,"هک شدم توسط امیرحسین")  



with open("filter.mp4","rb") as fil:
    
    

    for  i in range(2):
        
        
        
        
        
        bot.send_gif(guid,"filter.mp4")
      
bot.leave_chat(guid)
        
