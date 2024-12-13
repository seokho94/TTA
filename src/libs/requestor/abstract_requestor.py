from abc import ABC, abstractmethod

class AbstractRequestor(ABC):
    @abstractmethod
    def get(url, method):
        pass

    @abstractmethod
    def post(url, method):
        pass

    @abstractmethod
    def put(url, method):
        pass

    @abstractmethod
    def delete(url, method):
        pass