class Tranformer:
    def __init__(self, percent, imp_estimator=None):
        self.percent = percent
        if imp_estimator is None:
            self.imputer_estimator = RandomForestRegressor(
            max_depth=10,
            max_features='sqrt',
            min_impurity_decrease=1e-5,
            n_jobs=4,
            random_state=17
          )
        else:
            self.imputer_estimator = imp_estimator

      def transform(self, X):
        X = X[:, :self.bound]
        X = self.imputer.transform(X)
        X = self.scaler.transform(X)
        X = X[:, self.mask]
        return X
