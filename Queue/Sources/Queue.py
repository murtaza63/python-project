from typing import Optional, Protocol, TypeVar
from xml.dom.minidom import Element

Element  = TypeVar('Element')

class Queue(Protocol(Element)):
    def enqueue(self, element: Element) -> bool: ...
    def dequeue(self) -> Optional[Element]: ...
    def is_empty(self) -> bool: ...
    def peek(self) -> Optional[Element]: ...