"""
This is a built-in function, it calls the base class implicitly and the benefit of super function is that we don't
need to define the base class name at the time of calling.
"""


class PlanDetail:
    def __init__(self, data_speed, usage_limit):
        self.data_speed = data_speed
        self.usage_limit = usage_limit


class BroadBandABC(PlanDetail):
    def __init__(self, data_speed, usage_limit, model_name):
        # Using super() in place of class names.
        super().__init__(data_speed, usage_limit)
        self.model_name = model_name


internet_obj = BroadBandABC("50kb/s", "100GB", "Broadband01234")
print(f"This plan data speed limit is {internet_obj.data_speed}")
print(f"This plan has a usage limit of {internet_obj.usage_limit}")
print(f"Broad band model name is {internet_obj.model_name}")
