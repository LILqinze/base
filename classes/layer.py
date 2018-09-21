class Layer:
    def __init__(self, model, **params):
        self._model = model
        self._params = params

    def __call__(self):
        return self._model.gen(**self._params)

    def __str__(self):
        return self.name

    @property
    def model(self):
        return self._model.gen

    @property
    def params(self):
        return self._params

    @property
    def name(self):
        return self._model.name
