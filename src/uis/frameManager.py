

class FrameManager:

    def __init__(self, frame):

        self.frame_stack = [frame]

    def addFrame(self, frame):

        self.frame_stack.append(frame)

    def dropFrame(self):

        self.frame_stack.pop()

    def getActiveFrame(self):

        return self.frame_stack[-1]

    def getFrameAt(self, pos):

        return self.frame_stack[pos]

    def getFrameCount(self):

        return len(self.frame_stack)
