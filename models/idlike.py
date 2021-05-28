class IdLike:
    def __init__(self, id, like):
        self.id = id
        self.like = like

    def __repr__(self):
        return f"Id: {self.id}, Like: {self.like}"