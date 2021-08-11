class BuyNow():

    def __init__(self, context):
        self.context = context
        self.web = context.web

    def check_nuy_now_page(self):
        self.web.open(self.context.url)
        pattern = "//*[contains(text(),'Buy') or contains(text(),'BUY')]"
        buy_web_elements = self.web.finds_by_xpath(pattern)
        buy_now_dict = {}
        for ele in buy_web_elements:
            if(ele.tag_name == "button"):
                if("button" not in buy_now_dict):
                    buy_now_dict["button"] = [ele]
                    print("Dict: ", buy_now_dict)
                else:
                    button_list = buy_now_dict["button"]
                    button_list.append(ele)
                    buy_now_dict["button"] = button_list
            if(ele.tag_name == "input"):
                if("input" not in buy_now_dict):
                    buy_now_dict["input"] = [ele]
                else:
                    input_list = buy_now_dict["input"]
                    input_list.append(ele)
                    buy_now_dict["input"] = input_list
            if(ele.tag_name == "a"):
                if("a" not in buy_now_dict):
                    buy_now_dict["a"] = [ele]
                else:
                    a_list = buy_now_dict["a"]
                    a_list.append(ele)
                    buy_now_dict["a"] = a_list
            if(ele.tag_name == "span"):
                if("span" not in buy_now_dict):
                    buy_now_dict["span"] = [ele]
                else:
                    span_list = buy_now_dict["span"]
                    span_list.append(ele)
                    buy_now_dict["span"] = span_list
        print("Elements dict: ", buy_now_dict)    

