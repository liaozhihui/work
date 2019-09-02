from rasa_core.actions import Action
class ActionSearchConsume(Action):
    def name(self):
        return 'action_search_consume'

    def run(self, dispatcher, tracker, domain):
        item = tracker.get_slot("item")
        item = extract_item(item)
        if item is None:
            dispatcher.utter_message("您好，我现在只会查话费和流量")
            dispatcher.utter_message("你可以这样问我：“帮我查话费”")
            return []

        time = tracker.get_slot("time")
        if time is None:
            dispatcher.utter_message("您想查询哪个月的消费？")
            return []
        # query database here using item and time as key. but you may normalize time format first.
        dispatcher.utter_message("好，请稍等")
        if item == "流量":
            dispatcher.utter_message("您好，您{}共使用{}二百八十兆，剩余三十兆。".format(time, item))
        else:
            dispatcher.utter_message("您好，您{}共消费二十八元。".format(time))
        return []