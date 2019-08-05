# -*- coding:utf-8 -*-


class EVALSTAGE(object):
    INIT = 'INIT'
    EVALUATION = 'EVALUATION'
    FREE = 'FREE'


class EvalStageContext(object):
    def __init__(self, obj, prepare_stage, after_stage):
        self.obj = obj
        self.prepare_stage = prepare_stage
        self.after_stage = after_stage


class LazyFunction(object):
    def __init__(self, func, *args, **kwargs):
        self.__func = func
        self.__func_args = args
        self.__func_kwargs = kwargs
        self.__func_res = None
        self.__evaluation = False
        print(self.__evaluation)

    def __eval_func(self):
        self.__func_res = self.__func(*self.__func_args, **self.__func_kwargs)
        self.__evaluation = True

    def __getattribute__(self, item):

        if item.startswith('_LazyFunction'):
            return object.__getattribute__(self, item)
        if object.__getattribute__(self, '_LazyFunction__evaluation') is False:
            self.__eval_func()
        return object.__getattribute__(self.__func_res, item)


    # def __getattr__(self, item):
    #     '''
    #     查找属性时，首先隐式调用 __getattribute__ 查找属性是否是 lazyfunction 本身特有的，如果找到，就直接返回
    #     如果没有找到，就调用 __getatt__。
    #     '''
    #     # if self.__override is True:
    #     #     return self.__dict__[item]
    #     # self.__eval_func()
    #     # return self.__func_res.__getattribute__(item)
    #     # return 'hello'
    #     self.__record = self.__eval_func()
    #     return self.__dict__[item]

    # def __setattr__(self, key, value):
    #     self.__dict__[key] = value
        # self[key] = value



lf = LazyFunction(print, 'dd')
print(getattr(lf, 'dd'))
