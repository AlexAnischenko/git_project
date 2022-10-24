class Model:
    def __init__(self, model):
        self.model = model

    def fit(self, X_train, y_train):
        self.model.fit(X_train, y_train)
