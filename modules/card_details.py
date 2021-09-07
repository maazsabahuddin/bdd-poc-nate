class CardDetails:
    def __init__(self, context) -> None:
        self.context = context
        self.web = context.web
        self.is_card_details_found = False
        