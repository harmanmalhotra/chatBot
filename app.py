import telebot
from telebot import types
import pandas as pd


while True:
    try:
        # Create a Telegram bot object with your bot token
        bot = telebot.TeleBot('6273259656:AAFqN7nOhjpFyczUhYvZjTSlsqtikF91goA')
        
        
        def check_message(message,ex):
        
            if (message.json['text'] == 'MOMS'):
                momo_type (message)
            if (message.json['text'] == 'shake'):
                shakes_category (message)
            if (message.json['text'] == 'Ice Tea'):
                ice_tea_category (message)
            if (message.json['text'] == 'Lemonade'):
                lemonades_category (message)
        
            if message.json['text'] in ['veg','chicken','panner','aww_special']:
                momo_category (message)
        
            if message.json['text'] in ['steam','gravy','afgani','fried']:
                momo_quantity (message)
        
            if message.json['text'] in ['Raspberry','rajbhog','black_current','coconut_cream','strawberry','banana','butterscotch','pinacolda','charcoal','oreo','kitkat','classic_lemon','lemon_ginger','cola','strawberry','orange','salty_lime','sweet_salty','masala_soda']:
                drink_quantity (message)
        
        # MG Road Menu
            if message.json['text'] in ['Burger']:
                burger_type (message)
        
            if message.json['text'] in ['Sandwich']:
                sandwich_type (message)
        
            if message.json['text'] in ['Thick Shake']:
                Thik_shake_type (message)
        
            if message.json['text'] in ['Fries']:
                fries_type (message)
        
            if message.json['text'] in ['Mocktails']:
                print("mocktail recieved")
                Mocktail_type (message)
        
            if message.json['text'] in ['Chocolate Shake']:
                chocolate_shake_type (message)
        
            if message.json['text'] in ['Special Flavour Shake']:
                special_shake_type (message)
        
            if message.json['text'] in ['Cold coffe']:
                cold_coffe_type (message)
        
            if message.json['text'] in ['Refresh Ice Tea']:
                ice_tea_type (message)
        
        
            if message.json['text'] in ['classic veg','veggi fusion','cheesy blast','crunchy munchy','pizza burger','cheese chicken','chicken pizza','lucknow e']:
                cheese_type (message)
        
            if message.json['text'] in ['Shakes']:
                SHAKES_type (message)
        
        
            if message.json['text'] in ['COCONUT CREAM','BLACK CURRENT','STRAWBERRY','BUTTERSCOTCH','MIXED FRUIT','MANGO','BANANA','BELGIAN CHOCOLATE','ENGLISH COFFEE','BROWNIE SHAKE','HAZELNUT','KITKAT','FERRERO ROCHER','OREO','PINACOLADA','BLUEBERRY','BUBBLE GUM','RASPBERRY','CHARCOAL','PINK GUAVA','GREEN APPLE']:
                Ice_Cream_type (message)
        
        
        
            if message.json['text'] in ['Blue Lagoon','Cindrella','Virgin Mojito','veggie delight','panner tikka','veg mexican','chicken sandwich','aaloo patty','club desi','CAPPUCCINO','MOCHA','IRISH COFFEE','FRAPPUCCINO','CARAMEL COLD COFFEE','CLASSIC COLD COFFEE','PEACH ICED TEA','ORANGE ICED TEA','CLASSIC LEMON ICED TEA','COLA ICED TEA','STRAWBERRY ICED TEA',]:
                    dictd = {}
                    dk = pd.read_excel(ex)
                    dictd["text"] = "MgRoad"
                    df = pd.DataFrame([dictd])
                    df.to_excel(ex)
                    order(message,str(dk['text'].iloc[0]))
        
        
            if message.json['text'] in ['half','full']:
                    dictd = {}
                    dk = pd.read_excel(ex)
                    dictd["text"] = "Sector56"
                    df = pd.DataFrame([dictd])
                    df.to_excel(ex)
                    order(message,str(dk['text'].iloc[0]))
        
            if message.json['text'] in ['Regular','Large']:
                    dictd = {}
                    dk = pd.read_excel(ex)
                    dictd["text"] = "Sector56"
                    df = pd.DataFrame([dictd])
                    df.to_excel(ex)
                    order(message,str(dk['text'].iloc[0]))
        
            if message.json['text'] in ['Without Ice Cream','Ice Cream']:
                    dictd = {}
                    dk = pd.read_excel(ex)
                    dictd["text"] = "MgRoad"
                    df = pd.DataFrame([dictd])
                    df.to_excel(ex)
                    order(message,str(dk['text'].iloc[0]))
        
            if message.json['text'] in ['Normal','Extra cheese']:
                    dictd = {}
                    dk = pd.read_excel(ex)
                    dictd["text"] = "MgRoad"
                    df = pd.DataFrame([dictd])
                    df.to_excel(ex)
                    order(message,str(dk['text'].iloc[0]))
        
        
        
        #check user
        
        def check_user(message):
            uid = message.json['from']['id']
            ex = "temp"+str(uid)+".xlsx"
            dictd = {}
        
            if (message.json['text'] == 'start_day'):
                dictd["text"] = "Sector56"
                df = pd.DataFrame([dictd])
                df.to_excel(ex)
                shop_name(message)
        
            if (message.json['text'] == 'Sector56'):
                dictd = {}
                dk = pd.read_excel(ex)
                dictd["text"] = "Sector56"
                df = pd.DataFrame([dictd])
                df.to_excel(ex)
                menu_sector_56(message)
        
            if message.json['text'] in ['Menu_56']:
                dictd = {}
                dk = pd.read_excel(ex)
                dictd["text"] = "Sector56"
                df = pd.DataFrame([dictd])
                df.to_excel(ex)
                menu_sector_56 (message)
        
            if message.json['text'] in ['Menu_Mg_road']:
                dictd = {}
                dk = pd.read_excel(ex)
                dictd["text"] = "Mg_Road"
                df = pd.DataFrame([dictd])
                df.to_excel(ex)
                menu_mg_road (message)
            if message.json['text'] in ['MgRoad']:
                dictd = {}
                dk = pd.read_excel(ex)
                dictd["text"] = "Mg_Road"
                df = pd.DataFrame([dictd])
                df.to_excel(ex)
                menu_mg_road (message)
        
            else:
                dk = pd.read_excel(ex)
                dictd["text"] = str(dk['text'].iloc[0]) + "-" + message.json['text']
                df = pd.DataFrame([dictd])
                df.to_excel(ex)
                check_message(message,ex)
        
        
        #Send Reply
        def keyborad_update(message,row_w,num_button,list_button,text):
            keyboard = types.ReplyKeyboardMarkup(row_width=row_w)
            button = num_button
            i=0
            try:
                while True:
                    if button == 1:
                        keyboard.add(types.KeyboardButton(list_button[i]))
                        break
        
                    if button == 2:
                        print(i)
                        keyboard.add(types.KeyboardButton(list_button[i]),types.KeyboardButton(list_button[i+1]))
                        break
        
                    if button >=3 :
                        keyboard.add(types.KeyboardButton(list_button[i]),types.KeyboardButton(list_button[i+1]),types.KeyboardButton(list_button[i+2]))
        
                    i = i+3
                    print(i)
                    button = button - 3
                    if button <= 0:
                        break
        
                bot.reply_to(message,text,reply_markup=keyboard)
        
            except:
                keyboard = types.ReplyKeyboardMarkup(row_width=1)
                button1 = types.KeyboardButton('start_day')
                keyboard.add(button1)
                bot.reply_to(message,text,reply_markup=keyboard)
        
        
        #Day Start
        def start_your_day(message):
            keyboard = types.ReplyKeyboardMarkup(row_width=1)
            button1 = types.KeyboardButton('start_day')
            keyboard.add(button1)
            bot.reply_to(message, 'start you day', reply_markup=keyboard)
        
        
        #Shop Name
        def shop_name(message):
            bot.reply_to(message, 'Select Shop', reply_markup=types.ReplyKeyboardRemove())
            keyboard = types.ReplyKeyboardMarkup(row_width=3)
            #button1 = types.KeyboardButton('Sector56')
            button2 = types.KeyboardButton('MgRoad')
            #keyboard.add(button1)
            keyboard.add(button2)
            bot.reply_to(message,"start your day" ,reply_markup=keyboard)
        
        
        
        #Menu
        
        
        #Shops Main_Menu
        def menu_sector_56 (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,5,['shake','MOMS','Ice Tea','Lemonade','Menu_56'],"Choose Menu")
        
        
        #MOMS
        def momo_category (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,5,['steam','gravy','afgani','fried','Menu_56'],"Choose category")
        
        
        def momo_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,5,['veg','chicken','panner','aww_special','Menu_56'],"Choose type")
        
        def momo_quantity (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,3,['half','full','Menu_56'],"Choose Quantity")
        
        #shops MAin Menu Mg Road
        def menu_mg_road (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,3,8,['Refresh Ice Tea','Cold coffe','Mocktails','Fries','Shakes','Sandwich','Burger','Menu_Mg_road'],"Choose Menu")
        
        #Mg Road
        
        def ice_tea_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,3,6,['PEACH ICED TEA','ORANGE ICED TEA','CLASSIC LEMON ICED TEA','COLA ICED TEA','STRAWBERRY ICED TEA','Menu_Mg_road'],"Choose type")
        
        def cold_coffe_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,3,7,['CAPPUCCINO','MOCHA','IRISH COFFEE','FRAPPUCCINO','CARAMEL COLD COFFEE','CLASSIC COLD COFFEE','Menu_Mg_road'],"Choose type")
        
        def special_shake_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,3,8,['PINACOLADA','BLUEBERRY','BUBBLE GUM','RASPBERRY','CHARCOAL','PINK GUAVA','GREEN APPLE','Menu_Mg_road'],"Choose type")
        
        def chocolate_shake_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,3,8,['BELGIAN CHOCOLATE','ENGLISH COFFEE','BROWNIE SHAKE','HAZELNUT','KITKAT','FERRERO ROCHER','OREO','Menu_Mg_road'],"Choose type")
        
        def Mocktail_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,4,['Blue Lagoon','Cindrella','Virgin Mojito','Menu_Mg_road'],"Choose type")
        
        def fries_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,4,['French Fries','Peri Peri','Cheesy Fries','Menu_Mg_road'],"Choose type")
        
        def Thik_shake_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,3,8,['COCONUT CREAM','BLACK CURRENT','STRAWBERRY','BUTTERSCOTCH','MIXED FRUIT','MANGO','BANANA','Menu_Mg_road'],"Choose type")
        
        def sandwich_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,3,7,['veggie delight','panner tikka','veg mexican','chicken sandwich','aaloo patty','club desi','Menu_Mg_road'],"Choose type")
        
        def burger_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,3,9,['classic veg','veggi fusion','cheesy blast','crunchy munchy','pizza burger','cheese chicken','chicken pizza','lucknow e','Menu_Mg_road'],"Choose type")
        
        def SHAKES_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,3,4,['Special Flavour Shake','Chocolate Shake','Thick Shake','Menu_Mg_road'],"Choose type")
        
        
        
        #cheese Type
        def cheese_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,3,['Normal','Extra cheese','Menu_Mg_road'],"Choose Cheese Quantity")
        
        
        #ice cream type
        def Ice_Cream_type (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,3,['Without Ice Cream','Ice Cream','Menu_Mg_road'],"Choose with or without ice cream")
        
        
        
        
        
        #Order
        def order(message,temp):
            dictd = {}
            bot.reply_to(message, 'Order Placed', reply_markup=types.ReplyKeyboardRemove())
            dk = pd.read_excel("check.xlsx")
            dk = dk[['date','user_id','event','order_detail']]
            dictd["date"] = message.json['date']
            dictd["user_id"] = message.json['from']['id']
            dictd["event"] = "Order Placed"
            dictd["order_detail"] = temp
        
            df = pd.DataFrame([dictd])
            dk = dk.append(df)
            dk.to_excel("check.xlsx")
            shop_name (message)
        
        
        #Shakes Sector 56
        def shakes_category (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,4,12,['Raspberry','rajbhog','black_current','coconut_cream','strawberry','banana','butterscotch','pinacolda','charcoal','oreo','kitkat','Menu_56'],"Choose category")
        
        
        #ICE Tea Sector 56
        def ice_tea_category (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,6,['classic_lemon','lemon_ginger','cola','strawberry','orange','Menu_56'],"Choose category")
        
        
        #lemonades Sector 56
        def lemonades_category (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,4,['salty_lime','sweet_salty','masala_soda','Menu_56'],"Choose category")
        
        
        
        
            #Combos Sector 56
        def combos_category (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,4,['momo_ice_tea','momo_shake'],"Choose category")
        
        
        
        
        #DrinkS Quantity
        def drink_quantity (message):
            bot.reply_to(message, 'Select Button', reply_markup=types.ReplyKeyboardRemove())
            keyborad_update(message,2,3,['Regular','Large','Menu_56'],"Choose Quantity")
        
        
        
        # Handle the '/start' command
        @bot.message_handler(commands=['start'])
        def handle_start(message):
            start_your_day(message)
        
        
        
        #@bot.message_handler(commands=['stop'])
        #def handle_stop(message):
         #   bot.send_message(message.chat.id, "Bot stopped.")
          #  bot.stop_polling()
        
        # Handle text messages
        @bot.message_handler(func=lambda message: True)
        def handle_text(message):
        
            check_user(message)
        
            print(message.json['text'])
        
            3#if (message.json['text'] == 'start_day'):
              #  shop_name(message)
        
            #if (message.json['text'] == 'Sector56'):
             #   menu_sector_56(message)
        
            #if (message.json['text'] == 'Thik shake'):
             #   button6= types.KeyboardButton('choco shake')
              #  button7 = types.KeyboardButton('Milk shake')
               # button8 = types.KeyboardButton('Button 7')
               # button9 = types.KeyboardButton('Button 8')
               # button10 = types.KeyboardButton('Main_Menu')
               # new_keyboard = types.ReplyKeyboardMarkup(row_width=2)
               # new_keyboard.add(button6, button7,button8,button9,button10)
               # bot.send_message(message.chat.id, "choose shakes", reply_markup=new_keyboard)
                #bot.stop_polling()
        
        
            ##if (message.json['text'] == 'MOMS'):
              ##  momo_type (message)
        
        
            ##if message.json['text'] in ['veg','chicken','panner','aww_special']:
              ##  momo_category (message)
        
        
            #if message.json['text'] in ['steam','gravy','afgani','fried']:
             #   momo_quantity (message)
        
        
            #if message.json['text'] in ['half','full']:
             #   order_sector_56(message)
        
        
        
            if(message.json['text'] == 'Main_Menu'):
                keyboard = types.ReplyKeyboardMarkup(row_width=3)
                button1 = types.KeyboardButton('Thik shake')
                button2 = types.KeyboardButton('MOMS')
                button3 = types.KeyboardButton('Menu_Mg_road')
                button5 = types.KeyboardButton('Refresh Ice Tea')
                button6= types.KeyboardButton('Burger')
                button7 = types.KeyboardButton('Sandwich')
                button8 = types.KeyboardButton('Mocktails')
                button9 = types.KeyboardButton('Cold coffe')
                button10 = types.KeyboardButton('Main_Menu')
                keyboard.add(button1, button2, button3,button5, button6, button7,button8,button9, button10)
                bot.reply_to(message, 'Hello! Please choose an option:', reply_markup=keyboard)
        
        
        
        # Start the bot
        while True:
            try:
                bot.polling()
            except Exception as e:
                print(f"An error occurred: {e}")
                # Delay for a certain period before retrying
    except Exception as e:
        print(f"An error occurred: {e}")
        # Delay for a certain period before retrying
