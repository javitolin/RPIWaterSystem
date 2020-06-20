from typing import List

class RunConfigurations(object):
    def __init__(self, StartTime, DurationInSeconds, IsActive):
        self.StartTime = StartTime
        self.DurationInSeconds = DurationInSeconds
        self.IsActive = IsActive

    @classmethod
    def from_json(cls, data: dict):
        return cls(**data)

class Configuration(object):
    """description of class"""
    def __init__(self, IsActive, RunConfigurations: List[RunConfigurations]):
        self.IsActive = IsActive
        self.RunConfigurations = RunConfigurations
   
    @classmethod
    def from_json(cls, data: dict):
        configurations = list(map(RunConfigurations.from_json, data["RunConfiguration"]))
        return cls(data["IsActive"], configurations)

