from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message,send_image_message

from relative import relative_name,honor_list_exist,honor_list_info,honor_info,list_info

from db import *

from linebot.models import MessageTemplateAction

col_use = ""
key=""
upcol=""
upkey=""
information = ""
name = ""
rel = ""

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
        send_text_message(reply_token, "輸入“請告訴我”來確認如何稱呼親戚！\n輸入“尊稱”來瞭解尊稱！\n輸入“登記”來記錄親戚的名字與稱呼!\n輸入`fsm`來查看狀態圖！!\n隨時輸入“結束”來重新開始！")
        
    def is_going_to_fsm(self,event):
        text = event.message.text
        return text.lower() == "fsm"
    
    def on_enter_fsm(self,event):
        reply_token = event.reply_token
        url = "https://i.imgur.com/1zgGqaR.jpg"
        send_image_message(reply_token, url)
        self.go_back()
        
    def is_going_to_log(self,event):
        text = event.message.text
        return text.lower() == "登記"
    
    def on_enter_log(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, information+log_message())
        
    def is_going_to_log_name(self,event):
        text = event.message.text
        return text.lower() == "存入"
    
    def on_enter_log_name(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入親戚姓名與稱呼：\n（按___<空格>___格式輸入，如：“王小明 哥哥”）")
    
    def is_going_to_log_ins_pro(self,event):
        text = event.message.text       
        return len(text)<= 100 and text.find(" ")!=-1
    
    def on_enter_log_ins_pro(self,event):
        info = event.message.text
        info = info.split()
        name = info[0]
        rel = info[1]
        reply_token = event.reply_token
        insert(event.source.user_id,name,rel)
        information = "成功登錄資訊:("+ name +","+ rel + ")\n\n"
        send_text_message(reply_token, information+log_message())
        self.go_back()
        
    def is_going_to_log_select(self,event):
        text = event.message.text
        return text.lower() == "查詢"
    
    def on_enter_log_select(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請問您是要按照親戚名字或稱呼來查詢？請輸入“名字”或“稱呼”。\n若是想查看全部資料請輸入“全部”")
        
    def is_going_to_log_sel(self,event):
        text = event.message.text
        return text=="名字" or text == "稱呼"
    
    def on_enter_log_sel(self,event):
        global col_use
        col_use = event.message.text
        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入欲查詢的名字/稱呼：")
        
    def is_going_to_log_sel_pro(self,event):
        text = event.message.text
        return len(text)<=50
    
    
    def on_enter_log_sel_pro(self,event):
        global col_use,key
        key = event.message.text
        print("Enter sel_pro"+col_use+" "+key+"\n")
        reply_token = event.reply_token
        send_text_message(reply_token, select(event.source.user_id,col_use,key)+"\n\n"+log_message())
        col_use = ""
        key = ""
        self.go_back()
        
    def is_going_to_log_sel_all_pro(self,event):
        text = event.message.text
        return text.lower()=="全部"
    
    def on_enter_log_sel_all_pro(self,event):
        key = event.message.text
        reply_token = event.reply_token
        send_text_message(reply_token,select(event.source.user_id,"",key)+"\n\n"+log_message())
        key = ""
        self.go_back()
    
    def is_going_to_log_update(self,event):
        text = event.message.text
        return text.lower() == "更新"
    
    def on_enter_log_update(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請問您是要按照親戚名字或稱呼來更新？請輸入“名字”或“稱呼”。")
    
    def is_going_to_log_upd(self,event):
        col_use = event.message.text
        return col_use=="名字" or col_use == "稱呼"
    
    def on_enter_log_upd(self,event):
        global col_use
        col_use = event.message.text
        reply_token = event.reply_token       
        send_text_message(reply_token, "請輸入欲更新資料的名字/稱呼：")
        
    def is_going_to_log_upd_col(self,event):
        text = event.message.text
        return len(text)<=50
    
    def on_enter_log_upd_col(self,event):
        global key
        key = event.message.text
        reply_token = event.reply_token
        send_text_message(reply_token, "請問您是要更新選定資料的名字或稱呼？請輸入“名字”或“稱呼”。")
    
    def is_going_to_log_upd_key(self,event):
        text = event.message.text
        return text == "名字" or text == "稱呼"
    
    def on_enter_log_upd_key(self,event):
        global upcol
        reply_token = event.reply_token
        upcol = event.message.text
        send_text_message(reply_token, "請輸入更新的内容：")
    
    def is_going_to_log_upd_pro(self,event):
        text = event.message.text
        return len(text)<=50
    
    def on_enter_log_upd_pro(self,event):
        global col_use,key,upcol
        upkey = event.message.text
        reply_token = event.reply_token
        information = update(event.source.user_id,col_use,key,upcol,upkey)+"\n"
        send_text_message(reply_token,information+"\n"+log_message())
        col_use=""
        key=""
        upcol=""
        self.go_back()
    
    def is_going_to_log_delete(self,event):
        text = event.message.text
        return text.lower() == "刪除"
    
    def on_enter_log_delete(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "請問您是要按照親戚名字或稱呼來刪除？請輸入“名字”或“稱呼”。\n若是想刪除全部資料請輸入“全部”")
        
    def is_going_to_log_del(self,event):
        text= event.message.text
        return text =="名字" or text == "稱呼"
    
    def on_enter_log_del(self,event):
        global col_use
        reply_token = event.reply_token
        col_use = event.message.text
        send_text_message(reply_token, "請輸入欲刪除的名字/稱呼：")
    
    def is_going_to_log_del_pro(self,event):
        text = event.message.text
        return len(text)<=50
    
    def on_enter_log_del_pro(self,event):
        global col_use
        key = event.message.text
        reply_token = event.reply_token
        send_text_message(reply_token,delete(event.source.user_id, col_use, key)+"\n"+log_message())
        col_use=""
        self.go_back()
    
    def is_going_to_log_del_all_pro(self,event):
        text = event.message.text
        return text.lower()=="全部"
    
    def on_enter_log_del_all_pro(self,event):
        reply_token = event.reply_token
        key = event.message.text
        send_text_message(reply_token,delete(event.source.user_id,"", key)+"\n"+log_message())
        self.go_back()
    
    def is_going_to_question(self, event):
        text = event.message.text
        return text.lower() == "請告訴我"
    
    def on_enter_question(self, event):
        print("I'm entering question")

        reply_token = event.reply_token
        send_text_message(reply_token, "請問你想問誰(限一等親内)的誰呢？（例如：父親的母親、妻子的哥哥等)\n若不清楚有哪些一等親，請輸入“一等親”來查詢！")
        
    def is_going_to_qing(self, event):
        text = event.message.text
        if len(text)>2:
            return text[2]=="的"
        return False
    
    def on_enter_qing(self, event):
        print("I'm entering qing")

        reply_token = event.reply_token
        send_text_message(reply_token, relative_name(event.message.text))
        #self.go_back()
        
    def is_going_to_qing_list(self, event):
        text = event.message.text
        return text=="一等親"
    
    def on_enter_qing_list(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token,list_info())
        self.go_back()
    
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
        url = 'https://i.imgur.com/sWrKlEi.png'
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
        url = 'https://i.imgur.com/WnfsDGT.png'
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
        url = 'https://i.imgur.com/oqoQymD.png'
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
        url = 'https://i.imgur.com/fGgL4T5.png'
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
        url = 'https://i.imgur.com/Pv0uC91.png'
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
        url = 'https://i.imgur.com/GjbxJxB.jpg'
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
        url = 'https://i.imgur.com/sdGS24A.png'
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
        url = 'https://i.imgur.com/nbXrIPO.png'
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
        url = 'https://i.imgur.com/rv6HoYj.png'
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
        url = 'https://i.imgur.com/NIN7eZh.png'
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
        url = 'https://i.imgur.com/sbpMlTF.png'
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
        url = 'https://i.imgur.com/ZxxAT9t.png'
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
        url = 'https://i.imgur.com/UVzUJga.png'
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
        url = 'https://i.imgur.com/TlJ34JH.png'
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
