from abc import ABC, abstractmethod


class abstractWit(ABC):

    @staticmethod
    @abstractmethod
    def init():
        pass

    @staticmethod
    @abstractmethod
    def add(name):
        pass

    @staticmethod
    @abstractmethod
    def commit_m_message(message):
        pass

    @staticmethod
    @abstractmethod
    def log():
        pass

    @staticmethod
    @abstractmethod
    def status():
        pass

    @staticmethod
    @abstractmethod
    def checkout(commit_id):
        pass
