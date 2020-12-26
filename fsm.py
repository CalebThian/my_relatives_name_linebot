from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message,send_image_message

from relative import relative_name,honor_list_exist,honor_list_info,honor_info

from linebot.models import MessageTemplateAction

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_user(self,event):
        text = event.message.text
        return text.lower() == "結束"
    
    def on_enter_user(self,event=0):
        if event == 0:
            return
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入“請告訴我”來確認如何稱呼親戚！\n輸入“尊稱”來瞭解尊稱！\n隨時輸入“結束”來重新開始！")
        
    def is_going_to_fsm(self,event):
        text = event.message.text
        return text.lower() == "fsm"
    
    def on_enter_fsm(self,event):
        reply_token = event.reply_token
        url = "https://e3fc8d90a333.ngrok.io/show-img"
        send_image_message(reply_token, url)
        self.go_back()
    
    def is_going_to_question(self, event):
        text = event.message.text
        return text.lower() == "請告訴我"
    
    def on_enter_question(self, event):
        print("I'm entering question")

        reply_token = event.reply_token
        send_text_message(reply_token, "請問你想問誰的誰呢？（例如：爸爸的媽媽、姐姐的丈夫的妹妹等)")
        
    def is_going_to_qing(self, event):
        text = event.message.text
        return text[2]=="的"
    
    def on_enter_qing(self, event):
        print("I'm entering qing")

        reply_token = event.reply_token
        send_text_message(reply_token, relative_name(event.message.text))
        #self.go_back()
    
    def is_going_to_honor(self, event):
        text = event.message.text
        return text.lower() == "尊稱"
    
    def is_going_back_to_honor(self, event):
        text = event.message.text
        return text.lower() == "回上一層"
    
    def is_going_to_claim(self, event):
        text = event.message.text
        return text.lower() == "自稱"

    def on_enter_honor(self, event):
        print("I'm entering honor")

        reply_token = event.reply_token
        title = '尊稱科普'
        text = '請選擇欲查看對象及其親戚關係的稱呼'
        btn = [
            MessageTemplateAction(
                label = '長輩',
                text = '長輩'
            ),
            MessageTemplateAction(
                label = '同輩',
                text = '同輩'
            ),
            MessageTemplateAction(
                label = '晚輩',
                text = '晚輩'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
        
    def is_going_to_honor_e(self, event):
        text = event.message.text
        return text.lower() == "長輩"

    def on_enter_honor_e(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--長輩'
        text = '請選擇欲查看對象及其親戚關係的稱呼'
        btn = [
            MessageTemplateAction(
                label = '祖輩',
                text = '祖輩'
            ),
            MessageTemplateAction(
                label = '父母',
                text = '父母'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
    
    def is_going_back_to_honor_e(self, event):
        text = event.message.text
        return text.lower() == "回上一層"
    
    def is_going_to_honor_g(self, event):
        text = event.message.text
        return text.lower() == "祖輩"

    def on_enter_honor_g(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--祖輩'
        text = '請點選下列選項，輸入列表提供的選項以科普該稱呼'
        btn = [
            MessageTemplateAction(
                label = '列表',
                text = '列表'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
        
    def is_going_to_honor_g_list(self, event):
        text = event.message.text
        return text.lower() == "列表" or honor_list_exist("祖輩",text)

    def on_enter_honor_g_list(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text.lower() == "列表":
            send_text_message(reply_token, honor_list_info("祖輩"))
        else:
            send_text_message(reply_token,honor_info("祖輩",text))
        self.go_back()
        
    def is_going_to_honor_pa(self, event):
        text = event.message.text
        return text.lower() == "父母"

    def on_enter_honor_pa(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--父母'
        text = '請選擇欲查看對象及其親戚關係的稱呼'
        btn = [
            MessageTemplateAction(
                label = '父母',
                text = '父母'
            ),
            MessageTemplateAction(
                label = '父母的親戚',
                text = '父母的親戚'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
    
    def is_going_back_to_honor_pa(self, event):
        text = event.message.text
        return text.lower() == "回上一層"
       
    def is_going_to_honor_panr(self, event):
        text = event.message.text
        return text.lower() == "父母"

    def on_enter_honor_panr(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--父母'
        text = '請點選下列選項，輸入列表提供的選項以科普該稱呼'
        btn = [
            MessageTemplateAction(
                label = '列表',
                text = '列表'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
        
    def is_going_to_honor_panr_list(self, event):
        text = event.message.text
        return text.lower() == "列表" or honor_list_exist("父母",text)

    def on_enter_honor_panr_list(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text.lower() == "列表":
            send_text_message(reply_token, honor_list_info("父母"))
        else:
            send_text_message(reply_token,honor_info("父母",text))
        self.go_back()
        
    def is_going_to_honor_par(self, event):
        text = event.message.text
        return text.lower() == "父母的親戚"

    def on_enter_honor_par(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--父母的親戚'
        text = '請點選下列選項，輸入列表提供的選項以科普該稱呼'
        btn = [
            MessageTemplateAction(
                label = '列表',
                text = '列表'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
        
    def is_going_to_honor_par_list(self, event):
        text = event.message.text
        return text.lower() == "列表" or honor_list_exist("父母親戚",text)

    def on_enter_honor_par_list(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text.lower() == "列表":
            send_text_message(reply_token, honor_list_info("父母親戚"))
        else:
            send_text_message(reply_token,honor_info("父母親戚",text))
        self.go_back()
    
    def is_going_to_honor_pp(self, event):
        text = event.message.text
        return text.lower() == "同輩"

    def on_enter_honor_pp(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--同輩'
        text = '請選擇欲查看對象及其親戚關係的稱呼'
        btn = [
            MessageTemplateAction(
                label = '兄弟姊妹',
                text = '兄弟姊妹'
            ),
            MessageTemplateAction(
                label = '夫妻',
                text = '夫妻'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
    
    def is_going_back_to_honor_pp(self, event):
        text = event.message.text
        return text.lower() == "回上一層"
    
    def is_going_to_honor_s(self, event):
        text = event.message.text
        return text.lower() == "兄弟姊妹"

    def on_enter_honor_s(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--兄弟姊妹'
        text = '請選擇欲查看對象及其親戚關係的稱呼'
        btn = [
            MessageTemplateAction(
                label = '兄弟',
                text = '兄弟'
            ),
            MessageTemplateAction(
                label = '姊妹',
                text = '姊妹'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
    
    def is_going_back_to_honor_s(self, event):
        text = event.message.text
        return text.lower() == "回上一層"   
    
    def is_going_to_honor_bro(self, event):
        text = event.message.text
        return text.lower() == "兄弟"

    def on_enter_honor_bro(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--兄弟'
        text = '請點選下列選項，輸入列表提供的選項以科普該稱呼'
        btn = [
            MessageTemplateAction(
                label = '列表',
                text = '列表'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
    
    def is_going_to_honor_bro_list(self, event):
        text = event.message.text
        return text.lower() == "列表" or honor_list_exist("兄弟",text)

    def on_enter_honor_bro_list(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text.lower() == "列表":
            send_text_message(reply_token, honor_list_info("兄弟"))
        else:
            send_text_message(reply_token,honor_info("兄弟",text))
        self.go_back()
    
    def is_going_to_honor_sis(self, event):
        text = event.message.text
        return text.lower() == "姊妹"

    def on_enter_honor_sis(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--姊妹'
        text = '請點選下列選項，輸入列表提供的選項以科普該稱呼'
        btn = [
            MessageTemplateAction(
                label = '列表',
                text = '列表'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
    
    def is_going_to_honor_sis_list(self, event):
        text = event.message.text
        return text.lower() == "列表" or honor_list_exist("姊妹",text)

    def on_enter_honor_sis_list(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text.lower() == "列表":
            send_text_message(reply_token, honor_list_info("姊妹"))
        else:
            send_text_message(reply_token,honor_info("姊妹",text))
        self.go_back()
 
    def is_going_to_honor_mc(self, event):
        text = event.message.text
        return text.lower() == "夫妻"

    def on_enter_honor_mc(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--夫妻'
        text = '請選擇欲查看對象及其親戚關係的稱呼'
        btn = [
            MessageTemplateAction(
                label = '夫妻',
                text = '夫妻'
            ),
            MessageTemplateAction(
                label = '夫妻的親戚',
                text = '夫妻的親戚'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
    
    def is_going_back_to_honor_mc(self, event):
        text = event.message.text
        return text.lower() == "回上一層"   
    
    def is_going_to_honor_mcnr(self, event):
        text = event.message.text
        return text.lower() == "夫妻"

    def on_enter_honor_mcnr(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--夫妻'
        text = '請點選下列選項，輸入列表提供的選項以科普該稱呼'
        btn = [
            MessageTemplateAction(
                label = '列表',
                text = '列表'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
    
    def is_going_to_honor_mcnr_list(self, event):
        text = event.message.text
        return text.lower() == "列表" or honor_list_exist("夫妻",text)

    def on_enter_honor_mcnr_list(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text.lower() == "列表":
            send_text_message(reply_token, honor_list_info("夫妻"))
        else:
            send_text_message(reply_token,honor_info("夫妻",text))
        self.go_back()
    
    def is_going_to_honor_mcr(self, event):
        text = event.message.text
        return text.lower() == "夫妻的親戚"

    def on_enter_honor_mcr(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--夫妻的親戚'
        text = '請點選下列選項，輸入列表提供的選項以科普該稱呼'
        btn = [
            MessageTemplateAction(
                label = '列表',
                text = '列表'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
    
    def is_going_to_honor_mcr_list(self, event):
        text = event.message.text
        return text.lower() == "列表" or honor_list_exist("夫妻親戚",text)

    def on_enter_honor_mcr_list(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text.lower() == "列表":
            send_text_message(reply_token, honor_list_info("夫妻親戚"))
        else:
            send_text_message(reply_token,honor_info("夫妻親戚",text))
        self.go_back()
 
    def is_going_to_honor_ch(self, event):
        text = event.message.text
        return text.lower() == "晚輩"

    def on_enter_honor_ch(self, event):
        reply_token = event.reply_token
        title = '尊稱科普--晚輩'
        text = '請點選下列選項，輸入列表提供的選項以科普該稱呼'
        btn = [
            MessageTemplateAction(
                label = '列表',
                text = '列表'
            ),
            MessageTemplateAction(
                label = '回上一層',
                text = '回上一層'
            )
        ]
        url = 'https://www.itsfun.com.tw/cacheimg/ba/65/3a17c88fae81cf6dc7e4c7d6f8df.jpg'
        send_button_message(reply_token, title, text, btn, url)
    
    def is_going_to_honor_ch_list(self, event):
        text = event.message.text
        return text.lower() == "列表" or honor_list_exist("子女",text)

    def on_enter_honor_ch_list(self, event):
        text = event.message.text
        reply_token = event.reply_token
        if text.lower() == "列表":
            send_text_message(reply_token, honor_list_info("子女"))
        else:
            send_text_message(reply_token,honor_info("子女",text))
        self.go_back()
 
    def on_enter_claim(self, event):
        print("I'm entering claim")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger claim")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving claim")
