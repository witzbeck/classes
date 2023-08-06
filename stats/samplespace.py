# Alex Beckwith
# Sample space generating classes

class SampleSpace(object):
    def one_iter(self, cur_list: list):      
        full_resp = []
        for resp in cur_list:
            resp_part = [resp + x for x in self.response_set]
            full_resp = full_resp + resp_part
        return full_resp

    def flip(self, n_flips: int):      
        cur_list = self.r_list_cur
        if n_flips < 2:
            return cur_list
        else:
            for i in range(n_flips - 1): #-1 cuz one flip should give response set
                cur_list = self.one_iter(cur_list)         
        self.r_list_cur = cur_list
        return cur_list

    def __init__(self, response_set: set):
        self.response_set = response_set
        self.r_list_init = list(response_set)
        self.r_list_cur = self.r_list_init
        self.r_len = len(response_set)
        self.r_range = range(self.r_len)              


class CoinSampleSpace(SampleSpace):
    def __init__(self, flips, response_set="th"):
        super().__init__(response_set)
        self.flip(flips)
        self.ss = self.r_list_cur


class DiceSampleSpace(SampleSpace):
    def __init__(self, flips, response_set="123456"):
        super().__init__(response_set)
        self.flip(flips)
        self.ss = self.r_list_cur
