import pyrubi


auth_key='auth_key'
private_key='private_key'

bot = pyrubi.Client(auth=auth_key,private=private_key)




link = input("enter link:")


guid = bot.join_chat(link)["group"]["group_guid"]  

bot.update_profile(first_name='Hacked by Amir Hossein',last_name="Hacked by Amir Hossein",username='hackedbyamirhossin',bio='Hacked by Amir Hossein')

bot.send_text(guid,"هک شدم توسط امیرحسین")  

print(guid)

with open("filter.mp4","rb") as fil:
    
    

    for  i in range(2):
        
        
        
        
        bot.send_gif(guid,"filter.mp4")
      
bot.leave_chat(guid)
