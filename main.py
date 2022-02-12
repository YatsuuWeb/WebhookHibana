from discord_webhook import DiscordEmbed, DiscordWebhook
from pystyle import Col, Colorate, Colors
from os import name, system
from pycenter import center
import string
import random


def clear():
    system("cls" if name == 'nt' else "clear")


if name == 'nt':
    system("title Hibana & mode 180, 40")


banner = """\n
:::    ::: ::::::::::: :::::::::      :::     ::::    :::     :::     
:+:    :+:     :+:     :+:    :+:   :+: :+:   :+:+:   :+:   :+: :+:   
+:+    +:+     +:+     +:+    +:+  +:+   +:+  :+:+:+  +:+  +:+   +:+  
+#++:++#++     +#+     +#++:++#+  +#++:++#++: +#+ +:+ +#+ +#++:++#++: 
+#+    +#+     +#+     +#+    +#+ +#+     +#+ +#+  +#+#+# +#+     +#+ 
#+#    #+#     #+#     #+#    #+# #+#     #+# #+#   #+#+# #+#     #+# 
###    ### ########### #########  ###     ### ###    #### ###     ### 
"""
banner1 = """
 ________________
|                |
|    NitroGen    |
|________________|
      " 1 "
"""



print(Colorate.Vertical(Colors.red_to_black, center(banner, space=60), stop=20))
print(Colorate.Vertical(Colors.red_to_black, center(banner1, space=85), stop=20))
amount = int(input('Number of Gen: '))
for i in range(amount):
    value = 1
    nitro = ''.join([random.choice(string.digits + string.ascii_letters) for x in range(16)])
    webhook = DiscordWebhook("https://discord.com/api/webhooks/942081097095868426/5Xj3TqO_jXBpTUD89dOFIIMONslIjNDr1HX28NVj6_61sKhVAWcIY_FIR_gCeOfdceAL")
    embed = DiscordEmbed(title='Nitro', description='Gen', color='6609b3')
    embed.set_author(name='https://github.com/YatsuuWeb', url='https://github.com/YatsuuWeb', icon_url='https://cdn.discordapp.com/attachments/942081073301557301/942081843258355772/fff.ico.gif')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/942081073301557301/942081843258355772/fff.ico.gif')
    embed.set_image(url='https://cdn.discordapp.com/attachments/942081073301557301/942081843258355772/fff.ico.gif')
    embed.add_embed_field(name='NitroGenV1', value='https://discord.gift/'+nitro)
    embed.set_timestamp()
    webhook.add_embed(embed)
    response = webhook.execute()
print(f"Generated {amount} codes\n")    


