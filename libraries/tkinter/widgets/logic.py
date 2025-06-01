class C_logic:
    @staticmethod
    def _sum(_one, _two):
        return _one + _two
    
    @staticmethod    
    def _substract(_one, _two):
        return _one - _two
    
    @staticmethod
    def _multiply(_one, _two):
        return _one * _two
    
    @staticmethod
    def _divide(_one, _two):
        if (_two == 0):
            return "Cant divide by zero"
        return _one / _two