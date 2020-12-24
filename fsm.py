from transitions.extensions import GraphMachine

from utils import send_text_message

from relative import relative_name,name_info

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
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

    def is_going_to_claim(self, event):
        text = event.message.text
        return text.lower() == "自稱"

    def on_enter_honor(self, event):
        print("I'm entering honor")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger honor")
        self.go_back()

    def on_exit_honor(self):
        print("Leaving honor")

    def on_enter_claim(self, event):
        print("I'm entering claim")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger claim")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving claim")
