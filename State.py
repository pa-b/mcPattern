from abc import ABC, abstractmethod

#from State import Pending, Progress, Done


class StateMachine(object):

    def __init__(self, initState):
        print("State machine innit")
        self.state = initState
        self.state.run()

    def set_next(self):
        self.state = self.state.next()
        self.state.run()
        # self.state = self.state.next()
        # self.state.run()


class Pending(object):

    def run(self):
        print("Order state: pending")

    def next(self):
        return State.progress

    # def __init__(self):
    #     pass


class Progress(object):

    def run(self):
        print("Order state: progress")

    def next(self):
        return State.done


class Done(object):

    def run(self):
        print("Order state: done")

    def next(self):
        #pass
        #print("done")
        return State.done


class State(StateMachine):

    pending = Pending()
    progress = Progress()
    done = Done()

    def __init__(self):
        super(State, self).__init__(State.pending)
        #self.state = State.pending

    # def set_state(self):
    #     self._state = self.__class__

    # def run(self):
    #     print("Order state: pending")
    #
    # def next_state(self):
    #     return State.

